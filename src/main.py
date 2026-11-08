"""Chạy toàn bộ phân tích và lưu đầu ra có thể kiểm chứng."""

import argparse
import csv
import json
import platform
from importlib.metadata import version
from pathlib import Path

from .descriptive_stats import summarize
from .generate_data import (
    DEFAULT_SEED,
    SAMPLE_SIZE,
    SCALE_MS,
    SHIFT_A_MS,
    SHIFT_B_MS,
    draw_samples,
    make_streams,
    sample_rows,
)
from .mann_whitney import mann_whitney_test, pooled_ranks
from .simulation import REPETITIONS, run_simulation
from .visualization import save_figures
from .welch_test import welch_test

ALPHA = 0.05
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def write_csv(path: Path, rows):
    with path.open("w", encoding="utf-8", newline="") as output:
        row_iter = iter(rows)
        first = next(row_iter)
        writer = csv.DictWriter(output, fieldnames=list(first))
        writer.writeheader()
        writer.writerow(first)
        writer.writerows(row_iter)


def run_project(output_dir: Path, seed: int):
    streams = make_streams(seed)
    a, b = draw_samples(streams)
    description = {"A": summarize(a), "B": summarize(b)}
    ranks = pooled_ranks(a, b)
    mann_whitney = mann_whitney_test(a, b, ALPHA)
    welch = welch_test(a, b, ALPHA)
    simulations, runs, simulation_summary = run_simulation(streams, ALPHA)

    data_dir = output_dir / "data"
    results_dir = output_dir / "results"
    figure_dir = output_dir / "figures"
    for directory in (data_dir, results_dir, figure_dir):
        directory.mkdir(parents=True, exist_ok=True)

    figures = save_figures(a, b, figure_dir)
    write_csv(data_dir / "samples.csv", sample_rows(a, b))
    write_csv(data_dir / "simulation_samples.csv", simulations)
    write_csv(results_dir / "descriptive.csv", (
        {"group": group, **summary} for group, summary in description.items()
    ))
    write_csv(results_dir / "ranks.csv", ranks)
    write_csv(results_dir / "simulation_runs.csv", runs)

    result = {
        "configuration": {
            "seed": seed,
            "generator": "NumPy PCG64, SeedSequence.spawn(2)",
            "simulated_data": True,
            "sample_size_per_group": SAMPLE_SIZE,
            "exponential_scale_ms": SCALE_MS,
            "shift_a_ms": SHIFT_A_MS,
            "shift_b_ms": SHIFT_B_MS,
            "alpha": ALPHA,
            "simulation_repetitions": REPETITIONS,
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.system(),
            **{package: version(package) for package in ("numpy", "scipy", "matplotlib", "pillow")},
        },
        "descriptive": description,
        "figures": figures,
        "mann_whitney": mann_whitney,
        "welch": welch,
        "simulation": simulation_summary,
    }
    (results_dir / "run.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return result


def parse_seed(value: str):
    try:
        seed = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("Seed phải là số nguyên.") from error
    if seed < 0:
        raise argparse.ArgumentTypeError("Seed phải không âm.")
    return seed


def main():
    parser = argparse.ArgumentParser(description="Phân tích thống kê Đề 8.")
    parser.add_argument("--seed", type=parse_seed, default=DEFAULT_SEED)
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT)
    args = parser.parse_args()
    run_project(args.output_dir, args.seed)
    print(f"Đã lưu kết quả tại {args.output_dir.resolve()} (seed {args.seed}).")


if __name__ == "__main__":
    main()
