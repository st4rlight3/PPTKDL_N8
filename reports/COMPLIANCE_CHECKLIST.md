# Bảng kiểm tuân thủ

Đối chiếu với [quy định chung, Đề 8 và sản phẩm nộp](REQUIREMENTS.md). PASS nghĩa là đã thực hiện và xác minh. FAIL nghĩa là yêu cầu thuộc phạm vi bàn giao chưa đạt. BLOCKED nghĩa là cần đầu vào, quyền truy cập hoặc phần việc của nhóm.

## Lớp 1 · Căn cứ bài giảng

| Nội dung | Bằng chứng rà soát | Trạng thái |
|---|---|---|
| Số trang, công thức và ký hiệu | Đọc ảnh kết xuất của cả 12 trang bộ đề. Kiểm tra lại các trang bài giảng chứa công thức quyết định, Bảng 5.7 và mục 7.2.1 trên ảnh trang gốc. [Đối chiếu chương, mục, trang](SOURCE_MAPPING.md) | PASS |
| Phân phối mũ, độc lập, thống kê mẫu và biểu đồ | Tham số tỷ lệ suy từ kỳ vọng ở §1.5.2.2, hai luồng độc lập theo thiết kế, SD dùng mẫu số n − 1, nội suy h = (n + 1)p và boxplot tóm tắt năm số. Bảng đối chiếu phân biệt công thức trực tiếp và quy ước triển khai. | PASS |
| Công thức U và giả thuyết Mann–Whitney | [ISSUES.md](ISSUES.md) ghi công thức in ở trang 212, phép thử số học, bất nhất về giả thuyết một phía và quy ước đếm cặp hai phía đã được người dùng xác nhận. Tổng hạng, U, p-value và chiều diễn giải khớp dữ liệu. | PASS |
| p-value hai phía, hiệu chỉnh liên tục và ties | Đối chiếu §7.2.1, trang 213, quy tắc hạng trung bình ở §7.3.1 và phần hiệu chỉnh phương sai được người dùng xác nhận. Đối chiếu thư viện trên cả 201 cặp mẫu và kiểm thử riêng các giá trị trùng. Mann–Whitney dùng p ≤ α theo §7.2.1. | PASS |
| Welch và điều kiện áp dụng | (5.38), (5.40), Bảng 5.7 và trang 159 cho công thức, kiểm định hai phía và quy ước làm tròn xuống bậc tự do. Báo cáo tách kết quả này với SciPy giữ bậc tự do thập phân và trình bày giới hạn xấp xỉ trên mẫu mũ dịch. | PASS |
| Diễn giải và dẫn nguồn | Báo cáo phân biệt giả thuyết phân phối và trung bình, có điều kiện cùng dạng khi đọc dịch vị trí, phân biệt tham số mô hình và thống kê mẫu. Các khác biệt về căn cứ và quy ước được ghi trong [METHODOLOGY.md](METHODOLOGY.md) và [SOURCE_MAPPING.md](SOURCE_MAPPING.md). | PASS |

## Lớp 2 · Yêu cầu bộ đề và sản phẩm

| Vị trí | Yêu cầu | Mã, đầu ra và bằng chứng | Trạng thái |
|---|---|---|---|
| Trang 1, §1 | Mục tiêu học tập | Báo cáo §1–9 trình bày thiết kế mô phỏng, kiến thức áp dụng, cách đọc kết quả và giới hạn suy luận. | PASS |
| Trang 1, §2.1 | Nhóm 4–5 sinh viên, thời gian dự kiến 3 tuần | Đã nhận danh sách 5 thành viên. Báo cáo công khai dùng mã 01–05. Thời gian dự kiến thuộc kế hoạch tổ chức của nhóm. | PASS |
| Trang 1, §2.2 | Công cụ và bước xử lý | [README.md](../README.md), [METHODOLOGY.md](METHODOLOGY.md) và trường môi trường của [run.json](../results/run.json) ghi Python, phiên bản thư viện và quy trình. | PASS |
| Trang 1, §2.3 | Dữ liệu mô phỏng | Báo cáo §1, §3, §9 và cấu hình `simulated_data` trong run.json xác định rõ nguồn mô phỏng. | PASS |
| Trang 1, §2.4 | Seed, dữ liệu, mã và kết quả tái lập | Có seed 8, hai CSV dữ liệu, toàn bộ mã và tám tệp đầu ra có SHA-256 khớp khi chạy lại. [Nhật ký chạy lại](../results/verification.txt) | PASS |
| Trang 1, §2.5 | Mức ý nghĩa 5%, mức tin cậy 95% | Mức 0,05 được dùng trong cả hai kiểm định. Mức 95% là quy ước cho các khoảng tin cậy được yêu cầu. Đề 8 chỉ định kiểm định và mô tả. | PASS |
| Trang 1, §2.6 | Ước lượng từ mẫu | Kiểm tra lại trung bình, trung vị, phương sai, SD và các phân vị từ CSV bằng hàm thư viện chuẩn Python. Số 20, 16 và 10 ms nằm ở cấu hình mô hình. | PASS |
| Trang 1, §2.7 | Lựa chọn, điều kiện và ý nghĩa thực tế | [Báo cáo](FINAL_REPORT.md) §2, §6–9 giải thích thiết kế, từng kiểm định, bằng chứng và giới hạn khi ứng dụng vào độ trễ mạng. | PASS |
| Trang 1, quy ước và trang 9, thiết kế | Hai mẫu độc lập 40 + 40, phân phối mũ dịch, mẫu mới từng lần lặp | [`make_streams`, `draw_samples`](../src/generate_data.py) tách hai luồng PCG64 từ seed gốc, dùng scale 10 và dịch 20/16. Kiểm tra tái sinh từng khối và 402 khối khác nhau. | PASS |
| Trang 9, YC1 | Trung bình, trung vị, SD, IQR | [`summarize`](../src/descriptive_stats.py), [descriptive.csv](../results/descriptive.csv), báo cáo §3. Tính lại từ dữ liệu bằng `statistics.mean`, `statistics.stdev`, `statistics.quantiles(method="exclusive")`. | PASS |
| Trang 9, YC2 | Histogram và boxplot | [`save_figures`](../src/visualization.py), [histogram.png](../figures/histogram.png), [boxplot.png](../figures/boxplot.png), báo cáo §4–5. Mỗi hình 300 DPI, đọc được trục ms. Kiểm tra đủ 40 điểm mỗi nhóm, diện tích histogram và trục chung giữ trọn hai đỉnh. | PASS |
| Trang 9, YC3 | Mann–Whitney hai phía | [`mann_whitney_test`](../src/mann_whitney.py), run.json và báo cáo §6. U ứng với A bằng 1.070, p = 0,0095069497. Kiểm tra độc lập bằng đếm cặp chéo và xác suất đuôi chuẩn. | PASS |
| Trang 9, YC4 | Gộp, xếp hạng, ties và tính U | [`pooled_ranks`](../src/mann_whitney.py), [ranks.csv](../results/ranks.csv). 80 dòng có nhóm, chỉ số gốc và hạng tăng dần. Tổng hạng 3.240, U hai nhóm cộng 1.600. Kiểm thử hạng trung bình trong và giữa nhóm. | PASS |
| Trang 9, YC5 | t Welch và so sánh | [`welch_test`](../src/welch_test.py), run.json, báo cáo §7. Tính lại t = 1,576805, ν = 76,817153, p = 0,118994 với bậc tự do 76. So sánh đại lượng được kiểm định trong hai phương pháp. | PASS |
| Trang 9, YC6 | 200 lần, tỷ lệ phát hiện | [`run_simulation`](../src/simulation.py), [simulation_runs.csv](../results/simulation_runs.csv), báo cáo §8. Tính lại U, p-value và quyết định từ CSV của 200 lần. Bác bỏ 147 lần, tỷ lệ 73,5%. | PASS |
| Trang 9, YC7 | Giải thích thiết kế độc lập | Báo cáo §8 giải thích khác biệt giữa chỉ số lượt sinh và cặp có liên kết do thiết kế, nêu ví dụ cùng kịch bản mạng. | PASS |
| Trang 9, kết luận | Phương án có độ trễ thấp hơn và điều kiện dịch vị trí | Báo cáo §9 phân biệt dịch 4 ms của mô hình với số đo mô phỏng, nêu cả hai kết quả kiểm định, tỷ lệ phát hiện và phạm vi diễn giải. | PASS |
| Trang 12, sản phẩm 1 | Báo cáo 8–12 trang | [FINAL_REPORT.md](FINAL_REPORT.md) và [bản dàn trang](FINAL_REPORT.pdf). Kiểm tra 10 trang A4 bằng `pdfinfo`, đối chiếu nội dung, bảng và hai hình trên PNG kết xuất. | PASS |
| Trang 12, sản phẩm 2 | Dữ liệu chi tiết và bảng kết quả lặp | [Mẫu chính](../data/samples.csv) có 80 dòng. [Dữ liệu lặp](../data/simulation_samples.csv) có 16.000 dòng. [Bảng lần lặp](../results/simulation_runs.csv) có 200 dòng và lưu p-value, quyết định. | PASS |
| Trang 12, sản phẩm 3 | Mã, seed và lệnh chạy lại | [README.md](../README.md) hướng dẫn cài gói, `python -m src.main` và seed. Đã kiểm tra chạy thật và tái lập. | PASS |
| Trang 12, sản phẩm 4 | Bài trình chiếu 8–10 trang | Người dùng phụ trách phần trình chiếu. | BLOCKED |
| Trang 12, sản phẩm 5 | Phân công và đóng góp | Phụ lục B có 5 mã thành viên. Chờ nhóm cung cấp phần việc và đóng góp thực tế. | BLOCKED |
| Trang 12, đoạn cuối | Vai trò kiến thức chương 1–5 | Báo cáo §2 có bảng riêng về từng chương và vai trò đối với phân tích chính ở chương 7. | PASS |

## Lớp 3 · Thực thi và kiểm thử

| Hạng mục | Bằng chứng | Trạng thái |
|---|---|---|
| Môi trường và chạy từ đầu đến cuối | Windows, Python 3.12.14, NumPy 2.3.5, SciPy 1.16.3, Matplotlib 3.10.8, Pillow 13.0.0. Chạy `python -m src.main --seed 8` thành công. [Cấu hình thực tế](../results/run.json) | PASS |
| Tính đúng từ tệp đầu ra | Lần kiểm tra độc lập đọc CSV và tính lại thống kê mẫu, 80 hạng, Welch, U bằng đếm cặp và p Mann–Whitney bằng hàm erfc ở 201 cặp mẫu. Không có p-value bằng 0,05 trong lần chạy này. | PASS |
| Mẫu mới và tái lập | Tái sinh đúng cả 16.080 quan sát từ hai luồng. 402 khối 40 quan sát khác nhau. Hai lần chạy cùng seed khớp SHA-256 trên năm CSV, một JSON và hai PNG. [Nhật ký](../results/verification.txt) | PASS |
| Kiểm thử tự động | `python -m unittest discover -s tests -v`. 15 kiểm thử đạt, gồm tham số sinh, tái lập, phân vị, hình, giới hạn trục histogram, ties, hiệu chỉnh liên tục và Welch. [Nhật ký](../results/verification.txt) | PASS |
| Kiểm tra bằng mắt | Kiểm tra hai hình và toàn bộ bản PDF. Lỗi cắt đỉnh nhóm B ở lần vẽ đầu đã được sửa, chạy lại và có kiểm thử hồi quy. | PASS |
| GitHub | Đã push nhánh `PPTKDL_N8` và đối chiếu SHA cục bộ với `git ls-remote`. [Kho công khai](https://github.com/st4rlight3/PPTKDL_N8/tree/PPTKDL_N8) | PASS |

Lần rà soát cuối kiểm tra lại bộ đề trang 1, 9 và 12, toàn bộ tệp thống kê, hai biểu đồ, bảng 200 lần và hướng dẫn tái lập. Không có mục FAIL thuộc phạm vi phân tích và kiểm thử. Các mục BLOCKED được liệt kê theo sản phẩm còn cần hoàn tất.
