# Phương pháp và quy ước triển khai

[Đ] và [GT] là bộ đề và bài giảng được định danh trong [tài liệu nguồn](../references/README.md). Số trang dưới đây ghi theo trang in. Bảng đối chiếu ghi thêm số trang PDF. [Bảng đối chiếu giáo trình](SOURCE_MAPPING.md)

## Mô hình và tái lập

Theo [Đ] trang 9, đặt X = 20 + Z và Y = 16 + Z′, trong đó Z và Z′ độc lập, có cùng phân phối mũ với trung bình 10 ms. Từ E(Z) = 1/λ trong [GT] §1.5.2.2, trang 33, suy ra λ = 0,1 ms⁻¹. Hàm `Generator.exponential` dùng tham số tỷ lệ 1/λ, nên chương trình truyền 10. Giá trị dịch 20 và 16 ms xác định cận dưới và tạo cùng hình dạng phân phối ở hai vị trí cách nhau 4 ms. Tính chất kỳ vọng và phương sai khi cộng hằng số nằm ở [GT] §1.3.2.1–2, trang 17–18.

Một seed gốc 8 được chọn trước khi chạy. `SeedSequence.spawn(2)` tạo hai seed con cho hai bộ sinh PCG64 riêng. Mỗi cặp mẫu lấy 40 giá trị mới từ mỗi luồng. Lượt đầu dùng cho phân tích chính. Hai luồng tiến tiếp 200 lượt mà không khởi tạo lại. Sự độc lập là giả thiết thiết kế mô phỏng, được triển khai bằng hai luồng giả ngẫu nhiên riêng, phù hợp với khái niệm mẫu độc lập ở [GT] §1.4.3 và §4.2, trang 24–25 và 99–100. Lưu CSV ở độ chính xác float đầu ra để tái tính và xếp hạng.

## Mô tả và biểu đồ

- Với n quan sát, trung bình là x̄ = Σxᵢ/n. Phương sai mẫu là s² = Σ(xᵢ − x̄)²/(n − 1) và độ lệch chuẩn mẫu là s = √s². Dùng `ddof=1` theo [GT] §3.3.1 và §5.3.2.2, trang 73–74 và 154.
- Tứ phân vị dùng nội suy tuyến tính ở vị trí h = (n + 1)p trên dãy đã sắp xếp, tương ứng `method="weibull"` của NumPy. Đây là quy ước triển khai dựa trên vị trí i/(n + 1) và gợi ý nội suy ở [GT] §3.3.2, trang 76–77, và §5.3.2.1, trang 152. Với n = 40, h lần lượt là 10,25, 20,5 và 30,75. Trung vị là trung bình hai giá trị ở hạng 20 và 21. IQR = Q₃ − Q₁.
- Histogram dùng sáu khoảng lớp đều nhau (gần √40), với cùng mép lớp trên miền dữ liệu gộp. Chiều cao từng cột là số đếm chia cho 40 và bề rộng lớp. Mỗi nhóm có tổng diện tích bằng 1 theo [GT] §3.3.2, trang 74–76.
- Boxplot đặt cạnh nhau theo [GT] §5.3.2.1, trang 151. Hộp biểu thị Q₁–Q₃, đường giữa là trung vị, râu kéo đến min và max theo quy ước tóm tắt năm số của dự án. Điểm quan sát được chồng lên hình. Các giá trị xa vùng giữa được mô tả là điểm cực trị hoặc quan sát ở đuôi, vì hình này dùng râu min–max và không phân loại ngoại lệ theo một ngưỡng riêng.

## Mann–Whitney hai phía

H₀ là Fₓ = Fᵧ, H₁ là Fₓ ≠ Fᵧ. [GT] §7.2–7.2.1, trang 210–213, đặt bài toán cho hai mẫu độc lập từ phân phối liên tục. Cách so sánh bằng thứ hạng phù hợp với độ trễ lệch phải và mô hình cùng dạng dịch vị trí. Ý nghĩa vị trí dựa trên mô hình đó. Thứ hạng được tính trên mẫu gộp.

1. Sắp tăng 80 giá trị và giữ lại nhóm cùng số thứ tự gốc. Các giá trị bằng nhau nhận trung bình của các hạng bị chiếm. Quy tắc hạng trung bình chuyển từ [GT] §7.3.1, trang 214, vì §7.2.1 xét trường hợp không có ties.
2. Tính tổng hạng R<sub>A</sub>, R<sub>B</sub>. Trừ nⱼ(nⱼ+1)/2 để ra Uⱼ theo quy ước đã được người dùng xác nhận. U<sub>A</sub> đếm số cặp chéo có A > B cộng nửa số cặp bằng nhau. Mã tính lại theo đếm cặp và kiểm tra cả hai chiều. Hai U cộng lại thành n<sub>A</sub>n<sub>B</sub>. Các công thức in tại trang 212 có mâu thuẫn với trang 213. [Giải trình và phép kiểm chứng](ISSUES.md)
3. Khi không có ties, lấy μᵤ = n<sub>A</sub>n<sub>B</sub>/2 và σᵤ² = n<sub>A</sub>n<sub>B</sub>(N + 1)/12 với N = n<sub>A</sub> + n<sub>B</sub> theo (7.8). Với U* = max(U<sub>A</sub>,U<sub>B</sub>), dùng z = (U* − μᵤ − 0,5)/σᵤ và p = min(1, 2P(Z ≥ z)) với Z chuẩn tắc, theo xấp xỉ chuẩn có hiệu chỉnh liên tục ở trang 213. Bác bỏ H₀ nếu p ≤ 0,05 theo §7.2.1.
4. Khi có ties, phần mở rộng kỹ thuật đã được xác nhận dùng σᵤ² = n<sub>A</sub>n<sub>B</sub> Σ(rᵢ − (N + 1)/2)²/[N(N − 1)], tính trên các hạng trung bình. Biểu thức tương đương n<sub>A</sub>n<sub>B</sub>[N + 1 − Σ(tₖ³ − tₖ)/(N(N − 1))]/12, với tₖ là kích thước cụm hạng trùng. Chứng minh và giới hạn nguồn nằm trong ISSUES.md. Khi mọi giá trị giống nhau, σᵤ² = 0, z không xác định và p = 1.
5. Với mẫu chính và mỗi lần lặp, gọi `scipy.stats.mannwhitneyu(a, b, alternative="two-sided", method="asymptotic", use_continuity=True)`. SciPy trả U của mẫu thứ nhất. Chương trình dừng nếu U hoặc p-value không khớp với tính tay trong dung sai số đã đặt.

## Welch hai phía

Đặt H₀ là μ<sub>A</sub> − μ<sub>B</sub> = 0 và H₁ là μ<sub>A</sub> − μ<sub>B</sub> ≠ 0. Theo [GT] §5.3.2.2, (5.38), (5.40) và Bảng 5.7, trang 159–160, tính wⱼ = sⱼ²/nⱼ, SE = √(w<sub>A</sub> + w<sub>B</sub>) và t = (x̄ − ȳ)/SE. Bậc tự do ν = (w<sub>A</sub> + w<sub>B</sub>)²/[w<sub>A</sub>²/(n<sub>A</sub> − 1) + w<sub>B</sub>²/(n<sub>B</sub> − 1)]. Tính p hai phía bằng `2 * scipy.stats.t.sf(abs(t), floor(ν))` theo quy ước làm tròn xuống ở trang 159, và bác bỏ khi p < 0,05 theo §5.1.3.3. Ghi thêm p của `ttest_ind(a, b, equal_var=False, alternative="two-sided")` với ν thập phân để đối chiếu.

Welch dùng hai mẫu độc lập và hai ước lượng phương sai riêng. Dẫn xuất xấp xỉ t trong bài giảng đặt trong bối cảnh tổng thể chuẩn. Dữ liệu Đề 8 là mũ dịch. Việc dùng Welch là yêu cầu của đề, với chênh lệch trung bình được xấp xỉ theo lập luận mẫu lớn ở [GT] §4.4.1 và §5.3.2.2. Cỡ mẫu 40 mỗi nhóm không bảo đảm xấp xỉ có mức danh nghĩa chính xác. Hai kiểm định có đối tượng khác nhau ngay cả khi quyết định cùng chiều.

## Mô phỏng và thiết kế độc lập

Ở mỗi lần trong 200 lần, sinh hai mẫu mới rồi áp dụng Mann–Whitney với đúng quy ước và mức ý nghĩa của mẫu chính. Tỷ lệ phát hiện là tổng số quyết định bác bỏ chia 200. Đây là tần suất quan sát của kiểm định dưới cấu hình cụ thể của đề, liên hệ với xác suất bác bỏ theo [GT] §5.1.3.2 và §5.2.1.2. Nó thay đổi theo seed, cỡ mẫu, mức dịch, mức ý nghĩa và quy tắc kiểm định. Với 200 lần, mỗi quyết định thay đổi tỷ lệ 0,5 điểm phần trăm.

Trong thiết kế ghép cặp, hai phép đo trong mỗi cặp gắn với cùng đơn vị hoặc hai đơn vị được ghép theo tiêu chí đã định trước. Phân tích khi đó dựa vào sai khác trong các cặp độc lập với nhau theo [GT] §5.3.1, trang 149–151 và §5.3.2.2, trang 161–162. Đề 8 phát sinh riêng hai nhóm. Ghép theo chỉ số dòng sẽ tạo cặp tùy ý từ các quan sát không có liên hệ thiết kế.
