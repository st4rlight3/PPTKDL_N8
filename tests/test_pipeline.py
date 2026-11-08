"""Kiểm tra mô hình sinh mẫu và toàn bộ tệp do điểm vào chính tạo ra."""

import csv
import json
import tempfile
import unittest
from collections import defaultdict
from pathlib import Path

import numpy as np
from PIL import Image

from src.generate_data import draw_samples, make_streams
from src.main import run_project


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


class DataGenerationTests(unittest.TestCase):
    def test_two_seed_children_and_exponential_parameters(self):
        streams = make_streams(8)
        self.assertIsNot(streams[0], streams[1])
        self.assertEqual(streams[0].bit_generator.seed_seq.spawn_key, (0,))
        self.assertEqual(streams[1].bit_generator.seed_seq.spawn_key, (1,))
        a, b = draw_samples(streams)
        for sample, shift, child in zip((a, b), (20.0, 16.0), np.random.SeedSequence(8).spawn(2)):
            expected = shift + np.random.Generator(np.random.PCG64(child)).exponential(
                scale=10.0, size=40
            )
            np.testing.assert_array_equal(sample, expected)
        self.assertFalse(np.array_equal(a, draw_samples(make_streams(9))[0]))


class PipelineTests(unittest.TestCase):
    def test_outputs_and_reproducibility(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first"
            second = Path(directory) / "second"
            run_project(first, 8)
            run_project(second, 8)

            files = {
                "data/samples.csv",
                "data/simulation_samples.csv",
                "results/descriptive.csv",
                "results/ranks.csv",
                "results/simulation_runs.csv",
                "results/run.json",
                "figures/histogram.png",
                "figures/boxplot.png",
            }
            self.assertEqual(
                {path.relative_to(first).as_posix() for path in first.rglob("*") if path.is_file()},
                files,
            )
            for file in files:
                self.assertEqual((first / file).read_bytes(), (second / file).read_bytes(), file)

            main_rows = read_csv(first / "data/samples.csv")
            self.assertEqual(len(main_rows), 80)
            self.assertEqual(sum(row["group"] == "A" for row in main_rows), 40)
            self.assertEqual(sum(row["group"] == "B" for row in main_rows), 40)
            source = {
                (row["group"], row["observation_id"]): float(row["latency_ms"])
                for row in main_rows
            }
            ranked = read_csv(first / "results/ranks.csv")
            self.assertEqual(len(ranked), 80)
            ranked_values = [float(row["latency_ms"]) for row in ranked]
            self.assertEqual(ranked_values, sorted(source.values()))
            for row in ranked:
                self.assertEqual(float(row["latency_ms"]), source[row["group"], row["observation_id"]])
            self.assertAlmostEqual(sum(float(row["rank"]) for row in ranked), 3240)

            raw_replicates = read_csv(first / "data/simulation_samples.csv")
            self.assertEqual(len(raw_replicates), 16_000)
            runs = read_csv(first / "results/simulation_runs.csv")
            self.assertEqual([int(row["iteration"]) for row in runs], list(range(1, 201)))
            draw_blocks = defaultdict(list)
            for row in raw_replicates:
                draw_blocks[int(row["iteration"]), row["group"]].append(float(row["latency_ms"]))
            self.assertEqual(set(draw_blocks), {(i, g) for i in range(1, 201) for g in ("A", "B")})
            self.assertTrue(all(len(block) == 40 for block in draw_blocks.values()))
            for group in ("A", "B"):
                main_sample = tuple(float(r["latency_ms"]) for r in main_rows if r["group"] == group)
                samples = {tuple(draw_blocks[i, group]) for i in range(1, 201)}
                self.assertEqual(len(samples), 200)
                self.assertNotIn(main_sample, samples)

            summary = json.loads((first / "results/run.json").read_text(encoding="utf-8"))
            for row in runs:
                p = float(row["p_value"])
                self.assertAlmostEqual(p, float(row["p_value_scipy"]), places=12)
                self.assertGreaterEqual(p, 0.0)
                self.assertLessEqual(p, 1.0)
                self.assertEqual(row["reject_h0"] == "True", p <= 0.05)
            n_rejections = sum(row["reject_h0"] == "True" for row in runs)
            self.assertEqual(summary["simulation"]["rejections"], n_rejections)
            self.assertEqual(summary["simulation"]["detection_rate"], n_rejections / 200)
            for file in ("figures/histogram.png", "figures/boxplot.png"):
                with Image.open(first / file) as chart:
                    self.assertEqual(chart.format, "PNG")
                    self.assertGreaterEqual(min(chart.size), 900)
                    self.assertAlmostEqual(chart.info["dpi"][0], 300, places=1)
                    chart.verify()


if __name__ == "__main__":
    unittest.main()
