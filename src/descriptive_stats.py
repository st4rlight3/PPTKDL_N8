"""Thống kê mô tả cho các quan sát độ trễ theo đơn vị ms."""

import math

import numpy as np


def summarize(values) -> dict[str, float | int]:
    """Tính các thống kê mẫu theo quy ước phân vị i/(n+1)."""
    sample = np.asarray(values, dtype=float)
    if sample.ndim != 1 or sample.size < 2 or not np.all(np.isfinite(sample)):
        raise ValueError("Mẫu phải là dãy một chiều có ít nhất hai giá trị hữu hạn.")

    # Nội suy tuyến tính giữa các quan sát đã sắp ở vị trí h=(n+1)*p.
    q1, median, q3 = np.quantile(sample, (0.25, 0.50, 0.75), method="weibull")
    variance = float(sample.var(ddof=1))
    return {
        "n": int(sample.size),
        "mean": float(sample.mean()),
        "median": float(median),
        "variance": variance,
        "sd": math.sqrt(variance),
        "q1": float(q1),
        "q3": float(q3),
        "iqr": float(q3 - q1),
        "min": float(sample.min()),
        "max": float(sample.max()),
    }
