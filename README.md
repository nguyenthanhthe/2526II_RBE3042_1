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
│   └── platformio.ini         # Cấu hình PlatformIO
├── data/                      # Dữ liệu thực nghiệm CSV
│   ├── dynamic/               # Dữ liệu động
│   └── static/                # Dữ liệu tĩnh
├── docs/                      # Tài liệu hướng dẫn & Tham khảo
│   ├── lab/                   # Hướng dẫn thực hành (Markdown)
│   │   ├── BÀI_THỰC_HÀNH_CẢM_BIẾN_ÁP_SUẤT.md
│   │   └── lab_instruction_1.md
│   └── references/            # Datasheets của BMP280
├── figures/                   # Hình ảnh & Đồ thị báo cáo
└── reports/                   # Các báo cáo tuần (Markdown)
    ├── report_1.md            # Báo cáo tuần 1: Lọc Kalman 1D trên ESP32-C3
    ├── report_2.md            # Báo cáo tuần 2: Đặc tính tĩnh, Oversampling & IIR
    ├── report_3.md            # Báo cáo tuần 3: Bộ lọc EMA
    ├── report_4.md            # Báo cáo tuần 4: Khảo sát ảnh hưởng nhiệt độ
    └── report_5.md            # Báo cáo tuần 5: So sánh Kalman & EMA
```

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
