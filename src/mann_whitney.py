"""Tính Mann–Whitney hai phía từ bảng hạng gộp của hai mẫu độc lập."""

import math
from itertools import groupby

import numpy as np
from scipy import stats


def pooled_ranks(a, b):
    """Giữ số thứ tự gốc trong mỗi nhóm và gán hạng trung bình cho ties."""
    observations = []
    for group, sample in (("A", a), ("B", b)):
        values = np.asarray(sample, dtype=float)
        if values.ndim != 1 or values.size == 0 or not np.isfinite(values).all():
            raise ValueError(f"Mẫu {group} phải là dãy một chiều gồm các số hữu hạn.")
        observations.extend(
            (float(value), group, observation_id)
            for observation_id, value in enumerate(values, start=1)
        )

    observations.sort(key=lambda observation: observation[0])
    rows = []
    next_rank = 1
    for latency, tied_observations in groupby(observations, key=lambda item: item[0]):
        tied_observations = list(tied_observations)
        tie_size = len(tied_observations)
        # Các giá trị bằng nhau chia đều tổng hạng của những vị trí bị chiếm.
        average_rank = next_rank + (tie_size - 1) / 2
        rows.extend(
            {
                "group": group,
                "observation_id": observation_id,
                "latency_ms": latency,
                "rank": average_rank,
                "tie_size": tie_size,
            }
            for _, group, observation_id in tied_observations
        )
        next_rank += tie_size
    return rows


def rank_summary(rows):
    """Tính tổng hạng từng nhóm và đếm số cụm giá trị trùng."""
    return {
        "rank_sum_a": sum(row["rank"] for row in rows if row["group"] == "A"),
        "rank_sum_b": sum(row["rank"] for row in rows if row["group"] == "B"),
        "tie_count": len({row["latency_ms"] for row in rows if row["tie_size"] > 1}),
    }


def mann_whitney_test(a, b, alpha):
    """Tính U từ tổng hạng và p-value xấp xỉ chuẩn có hiệu chỉnh liên tục."""
    if not 0 < alpha < 1:
        raise ValueError("Mức ý nghĩa phải nằm giữa 0 và 1.")
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    rows = pooled_ranks(a, b)
    summary = rank_summary(rows)
    n_a, n_b = a.size, b.size
    n_total = n_a + n_b
    pair_count = n_a * n_b

    u_a = summary["rank_sum_a"] - n_a * (n_a + 1) / 2
    u_b = summary["rank_sum_b"] - n_b * (n_b + 1) / 2
    u_min, u_max = min(u_a, u_b), max(u_a, u_b)

    # Đối chiếu U theo số cặp chéo, chia đều một điểm nếu hai giá trị bằng nhau.
    pair_a_greater = int(np.count_nonzero(a[:, None] > b))
    pair_equal = int(np.count_nonzero(a[:, None] == b))
    pair_b_greater = pair_count - pair_a_greater - pair_equal
    if (u_a, u_b) != (pair_a_greater + pair_equal / 2, pair_b_greater + pair_equal / 2):
        raise ArithmeticError("U từ tổng hạng khác U từ đếm cặp.")

    mean_u = pair_count / 2
    variance_no_ties = pair_count * (n_total + 1) / 12
    variance_u = variance_no_ties
    if summary["tie_count"]:
        # Dùng phương sai tổng hạng dưới hoán vị nhãn với các hạng trung bình cố định.
        mean_rank = (n_total + 1) / 2
        squared_deviations = sum((row["rank"] - mean_rank) ** 2 for row in rows)
        variance_u = pair_count * squared_deviations / (n_total * (n_total - 1))

    if variance_u == 0:
        # Mọi quan sát bằng nhau nên z không xác định và p bằng 1.
        z, p_value = None, 1.0
    else:
        z = (u_max - mean_u - 0.5) / math.sqrt(variance_u)
        p_value = min(1.0, math.erfc(z / math.sqrt(2)))

    scipy_result = stats.mannwhitneyu(
        a, b, alternative="two-sided", method="asymptotic", use_continuity=True,
    )
    if scipy_result.statistic != u_a or not math.isclose(
        scipy_result.pvalue, p_value, rel_tol=1e-12, abs_tol=1e-15,
    ):
        raise ArithmeticError("Kết quả Mann–Whitney khác kết quả đối chiếu SciPy.")

    return {
        **summary,
        "u_a": u_a,
        "u_b": u_b,
        "u_min": u_min,
        "u_max": u_max,
        "z": z,
        "variance_u": variance_u,
        "variance_u_no_ties": variance_no_ties,
        "p_value": p_value,
        "p_value_scipy": float(scipy_result.pvalue),
        "reject_h0": p_value <= alpha,
        "pair_a_greater": pair_a_greater,
        "pair_b_greater": pair_b_greater,
        "pair_equal": pair_equal,
    }
