## Authors
- Nguyễn Thanh Thế
- Phạm Quốc Hưng
- Trần Thanh Tùng


## Cấu trúc repo

```text
bmp280-kalman-survey/
├── .gitignore
├── platformio.ini                  # PlatformIO project config (ESP32-C3)
├── README.md
├── EMA_Filter/
│   └── EMA_Filter.ino             # Firmware lọc EMA (Exponential Moving Average)
├── Kalman_Filter/
│   └── Kalman_Filter.ino          # Firmware lọc Kalman
├── data/
│   ├── dynamic/                    # Dữ liệu đặc tính động
│   │   ├── 0,1.csv                #   RAW - α = 0.1 (lọc mạnh)
│   │   ├── 0,1_kalman.csv         #   Kalman - α = 0.1
│   │   ├── 0,3.csv                #   RAW - α = 0.3 (cân bằng)
│   │   ├── 0,3_kalman.csv         #   Kalman - α = 0.3
│   │   ├── 0,7.csv                #   RAW - α = 0.7 (lọc yếu)
│   │   └── 0,7_kalman.csv         #   Kalman - α = 0.7
│   └── static/                     # Dữ liệu đặc tính tĩnh (trống)
├── docs/
│   ├── lab/                        # Hướng dẫn thí nghiệm
│   │   └── BAI_THUC_HANH_CAM_BIEN_AP_SUAT.docx
│   └── references/                 # Datasheet & tài liệu tham khảo
│       └── BST-BMP280-DS001-11.pdf
└── figures/                        # Hình ảnh kết quả
    ├── comparision table (2).png
    ├── comparision table.png
    ├── Figure_1.png
    ├── survey_report.png
    └── survey_report_v2.png
```

## Phần cứng
- **Vi điều khiển:** ESP32-C3 Super Mini
- **Cảm biến:** GY-BMP280 (I2C)
- **Kết nối:** I2C (SDA / SCL)

