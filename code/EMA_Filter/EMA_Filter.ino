#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

#define I2C_SDA 6
#define I2C_SCL 7

Adafruit_BMP280 bmp;

// --- CẤU HÌNH BỘ LỌC EMA ---
// THAY ĐỔI GIÁ TRỊ ALPHA Ở ĐÂY CHO MỖI LẦN ĐO (0.1 / 0.3 / 0.7)
float alpha = 0.3;  // Hệ số lọc EMA (0.0 < alpha <= 1.0)
float y_prev = 0.0; // Giá trị lọc trước đó

// --- CẤU HÌNH ĐO LƯỜNG ---
const int SAMPLE_RATE_HZ = 20; // 20Hz (50ms/mẫu)
const int DURATION_SEC = 20;   // Tổng 20 giây
const int NUM_SAMPLES = SAMPLE_RATE_HZ * DURATION_SEC; 

// --- MẢNG LƯU TRỮ TRONG RAM ---
unsigned long time_arr[NUM_SAMPLES];
float raw_arr[NUM_SAMPLES];
float ema_arr[NUM_SAMPLES];

bool first_read = true;
bool cleanup_printed = false;

const float SEALEVELPRESSURE_HPA = 1013.25;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(100);

  Wire.begin(I2C_SDA, I2C_SCL);

  if (!bmp.begin(0x76)) {
    Serial.println("Khong tim thay BMP280! Kiem tra day noi.");
    while (1) delay(10);
  }

  // Tắt bộ lọc IIR nội bộ để cấp dữ liệu thô
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,
                  Adafruit_BMP280::SAMPLING_X2,
                  Adafruit_BMP280::SAMPLING_X16,
                  Adafruit_BMP280::FILTER_OFF,
                  Adafruit_BMP280::STANDBY_MS_1);

  Serial.println("======================================");
  Serial.println("CHUAN BI TU THE (Giu tay on dinh)...");
  Serial.println("Mat 3 giay de bat dau lay mau...");
  delay(3000); 

  Serial.println("DANG DO... (Hay giu yen tay)");

  unsigned long start_time = millis();
  
  for (int i = 0; i < NUM_SAMPLES; i++) {
    unsigned long loop_start = millis();
    unsigned long current_time = loop_start - start_time;
    
    // 1. Lấy dữ liệu thô
    float z = bmp.readAltitude(SEALEVELPRESSURE_HPA);

    // 2. Thuật toán EMA: y[n] = alpha * x[n] + (1 - alpha) * y[n-1]
    if (first_read) {
      y_prev = z;
      first_read = false;
    } else {
      y_prev = alpha * z + (1.0 - alpha) * y_prev;
    }

    // 3. Lưu vào mảng
    time_arr[i] = current_time;
    raw_arr[i] = z;
    ema_arr[i] = y_prev;

    // ----- LOGIC BÁO HIỆU QUA SERIAL MONITOR -----
    // Từ giây thứ 8 đến giây thứ 9, in thông báo liên tục
    if (current_time >= 8000 && current_time <= 9000) {
        Serial.print("[CHUYEN MUC NGAY !] - Time: ");
        Serial.print(current_time);
        Serial.println(" ms");
    } 
    // Dọn dẹp log sau giây thứ 9
    else if (current_time > 9000 && !cleanup_printed) {
        Serial.println("...");
        Serial.println("(Da xong buoc chuyen, tiep tuc giu yen tay cho den het 20s)");
        Serial.println("...");
        cleanup_printed = true;
    }
    // ---------------------------------------------

    // Timer bù trừ độ trễ, đảm bảo đúng 50ms mỗi vòng lặp
    unsigned long elapsed = millis() - loop_start;
    unsigned long period = 1000 / SAMPLE_RATE_HZ;
    if (elapsed < period) {
      delay(period - elapsed);
    }
  }

  // --- KẾT THÚC ĐO LƯỜNG & IN DỮ LIỆU CSV ---
  Serial.println("======================================");
  Serial.println("HOAN THANH! COPY DU LIEU BEN DUOI VA LUU THANH FILE .CSV:");
  Serial.println("Time(ms),Raw_Altitude(m),EMA_Altitude(m)");
  
  for (int i = 0; i < NUM_SAMPLES; i++) {
    Serial.print(time_arr[i]);
    Serial.print(",");
    Serial.print(raw_arr[i], 4);
    Serial.print(",");
    Serial.println(ema_arr[i], 4);
  }
}

void loop() {
  // Không thực thi gì thêm ở loop
}
