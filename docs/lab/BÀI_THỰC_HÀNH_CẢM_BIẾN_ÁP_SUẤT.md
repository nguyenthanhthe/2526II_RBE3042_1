# BÀI THỰC HÀNH: KHẢO SÁT ĐẶC TÍNH CẢM BIẾN ÁP SUẤT GY-BMP280 VÀ ỨNG DỤNG BỘ LỌC KALMAN

### I. Mục đích thí nghiệm
* Hiểu và đánh giá được các đặc tính đo lường cơ bản (Tĩnh và Động) của cảm biến áp suất/độ cao GY-BMP280.
* Thực hành lập trình thu thập dữ liệu qua chuẩn giao tiếp I2C trên vi điều khiển Arduino.
* Thiết kế và triển khai thuật toán lọc Kalman trên vi điều khiển để giảm nhiễu tín hiệu.
* Trực quan hóa, phân tích và so sánh dữ liệu thực nghiệm bằng các phần mềm chuyên dụng.

---

### II. Thiết bị và Dụng cụ
* Vi điều khiển: Arduino Uno hoặc Arduino Mega 2560.
* Cảm biến: Module GY-BMP280.
* Dây cắm (Jumper wires) và Breadboard.
* Thước dây (để đo chiều cao thực tế của các bậc thang).
* Máy tính cá nhân có cài đặt Arduino IDE.

---

### III. Cơ sở lý thuyết cần chuẩn bị
Sinh viên cần ôn tập lại:
* Phương trình quy đổi từ áp suất khí quyển sang độ cao tương đối:
  $$h = 44330 \times \left[1 - \left(\frac{p}{p_0}\right)^{\frac{1}{5.255}}\right]$$
  *(Trong đó $p$ là áp suất đo được, $p_0$ là áp suất tại mực nước biển hoặc điểm mốc).*
* Nguyên lý cơ bản của bộ lọc Kalman 1 chiều (1D Kalman Filter).

---

### IV. Trình tự Thí nghiệm

#### Phần 1: Khởi tạo Hệ thống và Lập trình cơ sở
1. **Kết nối phần cứng:** Giao tiếp GY-BMP280 với Arduino qua I2C.
2. **Yêu cầu Lập trình (Sinh viên tự thực hiện):**
   * Viết chương trình đọc giá trị độ cao thô từ cảm biến với tần số lấy mẫu $f_s$ ít nhất là 20Hz.
   * Cài đặt thuật toán lọc Kalman 1D vào chương trình. Chương trình cần xuất ra cổng Serial đồng thời 2 giá trị: `[Độ cao Raw, Độ cao Kalman]`.
   * Ghi dữ liệu từ Serial Monitor vào file text/csv để xử lý sau.

#### Phần 2: Khảo sát Đặc tính Tĩnh
Khảo sát khả năng đo lường ổn định và độ tuyến tính của cảm biến.
* **Tiến hành đo lường:**
  1. Cố định Arduino và cảm biến lên một mặt phẳng ổn định.
  2. Thực hiện đo độ cao tại mặt đất làm mốc tham chiếu.
  3. Di chuyển hệ thống đo lên từng bậc thang. Tại mỗi vị trí, giữ yên cảm biến trong vòng 10 giây để thu thập một chuỗi dữ liệu ổn định *(Khuyến khích đo tại nhiều độ cao khác nhau)*.
  4. Đo khoảng cách thực tế (bằng thước dây) giữa các bậc/tầng để làm giá trị chuẩn.
* **Dữ liệu cần lưu:** Tập dữ liệu tĩnh gồm các tín hiệu độ cao theo thời gian.

#### Phần 3: Khảo sát Đặc tính Động
Khảo sát tốc độ đáp ứng của cảm biến và sự ảnh hưởng của bộ lọc khi môi trường thay đổi đột ngột.
* **Tiến hành đo lường:**
  1. Cầm hệ thống trên tay, bắt đầu ở trạng thái đứng yên tại một độ cao cố định trong 5 giây.
  2. Di chuyển cảm biến lên cao (hoặc hạ xuống thấp) với tốc độ nhanh nhất có thể (ví dụ: giơ thẳng tay lên cao) và giữ yên trong 5 giây tiếp theo.
  3. Lặp lại động tác nâng/hạ đột ngột này 3-5 lần để tạo ra các xung bước.
* **Dữ liệu cần lưu:** Tập dữ liệu động có sự biến thiên liên tục và biên độ lớn.

---

### V. Yêu cầu Báo cáo & Đánh giá
Sinh viên sử dụng các phần mềm phân tích dữ liệu (như Excel, MATLAB, hoặc OriginLab) để vẽ đồ thị và thực hiện các yêu cầu sau:

#### 1. Phân tích Đặc tính Tĩnh:
* **Vẽ đồ thị:** Trục $x$ là vị trí các bậc thang, trục $y$ là giá trị độ cao đo được (trung bình của khoảng thời gian giữ yên). Trình bày đường hồi quy tuyến tính.
* **Tính toán thông số:**
  * **Range:** Chênh lệch độ cao tối đa đo được ở các bậc thang.
  * **Resolution:** Phân tích tín hiệu thô tại 2 bậc thang liền kề. Cảm biến có phân biệt rõ ràng được sự thay đổi của 1 bậc thang hay không?
  * **Error:** Tính toán sai số tuyệt đối và tương đối giữa giá trị độ cao từ cảm biến và giá trị đo bằng thước dây thực tế.

#### 2. Phân tích Đặc tính Động & Bộ lọc Kalman:
* **Vẽ đồ thị:** Đồ thị theo thời gian gồm 2 đường tín hiệu: Dữ liệu thô và Dữ liệu sau lọc.
* **Đánh giá bộ lọc:**
  * Quan sát biểu đồ để xác định thời gian đáp ứng của cảm biến thô khi thay đổi độ cao đột ngột.
  * **Tính toán độ trễ:** Đo khoảng thời gian chênh lệch giữa đỉnh của tín hiệu thô và đỉnh của tín hiệu đã qua lọc.
