# 2526II_RBE3042_1 — Cảm biến và Đo lường

Dự án thực hành và nghiên cứu môn học **Cảm biến và Đo lường** (Mã HP: RBE3042) — Khoa Điện tử - Viễn thông, Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội.

## Thành viên thực hiện
1. **Nguyễn Thanh Thế** - MSSV: 24022911 (Lớp K69E-RE1)
2. **Phạm Quốc Hưng** - MSSV: 24022877 (Lớp K69E-RE1)
3. **Trần Thanh Tùng** - MSSV: 24022927 (Lớp K69E-RE1)

---

## Giới thiệu môn học & Dự án
Học phần **Cảm biến và Đo lường** cung cấp các kiến thức cốt lõi về nguyên lý hoạt động, đặc tính kỹ thuật và phương pháp xử lý tín hiệu từ các loại cảm biến khác nhau. 

Dự án này tập trung khảo sát cảm biến áp suất khí quyển/độ cao **BMP280** (sử dụng cấu trúc MEMS áp điện trở) kết hợp với các bộ lọc số (Exponential Moving Average - EMA và Kalman Filter 1D) trên vi điều khiển **ESP32-C3** để thu thập dữ liệu độ cao chính xác và làm mịn nhiễu đo lường trong các ứng dụng thực tế (như thiết bị bay UAV, Robot di động).

---

## Cấu hình phần cứng & Sơ đồ kết nối
Hệ thống sử dụng vi điều khiển **ESP32-C3** kết nối với cảm biến **BMP280** qua giao tiếp I2C:

| BMP280 Pin | ESP32-C3 Pin | Chức năng |
|---|---|---|
| **VCC** | **3.3V** | Cấp nguồn |
| **GND** | **GND** | Nối đất |
| **SCL** | **GPIO7** | Xung nhịp I2C |
| **SDA** | **GPIO6** | Dữ liệu I2C |

---

## Cấu trúc thư mục Workspace
Workspace được tổ chức khoa học theo cấu trúc sau:
```text
2526II_RBE3042_1/
├── code/                      # Mã nguồn phần mềm
│   ├── EMA_Filter/            # Bộ lọc EMA (Exponential Moving Average)
│   │   └── EMA_Filter.ino
│   ├── Kalman_Filter/         # Bộ lọc Kalman 1 chiều (1D Kalman Filter)
│   │   └── Kalman_Filter.ino
│   ├── digitize_lectures.py   # Script số hóa slide bài giảng
│   └── platformio.ini         # Cấu hình PlatformIO
├── data/                      # Dữ liệu thực nghiệm CSV
│   ├── dynamic/               # Dữ liệu động
│   └── static/                # Dữ liệu tĩnh
├── docs/                      # Tài liệu hướng dẫn, Bài giảng & Ôn thi
│   ├── exam/                  # Ngân hàng câu hỏi ôn tập vấn đáp
│   │   └── ngan_hang_cau_hoi_bmp280.md
│   ├── lab/                   # Hướng dẫn thực hành (Markdown)
│   │   ├── BÀI_THỰC_HÀNH_CẢM_BIẾN_ÁP_SUẤT.md
│   │   └── lab_instruction_1.md
│   ├── lectures/              # Bài giảng & Slide môn học đã số hóa (.md)
│   │   ├── Chappter 5.2 ADC-Sampling and Filter.md
│   │   ├── EP10 Pressure.md
│   │   └── ... (10 tệp bài giảng chương/tuần)
│   └── references/            # Giáo trình & Datasheets (Mục lục & Tóm tắt)
│       ├── Handbook of modern sensors...md
│       ├── BST-BMP280-DS001-11.pdf (Datasheet gốc)
│       └── Lock-in ...Measurement and Instrumentation Principles...md
├── figures/                   # Hình ảnh & Đồ thị báo cáo
│   ├── exam/                  # Sơ đồ minh họa cho ngân hàng câu hỏi
│   ├── lectures/              # Hình ảnh trích xuất từ slide bài giảng
│   └── ...
├── reports/                   # Các báo cáo tuần (Markdown)
│   ├── report_1.md            # Báo cáo tuần 1: Lọc Kalman 1D trên ESP32-C3
│   ├── report_2.md            # Báo cáo tuần 2: Đặc tính tĩnh, Oversampling & IIR
│   ├── report_3.md            # Báo cáo tuần 3: Bộ lọc EMA
│   ├── report_4.md            # Báo cáo tuần 4: Khảo sát ảnh hưởng nhiệt độ
│   └── report_5.md            # Báo cáo tuần 5: So sánh Kalman & EMA
├── slides/                    # Slide báo cáo thuyết trình
│   └── presentation.html      # Trang slide báo cáo HTML
├── PROJECT.md                 # Kế hoạch và thông tin dự án
└── README.md                  # Hướng dẫn và giới thiệu tổng quan
```

---

## 📚 Ngân hàng Câu hỏi Ôn thi Vấn đáp Cuối kỳ
Tập tài liệu ngân hàng câu hỏi chi tiết phục vụ thi vấn đáp cuối kỳ môn học:
* [Ngân hàng Câu hỏi Ôn tập Vấn đáp BMP280](./docs/exam/ngan_hang_cau_hoi_bmp280.md) — Bao gồm **25 câu hỏi tự luận/vấn đáp** từ nguyên lý màng bán dẫn MEMS, mạch cầu đo Wheatstone, mạch khuếch đại vi sai AD620, cấu hình lấy mẫu Nyquist-Shannon cho tới thiết kế & cài đặt code C bộ lọc số (FIR, IIR Butterworth, EMA, Kalman 1D).

---

## 📖 Bài giảng & Slide Môn học (Số hóa sang Markdown - Tập trung vào BMP280)
Toàn bộ slide bài giảng liên quan trực tiếp đến cảm biến áp suất, mạch cầu đo, mạch xử lý tín hiệu và các bộ lọc số đã được trích xuất nội dung văn bản và hình ảnh tương ứng sang định dạng Markdown:
* **Áp suất & Cảm biến áp suất:** [EP10 Pressure](./docs/lectures/EP10%20Pressure.md)
* **Lấy mẫu & Bộ lọc số:** [Chappter 5.2 ADC-Sampling and Filter](./docs/lectures/Chappter%205.2%20ADC-Sampling%20and%20Filter.md)
* **Mạch đo cảm biến & Phần tử chuyển đổi:** [EP5 Circuits for Sensors](./docs/lectures/EP5%20Circuits%20for%20Sensors.md), [EP5b Interface Electronic Circuits](./docs/lectures/EP5b%20Interface%20Electronic%20Circuits.md) & [EP4 Variable conversion elements](./docs/lectures/EP4%20Variable%20conversion%20elements.md)
* **Mạch tiền xử lý tín hiệu:** [Chương 4: Mạch đo lường và xử lý tín hiệu lối ra cảm biến](./docs/lectures/Chương%204.md) & Khuếch đại đo lường [AD620](./docs/lectures/AD620.md)
* **Lý thuyết đo lường & Sai số:** [EP3 Errors during the measurement process](./docs/lectures/EP3%20Errors%20during%20the%20measurement%20process.md) & [EP2 Measurement Systems](./docs/lectures/EP2%20Measurement%20Systems.md)
* **Đề cương ôn tập khoa học:** [Đề cương ôn tập kỹ thuật đo lường và cảm biến](./docs/lectures/de-cuong-on-tap-ky-thuat-do-luong-va-cam-bien-k62-uet-450.md)
* [Xem toàn bộ 10 tệp bài giảng số hóa tại đây](./docs/lectures/)

---

## Tài liệu Hướng dẫn Thực hành (Lab Instructions)
Các bài hướng dẫn thực hành đã được số hóa và chuyển đổi hoàn toàn sang định dạng Markdown để tiện tra cứu trực tuyến:
* [BÀI THỰC HÀNH CẢM BIẾN ÁP SUẤT](./docs/lab/BÀI_THỰC_HÀNH_CẢM_BIẾN_ÁP_SUẤT.md)
* [LAB 01: CẢM BIẾN ÁP SUẤT - HƯỚNG DẪN CHI TIẾT](./docs/lab/lab_instruction_1.md)

---

## Danh sách Báo cáo Tuần (Weekly Reports)
Xem chi tiết kết quả thực nghiệm và phân tích số liệu qua các báo cáo tuần:
1. **Tuần 1:** [Thiết lập và Khảo sát Bộ lọc Kalman 1 chiều trên ESP32-C3](./reports/report_1.md)
2. **Tuần 2:** [Khảo sát Đặc tính Tĩnh, Oversampling và Bộ lọc IIR nội bộ của BMP280](./reports/report_2.md)
3. **Tuần 3:** [Thiết kế và Triển khai Bộ lọc EMA (Exponential Moving Average)](./reports/report_3.md)
4. **Tuần 4:** [Khảo sát Ảnh hưởng của Nhiệt độ đến phép đo Áp suất và Độ cao](./reports/report_4.md)
5. **Tuần 5:** [So sánh, Đánh giá Hiệu năng giữa bộ lọc Kalman và bộ lọc EMA](./reports/report_5.md)

---

## Hướng dẫn Biên dịch Code (PlatformIO)
Để biên dịch mã nguồn của dự án bằng PlatformIO:
1. Di chuyển vào thư mục `code/`.
2. Chạy lệnh:
   * Biên dịch cho board ESP32-C3 DevKit:
     ```bash
     pio run -e esp32-c3-dev
     ```
   * Biên dịch cho board ESP32-C3 Super Mini:
     ```bash
     pio run -e esp32-c3-super-mini
     ```
