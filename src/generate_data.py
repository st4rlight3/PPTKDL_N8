"""Sinh hai mẫu độ trễ độc lập theo mô hình của Đề 8."""

import numpy as np

DEFAULT_SEED = 8
SAMPLE_SIZE = 40
SCALE_MS = 10.0
SHIFT_A_MS = 20.0
SHIFT_B_MS = 16.0


def make_streams(seed: int):
    """Tách một seed gốc thành hai luồng cho A và B."""
    seed_a, seed_b = np.random.SeedSequence(seed).spawn(2)
    return (
        np.random.Generator(np.random.PCG64(seed_a)),
        np.random.Generator(np.random.PCG64(seed_b)),
    )


def draw_samples(streams):
    """Mỗi lời gọi tiến cả hai luồng thêm 40 giá trị mũ."""
    stream_a, stream_b = streams
    a = SHIFT_A_MS + stream_a.exponential(SCALE_MS, size=SAMPLE_SIZE)
    b = SHIFT_B_MS + stream_b.exponential(SCALE_MS, size=SAMPLE_SIZE)
    return a, b


def sample_rows(a, b):
    """Giữ thứ tự phát sinh và định danh quan sát trong từng nhóm."""
    for group, values in (("A", a), ("B", b)):
        for index, value in enumerate(values, start=1):
            yield {"group": group, "observation_id": index, "latency_ms": float(value)}
