"""So sánh hai trung bình bằng công thức Welch–Satterthwaite."""

import math

import numpy as np
from scipy import stats


def welch_test(a, b, alpha):
    """Kiểm định hai phía với bậc tự do làm tròn xuống theo bài giảng."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if any(sample.ndim != 1 or sample.size < 2 or not np.isfinite(sample).all()
           for sample in (a, b)):
        raise ValueError("Mỗi mẫu Welch phải là dãy một chiều gồm ít nhất hai số hữu hạn.")
    if not 0 < alpha < 1:
        raise ValueError("Mức ý nghĩa phải nằm giữa 0 và 1.")

    n_a, n_b = a.size, b.size
    mean_difference = float(a.mean() - b.mean())
    weight_a = float(a.var(ddof=1)) / n_a
    weight_b = float(b.var(ddof=1)) / n_b
    variance = weight_a + weight_b
    if not math.isfinite(variance) or variance <= 0:
        raise ValueError("Phương sai của hiệu trung bình phải hữu hạn và dương.")

    standard_error = math.sqrt(variance)
    statistic = mean_difference / standard_error
    # Công thức (5.38) sau khi chia tử và mẫu cho bình phương tổng hai trọng số.
    df = 1 / ((weight_a / variance) ** 2 / (n_a - 1)
              + (weight_b / variance) ** 2 / (n_b - 1))
    df_course = math.floor(df)
    p_value = float(2 * stats.t.sf(abs(statistic), df_course))
    scipy_result = stats.ttest_ind(a, b, equal_var=False, alternative="two-sided")
    return {
        "t": statistic,
        "df": df,
        "df_course": df_course,
        "p_value": p_value,
        "p_value_scipy": float(scipy_result.pvalue),
        "reject_h0": p_value < alpha,
        "mean_difference_ms": mean_difference,
        "standard_error_ms": standard_error,
    }
