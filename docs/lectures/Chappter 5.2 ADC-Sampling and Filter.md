# Chappter 5.2 ADC-Sampling and Filter

> Tài liệu chuyển đổi từ slide PowerPoint: `Chappter 5.2 ADC-Sampling and Filter.pptx`

---


## Slide 1

### ADC- Sampling and Filter

- 1

---


## Slide 2

### ADC Sampling

- 2
- 
![Hình ảnh slide 2](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_2_img_1.png)

- Measurement systems block diagram

---


## Slide 3

### ADC interface and sampling

- 
![Hình ảnh slide 3](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_3_img_2.png)

- 3

---


## Slide 4

### Digital Filters for sensor

- 4
- FIR (Finite Impulse Response) bộ lọc số có đáp ứng xung hữu hạn:
- Fs = 1 / 2 (ms) = 500 Hz, Fc = 50 Hz (low-pass), cửa sổ lọc N=5
- Thiết kế low-pass FIR thực chiến cho sensor
- 𝑥(𝑡) : tín hiệu vào
- ℎ(𝑡) : đáp ứng xung (impulse response)𝑦(𝑡) : tín hiệu ra

---


## Slide 5

### 5

- sinc(x)=sin(πx)/πx​
- h[n]=2⋅0.1⋅sinc(0.2(n−2))
- Digital Filter for sensor
- h[n]=hideal​[n]⋅w[n]

---


## Slide 6

### Digital Filter for sensor

- 6

---


## Slide 7

### 7

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

---


## Slide 8

### IIR Low pass filter-Bộ lọc đáp ứng xung vô hạn

- 8

---


## Slide 9

### 9

- float alpha = 0.385;
- float y_prev = 0;
- float IIR_LPF(float x)
- {
- float y = alpha * x + (1 - alpha) * y_prev;
- y_prev = y;
- return y;
- }
- 
![Hình ảnh slide 9](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_9_img_3.png)

- IIR Low pass filter
- IIR Low pass filter bậc I

---


## Slide 10

### 10

- 
![Hình ảnh slide 10](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_10_img_4.png)

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

---


## Slide 11

### Kalman filter for sensor

- 11
- Group discussion

---


## Slide 12

### Sensors for mobile robot

- 12
- 
![Hình ảnh slide 12](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_12_img_5.png)


---


## Slide 13

### Sensors for Robots- Mobile robot

- 13
- IMU sensor
- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_6.png)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_7.png)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_8.png)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_9.png)

- Motor: Encoder – Hall sensors
- Approximate sensor
- GPS
- Deep camera
- Line sensor
- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_10.jpg)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_11.png)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_12.jpg)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_13.png)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_14.jpg)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_15.jpg)

- 
![Hình ảnh slide 13](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_13_img_16.png)

- Lidar sensor

---


## Slide 14

### ROS and Sensors

- 14
- 
![Hình ảnh slide 14](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14_img_17.png)

- 
![Hình ảnh slide 14](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14_img_18.png)

- 
![Hình ảnh slide 14](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_14_img_19.png)


---


## Slide 15

### ROS - Sensors

- 15
- 
![Hình ảnh slide 15](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_15_img_20.png)

- 
![Hình ảnh slide 15](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_15_img_21.png)

- 
![Hình ảnh slide 15](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_15_img_22.png)


---


## Slide 16

### Laser scanner- LIDAR

- 16
- 
![Hình ảnh slide 16](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16_img_23.png)

- 
![Hình ảnh slide 16](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16_img_24.png)

- 
![Hình ảnh slide 16](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_16_img_25.png)


---


## Slide 17

### 17

- 
![Hình ảnh slide 17](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_img_26.jpg)

- 
![Hình ảnh slide 17](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_img_27.png)

- 2D Lidar
- 3D Lidar
- 
![Hình ảnh slide 17](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_img_28.png)

- 
![Hình ảnh slide 17](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_17_img_29.jpg)

- Laser scanner- LIDAR

---


## Slide 18

### BLDC MOTOR

- 18
- 
![Hình ảnh slide 18](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_img_30.png)

- 
![Hình ảnh slide 18](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_img_31.jpg)

- ROBOT Dynamic control
- 
![Hình ảnh slide 18](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_img_32.png)

- 
![Hình ảnh slide 18](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_18_img_33.png)


---


## Slide 19

### ROBOT-BLDC MOTOR

- 19
- 
![Hình ảnh slide 19](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_19_img_34.png)

- BLDC MOTOR

---


## Slide 20

### 20

- 
![Hình ảnh slide 20](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20_img_35.png)

- ROBOT-BLDC MOTOR
- BLDC MOTOR
- 
![Hình ảnh slide 20](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20_img_36.png)

- 
![Hình ảnh slide 20](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_20_img_37.png)


---


## Slide 21

### Magnetic (Hall) sensors

- 21
- 
![Hình ảnh slide 21](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_21_img_38.gif)

- 
![Hình ảnh slide 21](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_21_img_39.jpg)


---


## Slide 22

### Magnetic (Hall) sensors

- 22
- 
![Hình ảnh slide 22](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22_img_40.png)

- 
![Hình ảnh slide 22](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22_img_41.png)

- 
![Hình ảnh slide 22](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_22_img_42.wmf)


---


## Slide 23

### Incremental rotary encoders (IRC)

- 
![Hình ảnh slide 23](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_23_img_43.gif)

- 23

---


## Slide 24

### Absolute rotary encoders

- 
![Hình ảnh slide 24](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_24_img_44.gif)

- 24

---


## Slide 25

### 25

- 
![Hình ảnh slide 25](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_25_img_45.png)

- Absolute rotary encoders

---


## Slide 26

### ROBOT – IMU sensor

- 26
- 
![Hình ảnh slide 26](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26_img_46.png)

- 
![Hình ảnh slide 26](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26_img_47.jpg)

- 
![Hình ảnh slide 26](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_26_img_48.png)


---


## Slide 27

### 27

- ROBOT – IMU sensor
- 
![Hình ảnh slide 27](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27_img_49.png)

- 
![Hình ảnh slide 27](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27_img_50.png)

- 
![Hình ảnh slide 27](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_27_img_51.png)


---


## Slide 28

### 28

- ROBOT – IMU sensor
- 
![Hình ảnh slide 28](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28_img_52.png)

- 
![Hình ảnh slide 28](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28_img_53.png)

- Digital filter in IMU sensor
- 
![Hình ảnh slide 28](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_28_img_54.png)


---


## Slide 29

### Inductive proximity sensors

- 29
- 
![Hình ảnh slide 29](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_img_55.png)

- Only work with conductive objects
- 
![Hình ảnh slide 29](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_img_56.png)

- 
![Hình ảnh slide 29](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_img_57.wmf)

- 
![Hình ảnh slide 29](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_29_img_58.png)


---


## Slide 30

### Capacitive proximity sensors

- 30
- 
![Hình ảnh slide 30](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30_img_59.png)

- 
![Hình ảnh slide 30](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30_img_60.png)

- 
![Hình ảnh slide 30](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_30_img_61.png)


---


## Slide 31

### Optic proximity sensors

- 31
- 
![Hình ảnh slide 31](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31_img_62.png)

- 
![Hình ảnh slide 31](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31_img_63.png)

- 
![Hình ảnh slide 31](../../figures/lectures/Chappter 5.2 ADC-Sampling and Filter_slide_31_img_64.wmf)


---
