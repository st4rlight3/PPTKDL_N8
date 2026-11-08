# Kết quả chạy với seed 8

Mẫu chính gồm 40 quan sát mô phỏng ở mỗi nhóm. Bảng sử dụng đơn vị ms cho trung bình, trung vị, SD và IQR. Kết quả đầy đủ trước khi làm tròn nằm trong tệp CSV và JSON. [Dữ liệu chính](../data/samples.csv) · [Kết quả đầy đủ](../results/run.json)

| Nhóm | Trung bình | Trung vị | Độ lệch chuẩn mẫu | IQR |
|---|---:|---:|---:|---:|
| A | 29,809215 | 28,034122 | 9,272726 | 12,726183 |
| B | 26,315876 | 23,053491 | 10,504564 | 8,192340 |

Mẫu B có trung bình và trung vị thấp hơn, nửa giữa hẹp hơn và SD lớn hơn mẫu A. Hai biểu đồ 300 dpi giữ toàn bộ miền quan sát. [Histogram](../figures/histogram.png) · [Boxplot](../figures/boxplot.png)

## Hai kiểm định ở mức 5%

| Phương pháp | Thống kê | p hai phía | Quyết định |
|---|---|---:|---|
| Mann–Whitney | R<sub>A</sub> = 1.890, R<sub>B</sub> = 1.350, U<sub>A</sub> = 1.070, U<sub>B</sub> = 530, z = 2,593265 | 0,0095069497 | Bác bỏ H₀ về phân phối |
| Welch | t = 1,576805, ν = 76,817153, bậc tự do dùng là 76 | 0,1189939968 | Chưa bác bỏ H₀ về trung bình |

Tổng hạng là 3.240 và tổng U là 1.600. Đếm cặp trực tiếp cho 1.070 cặp A > B, 530 cặp B > A và 0 cặp bằng nhau. SciPy cho cùng U<sub>A</sub> và p = 0,009506949692480346 với xấp xỉ chuẩn, hiệu chỉnh liên tục và hai phía. Với Welch, SciPy cho p = 0,11894990248043129 khi dùng ν thập phân. Chênh lệch p của Welch phản ánh quy ước bậc tự do. [Bảng xếp hạng](../results/ranks.csv) · [Phương pháp](METHODOLOGY.md)

## Lặp mô phỏng

147 trong 200 lần bác bỏ H₀, cho tỷ lệ 73,5%. Cả 200 lần đều có cặp mẫu mới, mỗi nhóm 40 giá trị. Không có hạng trùng trong các lượt sinh với seed này. U và p-value khớp với SciPy trong tất cả các lần đối chiếu. Chênh lệch p lớn nhất trong 200 lần là 1,94 × 10⁻¹⁶. [Bảng từng lần](../results/simulation_runs.csv) · [Dữ liệu từng lần](../data/simulation_samples.csv)
