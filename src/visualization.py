"""Vẽ hai mẫu bằng thang trục và quy ước thống kê thống nhất."""

from pathlib import Path

import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

from .descriptive_stats import summarize


_DPI = 300
_GROUPS = ("A", "B")
_COLORS = {"A": "#1364a3", "B": "#a84319"}
_DARK = "#1d2c3a"


def _counts(values: np.ndarray, edges: np.ndarray) -> np.ndarray:
    # Điểm đúng biên trong được đếm vào khoảng thấp hơn (§3.3.2).
    bins = np.searchsorted(edges[1:-1], values, side="left")
    return np.bincount(bins, minlength=len(edges) - 1)


def save_figures(a, b, output_dir: Path) -> dict:
    """Xuất hai ảnh PNG và lưu thông số có thể dùng để kiểm tra hình."""
    samples = {group: np.asarray(values, dtype=float) for group, values in zip(_GROUPS, (a, b))}
    stats = {group: summarize(values) for group, values in samples.items()}
    output_dir.mkdir(parents=True, exist_ok=True)

    # Hai nhóm n=40 dùng sáu khoảng lớp chung theo gợi ý căn bậc hai của n.
    lower = min(summary["min"] for summary in stats.values())
    upper = max(summary["max"] for summary in stats.values())
    if lower == upper:
        lower, upper = lower - 0.5, upper + 0.5
    edges = np.linspace(lower, upper, 7)
    counts = {group: _counts(values, edges) for group, values in samples.items()}
    densities = {
        group: counts[group] / (stats[group]["n"] * np.diff(edges))
        for group in _GROUPS
    }
    _save_histogram(edges, densities, output_dir / "histogram.png")
    _save_boxplot(samples, stats, output_dir / "boxplot.png")
    return {
        "histogram_edges_ms": edges.tolist(),
        "histogram_counts": {group: counts[group].tolist() for group in _GROUPS},
        "histogram_density_per_ms": {group: densities[group].tolist() for group in _GROUPS},
        "boxplot_whiskers": "min_max",
        "dpi": _DPI,
    }


def _save_histogram(edges: np.ndarray, densities: dict, path: Path) -> None:
    figure = Figure(figsize=(8.4, 4.0), layout="constrained")
    FigureCanvasAgg(figure)
    axes = figure.subplots(1, 2, sharex=True, sharey=True)
    figure.suptitle("Histogram độ trễ theo phương án định tuyến", color=_DARK, fontweight="bold")
    for group, ax in zip(_GROUPS, axes):
        ax.stairs(
            densities[group], edges, fill=True, color=_COLORS[group], alpha=0.75
        )
        ax.set_title(f"Phương án {group}", color=_COLORS[group], loc="left")
        ax.set_xlabel("Độ trễ (ms)")
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#dde5ec")
        ax.spines[["top", "right"]].set_visible(False)
    # Đặt giới hạn chung sau khi vẽ cả hai nhóm để giữ trọn cột cao nhất.
    peak_density = max(float(values.max()) for values in densities.values())
    axes[0].set_ylim(0, 1.08 * peak_density)
    axes[0].set_ylabel("Mật độ (1/ms)")
    figure.savefig(path, dpi=_DPI)


def _save_boxplot(samples: dict, stats: dict, path: Path) -> None:
    figure = Figure(figsize=(8.4, 3.6), layout="constrained")
    FigureCanvasAgg(figure)
    ax = figure.subplots()
    ax.set_title("Boxplot độ trễ theo phương án định tuyến", color=_DARK, fontweight="bold")

    for position, group in enumerate(_GROUPS, start=1):
        summary = stats[group]
        # Dùng năm số của cùng bảng thống kê để hình không đổi cách tính tứ phân vị.
        box = {
            "med": summary["median"],
            "q1": summary["q1"],
            "q3": summary["q3"],
            "whislo": summary["min"],
            "whishi": summary["max"],
        }
        ax.bxp(
            [box],
            positions=[position],
            orientation="horizontal",
            widths=0.27,
            patch_artist=True,
            showfliers=False,
            manage_ticks=False,
            boxprops={"facecolor": _COLORS[group], "edgecolor": _DARK, "alpha": 0.65},
            medianprops={"color": _DARK, "linewidth": 2},
        )
        # Trải điểm nhẹ theo chiều đứng để thấy từng giá trị, không thay tọa độ độ trễ.
        spread = np.linspace(position - 0.26, position - 0.18, summary["n"])
        ax.scatter(samples[group], spread, s=10, color=_COLORS[group], alpha=0.68, zorder=3)

    ax.set_yticks([1, 2], ["Phương án A", "Phương án B"])
    ax.invert_yaxis()
    ax.set_xlabel("Độ trễ (ms) · Râu từ giá trị nhỏ nhất đến lớn nhất")
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#dde5ec")
    ax.spines[["top", "right", "left"]].set_visible(False)
    figure.savefig(path, dpi=_DPI)
