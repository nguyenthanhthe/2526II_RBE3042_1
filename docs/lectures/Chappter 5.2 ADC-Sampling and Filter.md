# Chappter 5.2 ADC-Sampling and Filter

> Tài liệu chuyển đổi từ PPTX: `Chappter 5.2 ADC-Sampling and Filter.pptx`

---

## Slide 1

- ADC- Sampling and Filter
- 1

![Slide 1](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_1.png)

---

## Slide 2

- ADC Sampling
- 2
- Measurement systems block diagram

![Slide 2](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_2_media_rId2.png)

---

## Slide 3

- ADC interface and sampling
- 3

![Slide 3](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_3_media_rId2.png)

---

## Slide 4

- Digital Filters for sensor
- 4
- FIR (Finite Impulse Response) bộ lọc số có đáp ứng xung hữu hạn:
- Fs = 1 / 2 (ms) = 500 Hz, Fc = 50 Hz (low-pass), cửa sổ lọc N=5
- Thiết kế low-pass FIR thực chiến cho sensor
- 𝑥(𝑡) : tín hiệu vào
- ℎ(𝑡) : đáp ứng xung (impulse response)𝑦(𝑡) : tín hiệu ra

![Slide 4](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_4.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_4_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_4_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_4_media_rId4.png)

---

## Slide 5

- 5
- sinc(x)=sin(πx)/πx​
- h[n]=2⋅0.1⋅sinc(0.2(n−2))
- Digital Filter for sensor
- h[n]=hideal​[n]⋅w[n]

![Slide 5](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_5.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_5_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_5_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_5_media_rId6.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_5_media_rId5.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_5_media_rId4.png)

---

## Slide 6

- Digital Filter for sensor
- 6

![Slide 6](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_6.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_6_media_rId2.png)

---

## Slide 7

- 7
- #define N 5
- float h[N] = {
- 0.0675,
- 0.2490,
- 0.3670,
- 0.2490,
- 0.0675
- };
- float buffer[N] = {0};
- int idx = 0;
- float FIR_LPF(float x)
- {
- buffer[idx] = x;
- float y = 0;
- int j = idx;
- for(int i = 0; i < N; i++)
- {
- y += h[i] * buffer[j];
- j--;
- if(j < 0) j = N - 1;
- }
- idx++;
- if(idx >= N) idx = 0;
- return y;
- }
- unsigned long last = 0;
- void loop()
- {
- if (micros() - last >= 2000) // 2 ms
- {
- last = micros();
- float input = analogRead(A0);
- float output = FIR_LPF(input);
- }
- }
- Fs = 1 / 2 (ms) = 500 Hz, Fc = 50 Hz (low-pass), cửa sổ lọc N=5
- Digital Filter for sensor

![Slide 7](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_7.png)

---

## Slide 8

- IIR Low pass filter-Bộ lọc đáp ứng xung vô hạn
- 8

![Slide 8](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_8.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_8_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_8_media_rId2.png)

---

## Slide 9

- 9
- float alpha = 0.385;
- float y_prev = 0;
- float IIR_LPF(float x)
- {
- float y = alpha * x + (1 - alpha) * y_prev;
- y_prev = y;
- return y;
- }
- IIR Low pass filter
- IIR Low pass filter bậc I

![Slide 9](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_9.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_9_media_rId2.png)

---

## Slide 10

- 10
- float b0 = 0.0675;
- float b1 = 0.1349;
- float b2 = 0.0675;
- float a1 = -1.1429;
- float a2 = 0.4128;
- float x1 = 0, x2 = 0;
- float y1 = 0, y2 = 0;
- float IIR_Butterworth(float x)
- {
- float y = b0*x + b1*x1 + b2*x2
- - a1*y1 - a2*y2;
- // shift state
- x2 = x1;
- x1 = x;
- y2 = y1;
- y1 = y;
- return y;
- }
- Butterworth 2nd order
- IIR Low pass filter

![Slide 10](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_10.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_10_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_10_media_rId2.png)

---

## Slide 11

- Kalman filter for sensor
- 11
- Group discussion

![Slide 11](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_11.png)

---

## Slide 12

- Sensors for mobile robot
- 12

![Slide 12](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_12.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_12_media_rId2.png)

---

## Slide 13

- Sensors for Robots- Mobile robot
- 13
- IMU sensor
- Motor: Encoder – Hall sensors
- Approximate sensor
- GPS
- Deep camera
- Line sensor
- Lidar sensor

![Slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId8.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId7.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId12.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId6.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId11.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId5.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId10.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId4.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_media_rId9.png)

---

## Slide 14

- ROS and Sensors
- 14

![Slide 14](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14_media_rId4.png)

---

## Slide 15

- ROS - Sensors
- 15

![Slide 15](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_15.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_15_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_15_media_rId2.png)

---

## Slide 16

- Laser scanner- LIDAR
- 16

![Slide 16](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16_media_rId4.png)

---

## Slide 17

- 17
- 2D Lidar
- 3D Lidar
- Laser scanner- LIDAR

![Slide 17](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_media_rId2.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_media_rId5.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_media_rId4.png)

---

## Slide 18

- BLDC MOTOR
- 18
- ROBOT Dynamic control

![Slide 18](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_media_rId3.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_media_rId5.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_media_rId4.png)

---

## Slide 19

- ROBOT-BLDC MOTOR
- 19
- BLDC MOTOR

![Slide 19](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_19.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_19_media_rId2.png)

---

## Slide 20

- 20
- ROBOT-BLDC MOTOR
- BLDC MOTOR

![Slide 20](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20_media_rId4.png)

---

## Slide 21

- Magnetic (Hall) sensors
- 21

![Slide 21](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_21.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_21_media_rId3.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_21_media_rId2.gif)

---

## Slide 22

- Magnetic (Hall) sensors
- 22

![Slide 22](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22_media_rId4.emf)

---

## Slide 23

- Incremental rotary encoders (IRC)
- 23

![Slide 23](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_23.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_23_media_rId2.gif)

---

## Slide 24

- Absolute rotary encoders
- 24

![Slide 24](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_24.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_24_media_rId2.gif)

---

## Slide 25

- 25
- Absolute rotary encoders

![Slide 25](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_25.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_25_media_rId2.png)

---

## Slide 26

- ROBOT – IMU sensor
- 26

![Slide 26](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26_media_rId3.jpeg)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26_media_rId4.png)

---

## Slide 27

- 27
- ROBOT – IMU sensor

![Slide 27](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27_media_rId4.png)

---

## Slide 28

- 28
- ROBOT – IMU sensor
- Digital filter in IMU sensor

![Slide 28](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28_media_rId4.png)

---

## Slide 29

- Inductive proximity sensors
- 29
- Only work with conductive objects

![Slide 29](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_media_rId5.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_media_rId4.emf)

---

## Slide 30

- Capacitive proximity sensors
- 30

![Slide 30](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30_media_rId4.png)

---

## Slide 31

- Optic proximity sensors
- 31

![Slide 31](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31_media_rId3.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31_media_rId2.png)

![Embedded Media](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31_media_rId4.emf)

---

