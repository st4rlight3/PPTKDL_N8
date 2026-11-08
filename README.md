# Đề 8 · So sánh hai phương án định tuyến bằng dữ liệu độ trễ

Dự án Python so sánh hai mẫu độ trễ mô phỏng, mỗi nhóm 40 quan sát. Chương trình sinh mẫu, vẽ hai biểu đồ, tính Mann–Whitney và Welch hai phía, rồi chạy Mann–Whitney trên 200 cặp mẫu mới. Các thống kê dùng độ trễ theo mili giây.

## Cài đặt và chạy

Chạy tại thư mục chứa tệp này với Python 3.12. Kết quả bàn giao dùng Python 3.12.14 và seed gốc 8.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m src.main
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Trên macOS hoặc Linux, thay `.\.venv\Scripts\python.exe` bằng `.venv/bin/python`. Dùng `python -m src.main --seed 8 --output-dir ./tmp/replay` với môi trường đã kích hoạt để tái lập vào thư mục riêng. Chương trình cập nhật các tệp dữ liệu, kết quả và biểu đồ trong thư mục đầu ra. Các báo cáo là bản diễn giải của lần chạy seed 8.

| Tệp | Nội dung |
|---|---|
| [data/samples.csv](data/samples.csv) | 80 quan sát của mẫu chính, theo thứ tự sinh trong từng nhóm |
| [data/simulation_samples.csv](data/simulation_samples.csv) | 16.000 quan sát của 200 lần lặp, có chỉ số lần lặp |
| [results/run.json](results/run.json) | Seed, phiên bản, thống kê mô tả, kiểm định và tỷ lệ phát hiện |
| [results/verification.txt](results/verification.txt) | SHA-256 đối chiếu cùng seed và nhật ký kiểm thử |
| [results/ranks.csv](results/ranks.csv) | Bảng gộp 80 hạng, nhóm và mã quan sát |
| [results/simulation_runs.csv](results/simulation_runs.csv) | Thống kê, p-value, đối chiếu SciPy và quyết định của từng lần lặp |
| [figures/histogram.png](figures/histogram.png) và [figures/boxplot.png](figures/boxplot.png) | Biểu đồ của mẫu chính, 300 dpi |
| [Báo cáo Markdown](reports/FINAL_REPORT.md) và [PDF 10 trang](reports/FINAL_REPORT.pdf) | Báo cáo học thuật và phụ lục |
| [reports/METHODOLOGY.md](reports/METHODOLOGY.md) và [reports/RESULTS.md](reports/RESULTS.md) | Phương pháp và kết quả đã chạy |
| [reports/REQUIREMENTS.md](reports/REQUIREMENTS.md) và [reports/COMPLIANCE_CHECKLIST.md](reports/COMPLIANCE_CHECKLIST.md) | Quy định gốc và bằng chứng kiểm tra |
| [reports/SOURCE_MAPPING.md](reports/SOURCE_MAPPING.md) và [reports/ISSUES.md](reports/ISSUES.md) | Dẫn chiếu bài giảng và cách xử lý điểm bất nhất |

Hai PDF nguồn đặt tại máy dùng để đối chiếu. Thông tin bản nguồn và số trang nằm trong [references/README.md](references/README.md). Chương trình sử dụng mô hình đã ghi trong đề và chạy độc lập với các tệp PDF.
