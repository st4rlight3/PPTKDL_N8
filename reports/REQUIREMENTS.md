# Yêu cầu Đề 8 và quy định nộp bài

## Kiểm kê và đối chiếu bản gốc

| Tệp đầu vào | Vai trò |
|---|---|
| `Bo_de_bai_tap_nhom_Phuong_phap_thong_ke_du_lieu_sinh_vien.pdf` | Bộ đề của môn học. Nguồn quy định đề tài, thiết kế mô phỏng và sản phẩm nộp. |
| `Bai giang TK va PT DL_v2_edit_1.pdf` | Giáo trình. Vị trí, công thức và giới hạn của các căn cứ được ghi tại [SOURCE_MAPPING.md](SOURCE_MAPPING.md). |

Thư mục ban đầu chứa hai PDF trên và không có tài liệu bổ sung. Bộ đề có 12 trang theo `pdfinfo`, với số trang in khớp số trang PDF. Cả 12 trang được trích văn bản bằng `pypdf`, kết xuất thành ảnh bằng `pdftoppm -r 132 -png` và đọc trên ảnh trang gốc. Không có trang bị thiếu hoặc không đọc được. Các trang 2–8 và 10–11 chứa chín đề còn lại. Trang 1 chứa quy định chung, trang 9 chứa toàn bộ Đề 8 và trang 12 chứa quy cách nộp chung. Ba trang liên quan không có bảng, hình hoặc chú thích chân trang cần đọc thêm. Bản trích văn bản có vài khoảng trắng chen vào từ (chẳng hạn “đ ộ trễ”, “phân ph ối” ở trang 9). Bản chép bên dưới được đối chiếu với hình trang gốc để giữ đúng dấu, chỉ số và ký hiệu (Z′).

## Văn bản bộ đề

### Trang in 1, trang PDF 1

> **BỘ ĐỀ BÀI TẬP NHÓM**
>
> **Phương pháp thống kê dữ liệu**
>
> Trọng tâm chương 6 và chương 7 kết hợp kiến thức các chương trước
>
> Bộ đề gồm 10 tình huống trong viễn thông và dịch vụ số. Sinh viên sử dụng máy tính để tạo dữ liệu, phân tích thống kê và đưa ra kết luận có căn cứ. Mỗi nhóm thực hiện một đề theo phân công của giảng viên; không cần thiết bị đo chuyên dụng.
>
> **1. Mục tiêu học tập**
>
> Vận dụng hồi quy và kiểm định phi tham số; kết hợp kiến thức về biến ngẫu nhiên, phân phối xác suất, mẫu, thống kê mô tả và ước lượng. Rèn luyện thiết kế thực nghiệm mô phỏng, phân tích kết quả và trình bày giới hạn của kết luận.
>
> **2. Yêu cầu chung**
>
> 1. Mỗi nhóm 4–5 sinh viên; thời gian thực hiện dự kiến 3 tuần.
> 2. Sử dụng Python, MATLAB hoặc phần mềm thống kê phù hợp. Ghi rõ công cụ và các bước xử lý.
> 3. Dữ liệu trong các đề là dữ liệu mô phỏng. Không trình bày chúng như số đo thực tế.
> 4. Lưu hạt giống ngẫu nhiên (seed), dữ liệu gốc, mã lệnh và kết quả để có thể tái lập.
> 5. Sử dụng mức ý nghĩa 5% và mức tin cậy 95%, trừ khi đề yêu cầu khác.
> 6. Các tham số tạo dữ liệu chỉ dùng để đánh giá phương pháp. Khi phân tích từng mẫu, phải ước lượng từ mẫu, không thay trực tiếp tham số đã biết vào kết quả ước lượng.
> 7. Giải thích cách chọn phương pháp, điều kiện áp dụng và ý nghĩa thực tế; không chỉ chép kết quả phần mềm.
>
> Quy ước: N(μ, σ²) là phân phối chuẩn với trung bình μ và phương sai σ²; U(a, b) là phân phối đều trên [a, b]. Các lần sinh ngẫu nhiên độc lập, trừ quan hệ ghép cặp được nêu rõ. Khi lặp mô phỏng, mỗi lần phải sinh một mẫu mới.

### Trang in 9, trang PDF 9

> **Đề 8  So sánh hai phương án định tuyến bằng dữ liệu độ trễ**
>
> **Tình huống**
>
> Hai phương án định tuyến được thử trên hai nhóm phiên truyền độc lập.
>
> **Kiến thức sử dụng**
>
> Kiểm định Mann–Whitney; mẫu độc lập, dữ liệu lệch và so sánh với kiểm định t Welch.
>
> **Dữ liệu và cách tạo mẫu**
>
> Tạo 40 quan sát cho mỗi phương án: A có X = 20 + Z; B có Y = 16 + Z′. Z và Z′ có phân phối mũ với trung bình 10 ms. Hai mẫu độc lập.
>
> **Yêu cầu thực hiện**
>
> 1. Tính trung bình, trung vị, độ lệch chuẩn và khoảng tứ phân vị cho mỗi nhóm.
> 2. Vẽ histogram và biểu đồ hộp để so sánh.
> 3. Phát biểu giả thuyết và thực hiện kiểm định Mann–Whitney hai phía.
> 4. Trình bày cách gộp hai mẫu, xếp hạng và tính thống kê kiểm định; xử lý hạng trùng nếu có.
> 5. Thực hiện kiểm định t Welch; giải thích khác biệt về đại lượng được kiểm định.
> 6. Lặp mô phỏng 200 lần và tính tỷ lệ phát hiện khác biệt.
> 7. Giải thích vì sao không sử dụng kiểm định ghép cặp cho thiết kế này.
>
> **Kết luận cần trình bày**
>
> Nhận xét phương án có độ trễ thấp hơn trong mô hình đã cho. Mann–Whitney không mặc nhiên là kiểm định trung bình; diễn giải dịch chuyển vị trí dựa trên giả thiết hai phân phối cùng dạng.

### Trang in 12, trang PDF 12

> **Sản phẩm nộp và đánh giá**
>
> **Sản phẩm mỗi nhóm phải nộp**
>
> 1. Báo cáo 8–12 trang: bài toán, thiết kế mô phỏng, thống kê mô tả, phân tích chính, kết luận và hạn chế.
> 2. Tệp dữ liệu của mẫu phân tích chi tiết và bảng kết quả các lần mô phỏng lặp.
> 3. Mã lệnh hoặc tệp phân tích kèm hướng dẫn chạy lại và seed.
> 4. Bài trình chiếu 8–10 trang để báo cáo kết quả.
> 5. Bảng phân công nhiệm vụ và đóng góp của từng thành viên.
>
> Trong báo cáo, dành một mục ngắn chỉ rõ kiến thức chương 1–5 đã dùng và vai trò của chúng đối với nội dung chính ở chương 6 hoặc chương 7.

## Công việc và tiêu chí kiểm tra

| Vị trí | Yêu cầu | Công việc và bằng chứng cần kiểm tra |
|---|---|---|
| Trang 1, §1 | Mục tiêu học tập | Áp dụng kiểm định phi tham số và các kiến thức nền cần thiết cho Đề 8. Giải thích thiết kế, cách đọc kết quả và giới hạn suy luận. |
| Trang 1, §2.1 | Nhóm 4–5 sinh viên, thời gian dự kiến 3 tuần | Nhóm sinh viên xác nhận số thành viên và tự quản lý tiến độ theo phân công của giảng viên. |
| Trang 1, §2.2 | Công cụ và bước xử lý | Nêu phiên bản Python, thư viện, cấu hình và trình tự chạy trong hướng dẫn tái lập. |
| Trang 1, §2.3 | Tính chất dữ liệu | Ghi rõ độ trễ sinh theo mô hình ở bảng kết quả, biểu đồ và báo cáo. |
| Trang 1, §2.4 | Tái lập | Lưu seed, cấu hình, CSV gốc, mã và kết quả. Chạy lại cùng cấu hình để kiểm tra. |
| Trang 1, §2.5 | Mức ý nghĩa và mức tin cậy | Dùng `α = 0,05` cho quyết định kiểm định. Mức tin cậy mặc định 95% áp dụng cho khoảng tin cậy khi được yêu cầu. Đề 8 không chỉ định khoảng tin cậy hoặc tham số cần lập khoảng. |
| Trang 1, §2.6 | Ước lượng từ mẫu | Tính các đặc trưng bằng dữ liệu CSV, tách chúng khỏi tham số 20, 16 và 10 ms dùng để sinh. |
| Trang 1, §2.7 | Giải thích thống kê và ý nghĩa thực tế | Mỗi phương pháp cần có lý do chọn, điều kiện, giả thuyết nếu có kiểm định, cách tính, kết quả và diễn giải trong bài toán định tuyến. |
| Trang 1, Quy ước; trang 9, dữ liệu | Mẫu độc lập và mô hình sinh | Sinh 40 quan sát mỗi nhóm từ các giá trị mũ mới với trung bình 10 ms, cộng 20 ms cho A và 16 ms cho B. Không ghép cặp, không dùng lại giá trị đã sinh khi lặp. |
| Trang 9, yêu cầu 1 | Thống kê mô tả | Tính riêng trung bình, trung vị, độ lệch chuẩn mẫu và IQR. Nêu quy ước tính độ lệch chuẩn và tứ phân vị, so sánh bằng bảng. |
| Trang 9, yêu cầu 2 | Hai loại biểu đồ | Vẽ histogram và biểu đồ hộp từ cùng mẫu. Kiểm tra phạm vi, thang đo ms, tiêu đề và hình xuất PNG. Diễn giải hình dạng, mức điển hình, độ phân tán và điểm nằm ngoài râu nếu có. |
| Trang 9, yêu cầu 3 | Mann–Whitney hai phía | Nêu giả thuyết, điều kiện, thống kê, p-value, quyết định ở 5% và ý nghĩa. Phương pháp p-value cần đối chiếu với giáo trình, vì bộ đề chỉ quy định số phía. |
| Trang 9, yêu cầu 4 | Gộp và xếp hạng | Gộp 80 quan sát, sắp tăng dần, ghi hạng và mã gốc, dùng hạng trung bình cho các giá trị trùng. Kiểm tra tổng hạng và thống kê kiểm định với thư viện theo cùng quy ước. |
| Trang 9, yêu cầu 5 | t Welch | Phân tích trên cùng mẫu với giả thuyết về trung bình, thống kê t, bậc tự do, p-value, điều kiện và giới hạn áp dụng. So sánh đại lượng được kiểm định với Mann–Whitney. |
| Trang 9, yêu cầu 6 | Lặp 200 lần | Sinh hai mẫu mới 40 quan sát ở từng lần. Yêu cầu bàn giao xác định rõ kiểm định Mann–Whitney hai phía cho cả 200 lần. Lưu từng p-value, quyết định, số lần bác bỏ và tỷ lệ trên 200. |
| Trang 9, yêu cầu 7 | Thiết kế độc lập | Giải thích chỉ số quan sát không tạo ra liên kết giữa hai phiên. Nêu khi nào dữ liệu thực sự có cấu trúc ghép cặp. |
| Trang 9, kết luận | Độ trễ và diễn giải kiểm định | Xác định B thấp hơn theo phân phối đã thiết kế. Đối chiếu với mô tả mẫu và các kiểm định đã được xác nhận. Điều kiện cùng dạng cho phép diễn giải theo dịch chuyển vị trí. Tách kết luận mô hình khỏi bằng chứng quan sát. |
| Trang 12, sản phẩm 1 | Báo cáo 8–12 trang | Viết báo cáo học thuật tiếng Việt theo nội dung quy định. Bản bàn giao chính là Markdown. Số trang cần kiểm tra trên bản dàn trang dùng để nộp. |
| Trang 12, sản phẩm 2 | Tệp dữ liệu và bảng kết quả lặp | Kiểm tra CSV chi tiết đủ 80 quan sát và bảng đủ 200 lần chạy với các trường yêu cầu. |
| Trang 12, sản phẩm 3 | Mã và hướng dẫn | Kiểm tra lệnh chạy toàn bộ, phiên bản thư viện và cấu hình seed. |
| Trang 12, sản phẩm 4 | Trình chiếu 8–10 trang | Người dùng phụ trách theo chỉ dẫn bàn giao. |
| Trang 12, sản phẩm 5 | Phân công và đóng góp | Nhóm cung cấp danh sách và phần việc thực tế của từng thành viên để điền vào bảng. |
| Trang 12, đoạn cuối | Liên hệ kiến thức chương 1–5 | Dành một mục ngắn trong báo cáo để chỉ ra các khái niệm thực sự dùng và vai trò của chúng đối với nội dung chính ở chương 7. |

Yêu cầu bàn giao còn quy định tên và cấu trúc các tệp, đối chiếu công thức với giáo trình, chạy và kiểm thử thực tế, ba lớp kiểm tra, cùng commit và push GitHub sau khi giải quyết các điều kiện còn thiếu. Trạng thái xác minh được ghi riêng trong [COMPLIANCE_CHECKLIST.md](COMPLIANCE_CHECKLIST.md).
