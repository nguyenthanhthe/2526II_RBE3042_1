# BMP280 + Kalman/EMA Filter Survey

**Bài thực hành:** Khảo sát đặc tính cảm biến áp suất/độ cao GY-BMP280 và ứng dụng bộ lọc Kalman & EMA trên ESP32-C3 Super Mini.

## Authors
- Nguyễn Thanh Thế
- Phạm Quốc Hưng
- Trần Thanh Tùng

## Mục tiêu thí nghiệm
Theo file hướng dẫn `docs/lab/BAI_THUC_HANH_CAM_BIEN_AP_SUAT.docx`:
1. Đánh giá đặc tính đo lường cơ bản của BMP280: **tĩnh** và **động**.
2. Thu thập dữ liệu qua I2C trên vi điều khiển.
3. So sánh dữ liệu thô và dữ liệu sau lọc Kalman / EMA.
4. Trực quan hóa và phân tích dữ liệu thực nghiệm.

## Cấu trúc repo

```text
bmp280-kalman-survey/
├── .gitignore
├── platformio.ini                  # PlatformIO project config
├── README.md
├── data/
│   ├── dynamic/                    # Dữ liệu đặc tính động
│   │   ├── 0,1.csv                #   RAW - alpha=0.1 (lọc mạnh)
│   │   ├── 0,1_kalman.csv         #   Kalman - alpha=0.1
│   │   ├── 0,3.csv                #   RAW - alpha=0.3 (cân bằng)
│   │   ├── 0,3_kalman.csv         #   Kalman - alpha=0.3
│   │   ├── 0,7.csv                #   RAW - alpha=0.7 (lọc yếu)
│   │   └── 0,7_kalman.csv         #   Kalman - alpha=0.7
│   └── static/                     # Dữ liệu đặc tính tĩnh (trống)
├── docs/
│   ├── lab/                        # Hướng dẫn thí nghiệm
│   │   ├── BAI_THUC_HANH_CAM_BIEN_AP_SUAT.docx
│   │   └── lab_instruction_1.pdf
│   └── references/                 # Datasheet & tài liệu tham khảo
│       └── BST-BMP280-DS001-11.pdf
├── EMA_Filter/
│   └── EMA_Filter.ino             # Firmware lọc EMA (Exponential Moving Average)
├── figures/
│   ├── comparision table (2).png  # Bảng so sánh bộ lọc
│   ├── comparision table.png
│   ├── Figure_1.png               # Biểu đồ khảo sát
│   ├── survey_report.png          # Báo cáo khảo sát
│   └── survey_report_v2.png
└── Kalman_Filter/
    └── Kalman_Filter.ino          # Firmware lọc Kalman
```

## Phần cứng
- **Vi điều khiển:** ESP32-C3 Super Mini
- **Cảm biến:** GY-BMP280 (I2C)
- **Kết nối:** I2C (SDA / SCL)

## Nội dung thí nghiệm

### 1) Khảo sát đặc tính tĩnh
Mục đích:
- Đánh giá **độ ổn định** của cảm biến ở độ cao cố định.
- Đánh giá **độ tuyến tính** khi thay đổi độ cao.

Quy trình:
- Lấy mốc mặt đất.
- Di chuyển cảm biến lên các mức cao khác nhau.
- Giữ yên tại mỗi vị trí trong khoảng thời gian cố định.
- Đo chiều cao thực bằng thước để làm giá trị chuẩn.
- Lưu dữ liệu độ cao theo thời gian.

Dữ liệu thô và xử lý lưu tại `data/static/`.

### 2) Khảo sát đặc tính động (với EMA filter)
Mục đích:
- Đánh giá đáp ứng khi độ cao thay đổi nhanh.
- Quan sát ảnh hưởng của bộ lọc Kalman và EMA lên tín hiệu.
- So sánh chất lượng lọc với các hệ số α khác nhau (0.1, 0.3, 0.7).

Dữ liệu động lưu tại `data/dynamic/` với định dạng:
- `{alpha}.csv` — dữ liệu RAW
- `{alpha}_kalman.csv` — dữ liệu sau lọc Kalman

## Firmware
- **ESP32-C3** — PlatformIO project
- `EMA_Filter/EMA_Filter.ino` — đo + lọc EMA, ghi log qua Serial
- `Kalman_Filter/Kalman_Filter.ino` — đo + lọc Kalman, ghi log qua Serial

## Cách chạy

### 1) Nạp firmware
```bash
# Mở folder trong PlatformIO (VS Code)
# Chọn đúng board: ESP32-C3 Super Mini
pio run --target upload --environment esp32-c3-devkitm-1
```

### 2) Ghi dữ liệu từ Serial
```bash
pio device monitor --port COM9 --baud 115200 > data/dynamic/0,3.csv
```

### 3) Import vào Excel / MATLAB để phân tích và vẽ biểu đồ

## Hình ảnh kết quả
Xem trong thư mục `figures/`:

| Hình ảnh | Mô tả |
|---|---|
| `Figure_1.png` | Biểu đồ khảo sát chính |
| `survey_report.png` | Báo cáo kết quả khảo sát |
| `comparision table.png` | Bảng so sánh các bộ lọc |

## Tài liệu tham khảo
- Hướng dẫn bài thực hành: `docs/lab/BAI_THUC_HANH_CAM_BIEN_AP_SUAT.docx`
- Lab instruction (PDF): `docs/lab/lab_instruction_1.pdf`
- Datasheet BMP280: `docs/references/BST-BMP280-DS001-11.pdf`

## Ghi chú
- Dữ liệu động được thu thập với 3 mức lọc EMA: α = 0.1 (lọc mạnh), 0.3 (cân bằng), 0.7 (lọc yếu), kèm lọc Kalman song song.
- Dữ liệu tĩnh chưa được cập nhật.
