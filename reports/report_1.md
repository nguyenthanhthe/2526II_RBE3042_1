# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ
# ĐẠI HỌC QUỐC GIA HÀ NỘI

![VNU Logo](../figures/vnu_logo.jpg)
![Cover Graphic](../figures/cover_graphic.png)

# BÁO CÁO THỰC HÀNH MÔN HỌC: CẢM BIẾN VÀ ĐO LƯỜNG
## THIẾT KẾ VÀ ĐÁNH GIÁ BỘ LỌC KALMAN 1 CHIỀU TRÊN ESP32-C3 VỚI CẢM BIẾN BMP280

**Giảng viên hướng dẫn:** Trần Khánh Duy, Nguyễn Kiên
**Nhóm sinh viên thực hiện:**
- Nguyễn Thanh Thế (MSSV: 24022911, Lớp: K69E-RE1)
- Trần Thanh Tùng (MSSV: 24022927, Lớp: K69E-RE1)
- Phạm Quốc Hưng (MSSV: 24022877, Lớp: K69E-RE1)

---

### I. MỤC ĐÍCH THÍ NGHIỆM
- Tìm hiểu lý thuyết và cách thức hoạt động của bộ lọc Kalman 1 chiều (1D Kalman Filter).
- Triển khai thuật toán lọc Kalman trực tiếp trên hệ thống nhúng sử dụng vi điều khiển **ESP32-C3** và cảm biến áp suất/độ cao **BMP280**.
- Đánh giá chất lượng lọc thông qua việc thay đổi thông số nhiễu quá trình $Q$ (với các giá trị khảo sát là 0.011, 0.128, và 1.633) khi cảm biến chuyển đổi trạng thái độ cao.

---

### II. THIẾT BỊ VÀ DỤNG CỤ
1. **Vi điều khiển:** ESP32-C3 (DevKit hoặc Super Mini) hỗ trợ kết nối I2C và truyền thông Serial.
2. **Cảm biến:** Cảm biến áp suất khí quyển và độ cao GY-BMP280.
3. **Phần mềm:** PlatformIO / Arduino IDE, thư viện `Adafruit_BMP280` và `Adafruit_Sensor`.
4. **Phụ kiện:** Breadboard, dây cắm.

---

### III. SƠ ĐỒ KẾT NỐI
Kết nối giữa ESP32-C3 và cảm biến BMP280 thông qua giao tiếp I2C:

| Chân trên BMP280 | Chân trên ESP32-C3 | Chức năng |
|---|---|---|
| **VCC** | **3.3V** | Cấp nguồn 3.3V |
| **GND** | **GND** | Nối đất |
| **SCL** | **GPIO7** | Chân xung nhịp I2C (SCL) |
| **SDA** | **GPIO6** | Chân dữ liệu I2C (SDA) |

*Lưu ý:* Cấu hình phần cứng tắt bộ lọc IIR nội bộ của BMP280 (`FILTER_OFF`) nhằm thu thập dữ liệu thô (Raw Altitude) phục vụ cho việc đánh giá bộ lọc Kalman độc lập.

---

### IV. THUẬT TOÁN LỌC KALMAN 1 CHIỀU ĐÃ TRIỂN KHAI
Thuật toán lọc Kalman 1 chiều được hiện thực hóa qua hai bước chính trong mỗi chu kỳ lấy mẫu:

#### 1. Bước dự báo (Prediction)
* Dự báo trạng thái tiếp theo (độ cao dự kiến giữ nguyên do không có mô hình động lực học phức tạp):
  $$x_{pred} = x_{est}$$
* Dự báo hiệp phương sai sai số (tăng lên do nhiễu quá trình $Q$):
  $$p_{pred} = p_{est} + Q$$

#### 2. Bước cập nhật (Update)
* Tính toán hệ số tăng Kalman (Kalman Gain $K$):
  $$K = \frac{p_{pred}}{p_{pred} + R}$$
* Cập nhật ước lượng trạng thái mới dựa trên giá trị đo thực tế $z$ thu được từ BMP280:
  $$x_{est} = x_{est} + K \cdot (z - x_{est})$$
* Cập nhật hiệp phương sai sai số phục vụ chu kỳ tiếp theo:
  $$p_{est} = (1 - K) \cdot p_{pred}$$

---

### V. CẤU HÌNH THÍ NGHIỆM & QUY TRÌNH THU THẬP
* **Tần số lấy mẫu:** 20Hz (khoảng cách 50ms giữa các mẫu đo, được căn chỉnh chính xác nhờ vòng lặp bù trễ thời gian thực).
* **Tổng thời gian khảo sát:** 20 giây (tương đương 400 mẫu dữ liệu).
* **Kịch bản đo đạc:**
  * **0s đến 8s:** Giữ nguyên cảm biến áp suất cố định trên mặt bàn phẳng để xác định trạng thái tĩnh ổn định ban đầu.
  * **8s đến 9s:** Di chuyển nâng/hạ cảm biến nhanh chóng sang một bậc độ cao mới. Hệ thống sẽ phát tín hiệu báo động `[CHUYEN MUC NGAY !]` qua Serial Monitor để đánh dấu thời gian chuyển trạng thái.
  * **9s đến 20s:** Giữ cố định cảm biến ở vị trí mới nhằm theo dõi khả năng xác lập lại trạng thái ổn định và triệt tiêu nhiễu của bộ lọc.
* **Cấu hình tham số lọc:**
  * Nhiễu đo lường cố định: $R = 1.0$
  * Khảo sát 3 kịch bản nhiễu quá trình: $Q \in \{0.011, 0.128, 1.633\}$

---

### VI. KẾT QUẢ VÀ NHẬN XÉT
1. **Với $Q = 0.011$ (Nhiễu quá trình rất nhỏ):**
   * Bộ lọc cho đường đặc tính cực kỳ mượt mà, triệt tiêu hoàn toàn nhiễu dao động răng cưa của cảm biến BMP280.
   * *Nhược điểm:* Phản ứng rất chậm khi thay đổi độ cao (trễ pha nặng). Khi cảm biến đã di chuyển đến vị trí mới, bộ lọc cần nhiều giây mới đuổi kịp giá trị thực.
2. **Với $Q = 1.633$ (Nhiễu quá trình lớn):**
   * Bộ lọc bám rất sát và phản ứng ngay lập tức với chuyển động nâng/hạ cảm biến.
   * *Nhược điểm:* Khả năng lọc nhiễu kém, đường đồ thị lọc Kalman vẫn còn dao động lớn gần như đường dữ liệu thô.
3. **Với $Q = 0.128$ (Giá trị tối ưu trung gian):**
   * Đạt được sự cân bằng tối ưu giữa tốc độ đáp ứng chuyển động và khả năng làm mịn nhiễu tĩnh.
