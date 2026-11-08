"""Kiểm tra quy ước phân vị, phân lớp và ảnh đầu ra."""

import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from matplotlib.figure import Figure
from PIL import Image

from src.descriptive_stats import summarize
from src.visualization import save_figures


class DescriptiveTests(unittest.TestCase):
    def test_quartiles_and_sample_standard_deviation(self):
        summary = summarize([5, 1, 4, 2, 3, 6])
        self.assertEqual(summary["n"], 6)
        self.assertEqual(summary["mean"], 3.5)
        self.assertEqual(summary["median"], 3.5)
        self.assertEqual(summary["q1"], 1.75)
        self.assertEqual(summary["q3"], 5.25)
        self.assertEqual(summary["iqr"], 3.5)
        self.assertEqual(summary["variance"], 3.5)
        self.assertAlmostEqual(summary["sd"], math.sqrt(3.5))
        self.assertEqual((summary["min"], summary["max"]), (1.0, 6.0))

    def test_invalid_samples(self):
        for values in ([], [1], [1, np.nan], [[1, 2], [3, 4]]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                summarize(values)

    def test_histogram_counts_density_and_figure_files(self):
        # Hai mẫu có điểm đúng ở biên trong và tại hai đầu khoảng gộp.
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            metadata = save_figures([0, 1, 2, 6], [1, 3, 4, 5], output)
            self.assertEqual(metadata["histogram_edges_ms"], list(range(7)))
            self.assertEqual(metadata["histogram_counts"]["A"], [2, 1, 0, 0, 0, 1])
            self.assertEqual(metadata["histogram_counts"]["B"], [1, 0, 1, 1, 1, 0])
            widths = np.diff(metadata["histogram_edges_ms"])
            for density in metadata["histogram_density_per_ms"].values():
                self.assertAlmostEqual(np.dot(density, widths), 1.0)
            self.assertEqual(metadata["boxplot_whiskers"], "min_max")
            for name in ("histogram.png", "boxplot.png"):
                with Image.open(output / name) as figure:
                    self.assertEqual(figure.format, "PNG")
                    self.assertGreaterEqual(figure.width, 2000)
                    self.assertAlmostEqual(figure.info["dpi"][0], 300, places=1)

    def test_histogram_shared_axis_contains_both_peaks(self):
        # Mẫu B có cột cao hơn A và được vẽ sau trên cùng thang đo.
        with tempfile.TemporaryDirectory() as folder, patch.object(Figure, "savefig", autospec=True) as save:
            metadata = save_figures([0, 1, 3, 6], [0, 0.2, 0.4, 0.6], Path(folder))
            histogram = save.call_args_list[0].args[0]
            peak_density = max(max(values) for values in metadata["histogram_density_per_ms"].values())
            limits_a, limits_b = (axis.get_ylim() for axis in histogram.axes)
            self.assertEqual(limits_a, limits_b)
            self.assertEqual(limits_a[0], 0)
            self.assertGreater(limits_a[1], peak_density)
