"""Lặp lại kiểm định Mann–Whitney trên 200 cặp mẫu mới."""

from .generate_data import draw_samples, sample_rows
from .mann_whitney import mann_whitney_test

REPETITIONS = 200


def run_simulation(streams, alpha: float):
    samples = []
    runs = []
    for iteration in range(1, REPETITIONS + 1):
        a, b = draw_samples(streams)
        samples.extend({"iteration": iteration, **row} for row in sample_rows(a, b))
        result = mann_whitney_test(a, b, alpha)
        runs.append({"iteration": iteration, **result})

    detected = sum(run["reject_h0"] for run in runs)
    summary = {
        "repetitions": REPETITIONS,
        "rejections": detected,
        "detection_rate": detected / REPETITIONS,
        "repetitions_with_ties": sum(run["tie_count"] > 0 for run in runs),
        "max_absolute_p_difference_scipy": max(
            abs(run["p_value"] - run["p_value_scipy"]) for run in runs
        ),
    }
    return samples, runs, summary
