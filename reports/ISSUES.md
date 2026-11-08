# Các vấn đề phát hiện khi đối chiếu tài liệu

Các số trang PDF được đếm từ 1. Tại các mục được dẫn của bài giảng, số trang PDF bằng số trang in cộng 14. Công thức và ký hiệu dưới đây được đối chiếu với ảnh render trang gốc.

## 1. Ký hiệu thống kê U ở mục 7.2.1

**Trạng thái: Quy ước U đã được người dùng xác nhận.** Mâu thuẫn ảnh hưởng đến yêu cầu 3, phần tính U và đối chiếu thư viện của yêu cầu 4, tỷ lệ phát hiện ở yêu cầu 6 và các nội dung tương ứng trong kết luận. Người dùng chấp thuận công thức trừ phần hạng nội bộ và yêu cầu kiểm chứng ties, hiệu chỉnh liên tục, p-value hai phía.

### Công thức đã kiểm tra

Ở mục 7.2.1, trang in 212 (PDF 226), bước 1 gọi $u_i$ và $v_j$ là hạng của $x_i$ và $y_j$ khi gộp hai mẫu và xếp tăng dần. Bước 2 in các đẳng thức sau:

$$
U_1=u_1+u_2+\cdots+u_n=\frac{n(n+1)}2+\sum_{i=1}^{n}u_i,
\qquad
U_2=v_1+v_2+\cdots+v_r=\frac{r(r+1)}2+\sum_{j=1}^{r}v_j.
$$

Cùng trang in công thức $U_1+U_2=n(n+1)/2+r(r+1)/2+nr$. Trang in 213 (PDF 227), (7.8), cho $E(U)=nr/2$ và $\operatorname{Var}(U)=nr(n+r+1)/12$. Trang này cũng cho hiệu chỉnh liên tục $z=(U-nr/2-1/2)/\sqrt{nr(n+r+1)/12}$ và quy tắc hai phía $p=2P(U\ge U_{\max})=2P(U\le U_{\min})$.

### Phép kiểm tra số học

Gọi $R_A=\sum_i u_i$ và $R_B=\sum_j v_j$. Với $n=r=40$, xét một mẫu minh họa có toàn bộ A đứng trước toàn bộ B khi xếp tăng dần. Khi đó $R_A=1+\cdots+40=820$ và $R_B=41+\cdots+80=2420$. Bước 2 cho đồng thời $U_1=820$ và $U_1=820+820=1640$. Nếu cộng hai vế có dấu cộng ở bước 2, tổng là 4880, trong khi công thức tổng trên cùng trang cho 3240. Ngay cả cách đọc $U_1=R_A$ cũng có giá trị nhỏ nhất là 820, cao hơn kỳ vọng 800 ở (7.8). Đây là phép kiểm tra quy ước, độc lập với số liệu mô phỏng của báo cáo.

Mục 7.2, trang in 210 (PDF 224), (7.5), xác định $F_X<F_Y$ theo nghĩa $X$ lớn hơn $Y$ về mặt xác suất và nêu hệ quả $P(X>Y)>1/2$. Trang in 212 (PDF 226) lại giải thích $F_X<F_Y$ là một giá trị từ $X$ **nhỏ hơn** một giá trị từ $Y$ với xác suất lớn hơn $1/2$. Chẳng hạn $X\sim U(2,3)$ và $Y\sim U(0,1)$ cho $F_X\le F_Y$ mọi nơi, nghiêm tại một số điểm, nhưng $P(X<Y)=0$. Trang in 211 (PDF 225) cũng ghi $F_Y>F_X$ cho giả thuyết phía dưới, có cùng chiều bất đẳng thức với phía trên ở (7.6). Hai điểm này liên quan đến phát biểu một phía. Giả thuyết hai phía vẫn được nêu rõ ở trang 211.

### Quy ước đã được xác nhận

Dùng $U_A=R_A-n(n+1)/2$ và $U_B=R_B-r(r+1)/2$. Với hạng tăng dần và các giá trị phân biệt, mỗi hạng A đếm số quan sát đứng trước, cộng một. Cộng các hạng A và trừ tổng $1+\cdots+n$ để bỏ phần thứ tự nội bộ A, ta thu được số cặp $(A_i,B_j)$ có $A_i>B_j$. Vì mỗi cặp chéo thuộc một trong hai chiều, $U_A+U_B=nr$. Với ví dụ trên, $U_A=0$, $U_B=1600$. Cách đếm này tương thích với tâm $nr/2$ của (7.8). Chương trình giữ xấp xỉ chuẩn và hiệu chỉnh liên tục của trang 213, thế $U_{\max}=\max(U_A,U_B)$ và tính $p=\min\{1,2[1-\Phi(z)]\}$. Giới hạn trên 1 giữ kết quả trong miền xác suất khi hai đuôi trùng nhau tại tâm. Mỗi lần kiểm định đối chiếu với `scipy.stats.mannwhitneyu(a, b, alternative="two-sided", method="asymptotic", use_continuity=True)`, trong đó thư viện trả thống kê ứng với đối số thứ nhất. Quy ước được xác nhận và phép đối chiếu kỹ thuật này được phân biệt với công thức in ở trang 212.

## 2. Hạng trùng và phạm vi xấp xỉ chuẩn

Mục 7.2.1, trang in 212–213 (PDF 226–227), giả sử không có ties và không trình bày phương sai U đã hiệu chỉnh cho ties. Mục 7.3.1, trang in 214 (PDF 228), giới thiệu Kruskal–Wallis như mở rộng của kiểm định tổng hạng Wilcoxon và nêu quy tắc gán hạng trung bình khi có giá trị bằng nhau. Bảng hạng áp dụng quy tắc này cho bước xếp hạng gộp, giữ nguyên độ chính xác của quan sát. Khi các vị trí $k$ đến $\ell$ cùng giá trị, mỗi quan sát nhận hạng $(k+\ell)/2$. Suy ra phần đóng góp của một cặp bằng nhau vào thống kê đếm cặp đề xuất là $1/2$ cho mỗi nhóm.

Mô hình sinh liên tục của Đề 8 có xác suất trùng bằng 0 về mặt lý thuyết. Chương trình kiểm tra ties trên các giá trị thực sự được sinh, kể cả trong các lần lặp. Khi có ties, phần mở rộng kỹ thuật dưới đây dùng hạng trung bình cố định và phương sai dưới hoán vị nhãn theo $H_0$. Bước này nằm ngoài mục 7.2.1. Quy tắc gán hạng trung bình ở trang 214 cung cấp căn cứ cho bước xếp hạng.

Đặt $N=n+r$, $q_i$ là hạng gộp, $\bar q=(N+1)/2$ và $I_i$ là chỉ báo vị trí $i$ được gán nhãn A dưới $H_0$. Khi gán đều $n$ nhãn A vào $N$ vị trí, $E(I_i)=n/N$, $\operatorname{Var}(I_i)=nr/N^2$ và $\operatorname{Cov}(I_i,I_j)=-nr/[N^2(N-1)]$ với $i\ne j$. Vì $\sum_i(q_i-\bar q)=0$, phương sai của $U_A$ bằng phương sai của tổng hạng và bằng

$$
\frac{nr}{N(N-1)}\sum_{i=1}^N(q_i-\bar q)^2.
$$

Khi không có ties, tổng bình phương là $N(N^2-1)/12$ và phương sai trở về (7.8). Một cụm ties có $t$ vị trí liên tiếp làm giảm tổng bình phương đúng $t(t^2-1)/12$ khi thay từng hạng bằng trung bình của cụm. Do đó, công thức tương đương $nr[N+1-\sum_t(t^3-t)/(N(N-1))]/12$, cùng hiệu chỉnh với SciPy. Khi mọi quan sát bằng nhau, phương sai bằng 0, $z$ không xác định và $p=1$.

## 3. Phạm vi diễn giải Welch

Đề 8 (PDF 9) yêu cầu Welch trên hai mẫu lệch phải. Bài giảng §5.3.2 trình bày hai mẫu độc lập, công thức (5.37)–(5.40) và xấp xỉ Welch–Satterthwaite ở trang in 158–160 (PDF 172–174), trong phần mô tả hai tổng thể chuẩn với phương sai chưa biết và không gộp. Đề 8 dùng hai phân phối mũ dịch chuyển có cùng độ phân tán theo thiết kế. Thực hiện phép so sánh trung bình theo yêu cầu đề bằng phương sai mẫu riêng, và xem p-value là xấp xỉ trong bài toán này. Định lý giới hạn trung tâm trong §4.4.1, trang in 102–103 (PDF 116–117), hỗ trợ giải thích hành vi trung bình mẫu. Độ chính xác cụ thể ở $n_A=n_B=40$ vẫn là giới hạn diễn giải. Trang in 159 (PDF 173) nêu quy ước làm tròn bậc tự do xuống để tra bảng. Báo cáo phân biệt kết quả theo bậc tự do làm tròn xuống với phép đối chiếu SciPy dùng bậc tự do chưa làm tròn.

## 4. Ký hiệu nguồn ở các phần liên quan

- Bài giảng §1.5.2, trang in 33 (PDF 47), viết $\lambda e^{-\lambda x}$ trong tích phân theo $dy$. Biểu thức CDF in bên phải $1-e^{-\lambda x}$ nhất quán với mật độ in cùng trang và cách nghịch đảo ở Ví dụ 1.13. Chương trình dùng phân phối mũ với tham số trung bình theo đề.
- Ví dụ 1.13, trang in 20 (PDF 34), tính $\tilde\mu=\ln(2)/\lambda$ và $\mu=1/\lambda$, nhưng câu cuối ghi $\mu<\tilde\mu$ cho phân phối lệch phải. Hai giá trị tính được cho chiều ngược lại. Báo cáo dùng giá trị thống kê từ mẫu và mô tả hình dạng theo §3.3.1, trang in 73–74 (PDF 87–88).
- Bài giảng §4.3, trang in 101 (PDF 115), thiếu gạch ngang trên $X$ ở ký hiệu phương sai trong (4.1). Đoạn minh họa §4.4.1, trang in 102 (PDF 116), có ký hiệu phương sai của trung bình mẫu thiếu hệ số $1/n$. Báo cáo dùng định lý giới hạn trung tâm ở dạng chuẩn hóa và hệ thức phương sai hai trung bình độc lập trong (5.30), trang in 154 (PDF 168).

## 5. Thông tin bàn giao

| Hạng mục | Căn cứ | Tình trạng |
|---|---|---|
| Số trang báo cáo | Bộ đề PDF 12, báo cáo 8–12 trang | PASS. Báo cáo dàn trang PDF 10 trang A4, đã kết xuất và kiểm tra từng trang. |
| Thành viên và đóng góp | Bộ đề PDF 1 và 12, nhóm 4–5 sinh viên và bảng đóng góp | Đã có danh sách năm thành viên, lưu riêng tại máy. BLOCKED với mô tả đóng góp thực tế. |
| Bài trình bày | Bộ đề PDF 12, bài trình bày 8–10 trang | Người dùng phụ trách phần này. |
| Đích GitHub | Chỉ dẫn bàn giao, mục 22 | Kho công khai mới và nhánh đích được ghi trong bảng kiểm bàn giao. |

[Bản gốc, tên tệp tại máy và mã SHA-256](../references/README.md)
