---
layout: home
title: Trang chủ
nav_order: 1
permalink: /
---

# 🔬 Cảm biến & Đo lường — BMP280

**Môn học:** RBE3042 — Cảm biến và Đo lường cho Robot  
**Trường:** Đại học Công nghệ — ĐHQGHN (VNU-UET)  
**Nhóm:** K69E-RE1

---

## Giới thiệu

Dự án này tập trung **khảo sát, số hóa và phân tích chuyên sâu** cảm biến áp suất khí quyển **BMP280** — cảm biến MEMS áp điện trở thế hệ mới của Bosch Sensortec, kết hợp với bộ lọc số (EMA & Kalman 1D) trên vi điều khiển **ESP32-C3**.

---

## 📚 Bài giảng số hóa

| # | Tên bài giảng | Mô tả |
|---|---|---|
| 1 | [EP10 Pressure](docs/lectures/EP10 Pressure) | Cảm biến áp suất — Nguyên lý & BMP280 |
| 2 | [EP2 Measurement Systems](docs/lectures/EP2 Measurement Systems) | Hệ thống đo lường tổng quan |
| 3 | [EP3 Errors](docs/lectures/EP3 Errors during the measurement process) | Sai số trong quá trình đo lường |
| 4 | [EP4 Variable Conversion](docs/lectures/EP4 Variable conversion elements) | Phần tử biến đổi đại lượng |
| 5 | [EP5 Circuits for Sensors](docs/lectures/EP5 Circuits for Sensors) | Mạch điện cho cảm biến |
| 6 | [EP5b Interface Circuits](docs/lectures/EP5b Interface Electronic Circuits) | Mạch giao tiếp điện tử |
| 7 | [Chương 4](docs/lectures/Chương 4) | Cảm biến — Phân loại & Đặc tính |
| 8 | [Chapter 5.2 ADC & Filter](docs/lectures/Chappter 5.2 ADC-Sampling and Filter) | ADC, Lấy mẫu & Bộ lọc số |
| 9 | [AD620](docs/lectures/AD620) | IC Khuếch đại đo lường AD620 |
| 10 | [Đề cương ôn tập](docs/lectures/de-cuong-on-tap-ky-thuat-do-luong-va-cam-bien-k62-uet-450) | Đề cương ôn tập K62-UET |

---

## 📝 Ngân hàng câu hỏi BMP280

> **25+ câu hỏi** từ tổng quát đến chuyên sâu cho kỳ thi vấn đáp cuối kỳ.

[👉 Xem ngân hàng câu hỏi](docs/exam/ngan_hang_cau_hoi_bmp280){: .btn .btn-blue }

---

## ⚙️ Phần cứng & Kết nối

| BMP280 | ESP32-C3 | Chức năng |
|---|---|---|
| VCC | 3.3V | Nguồn |
| GND | GND | Đất |
| SCL | GPIO7 | I2C Clock |
| SDA | GPIO6 | I2C Data |

---

## 🔗 Liên kết nhanh

- 📦 [GitHub Repository](https://github.com/nguyenthanhthe/2526II_RBE3042_1)
- 📄 [Datasheet BMP280](docs/references/)
- 💻 [Mã nguồn ESP32-C3](https://github.com/nguyenthanhthe/2526II_RBE3042_1/tree/master/code)
