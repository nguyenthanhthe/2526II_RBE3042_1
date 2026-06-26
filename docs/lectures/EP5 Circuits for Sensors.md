---
layout: default
title: "EP5: Mạch cho Cảm biến"
nav_order: 5
parent: Bài giảng
---

# EP5 Circuits for Sensors

> Tài liệu chuyển đổi từ PDF: `EP5 Circuits for Sensors.pdf`

---

## Trang 1

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Circuits for Sensors
- 1

![Trang 1](../../figures/lectures/EP5 Circuits for Sensors_page_1.png)

---

## Trang 2

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Inverting Operational Amplifier
- 𝐴𝑣= 𝑉𝑜𝑢𝑡
- 𝑉𝑖𝑛
- = −
- 𝑅𝑓
- 𝑅𝑖𝑛
- 2

![Trang 2](../../figures/lectures/EP5 Circuits for Sensors_page_2.png)

![Hình ảnh trang 2](../../figures/lectures/EP5 Circuits for Sensors_page_2_img_1.png)

---

## Trang 3

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Non-inverting Operational Amplifier
- 𝐴𝑣= 1 + 𝑅𝐹
- 𝑅2
- 3

![Trang 3](../../figures/lectures/EP5 Circuits for Sensors_page_3.png)

![Hình ảnh trang 3](../../figures/lectures/EP5 Circuits for Sensors_page_3_img_1.png)

---

## Trang 4

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Voltage follower (pre-amplifier)
- 𝐴𝑣= 1
- 4

![Trang 4](../../figures/lectures/EP5 Circuits for Sensors_page_4.png)

![Hình ảnh trang 4](../../figures/lectures/EP5 Circuits for Sensors_page_4_img_1.png)

---

## Trang 5

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Differential Amplifier
- 5

![Trang 5](../../figures/lectures/EP5 Circuits for Sensors_page_5.png)

![Hình ảnh trang 5](../../figures/lectures/EP5 Circuits for Sensors_page_5_img_1.png)

---

## Trang 6

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Differential Amplifier
- Op-Amp as Differential Amplifier
- 𝑣0 =
- 𝑅4
- 𝑅3 + 𝑅4
- 𝑅1 + 𝑅2
- 𝑅1
- 𝑣𝑖2 −𝑅2
- 𝑅1
- 𝑣𝑖1
- If 𝑅1 = 𝑅3 and 𝑅2 = 𝑅4
- 𝑣0 = 𝑅2
- 𝑅1
- (𝑣𝑖2 −𝑣𝑖1)
- 6

![Trang 6](../../figures/lectures/EP5 Circuits for Sensors_page_6.png)

![Hình ảnh trang 6](../../figures/lectures/EP5 Circuits for Sensors_page_6_img_1.png)

---

## Trang 7

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Differential Amplifier
- 7
- 𝒗𝒐= 𝑨𝒅𝒗𝑰𝒅
- 𝒗𝒐= 𝑨𝒄𝒎𝒗𝑰𝒄𝒎
- 𝑣𝑜= 𝐴𝑑𝑣𝐼𝑑+ 𝐴𝑐𝑚𝑣𝐼𝑐𝑚
- Differential gain
- Common-mode gain
- Common-Mode Rejection Ratio (CMRR)
- 𝐶𝑀𝑅𝑅= 20 log 𝐴𝑑
- 𝐴𝑐𝑚

![Trang 7](../../figures/lectures/EP5 Circuits for Sensors_page_7.png)

![Hình ảnh trang 7](../../figures/lectures/EP5 Circuits for Sensors_page_7_img_1.jpeg)

![Hình ảnh trang 7](../../figures/lectures/EP5 Circuits for Sensors_page_7_img_2.png)

---

## Trang 8

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Differential Amplifier
- 8

![Trang 8](../../figures/lectures/EP5 Circuits for Sensors_page_8.png)

![Hình ảnh trang 8](../../figures/lectures/EP5 Circuits for Sensors_page_8_img_1.jpeg)

---

## Trang 9

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Differential Amplifier
- Common mode gain
- 𝐴𝑐𝑚= 𝑣𝑜
- 𝑣𝐼𝑐𝑚
- =
- 𝑅4
- 𝑅4 + 𝑅3
- 1 −𝑅2
- 𝑅1
- 𝑅3
- 𝑅4
- Ideally, 𝑅1 = 𝑅3 and 𝑅2 = 𝑅4
- 𝐴𝑐𝑚= 0 and 𝐶𝑀𝑅𝑅= ∞
- Any mismatch in the resistance ratios can make 𝐴𝑐𝑚nonzero
- 9
- 𝑣𝑜=
- 𝑅4
- 𝑅4 + 𝑅3
- 1 −𝑅2𝑅3
- 𝑅1𝑅4
- 𝑣𝐼𝑐𝑚

![Trang 9](../../figures/lectures/EP5 Circuits for Sensors_page_9.png)

![Hình ảnh trang 9](../../figures/lectures/EP5 Circuits for Sensors_page_9_img_1.png)

---

## Trang 10

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Differential Amplifier
- 
- Differential input resistance
- 𝑅𝑖𝑑≡𝑣𝐼𝑑
- 𝑖𝐼
- 𝑣𝐼𝑑= 𝑅1𝑖𝐼+ 𝑅1𝑖𝐼
- 𝑅𝑖𝑑= 2𝑅1
- 10
- •
- High input impedance: ❌
- •
- Low output impedance: ✔️
- •
- High gain: ❌
- •
- High CMRR: ❌

![Trang 10](../../figures/lectures/EP5 Circuits for Sensors_page_10.png)

![Hình ảnh trang 10](../../figures/lectures/EP5 Circuits for Sensors_page_10_img_1.png)

![Hình ảnh trang 10](../../figures/lectures/EP5 Circuits for Sensors_page_10_img_2.png)

![Hình ảnh trang 10](../../figures/lectures/EP5 Circuits for Sensors_page_10_img_3.png)

---

## Trang 11

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Instrumentation Amplifier
- 𝑣𝑜= 𝑅4
- 𝑅3
- 1 + 𝑅2
- 𝑅1
- 𝑣𝐼𝑑
- 𝐴𝑑=
- 𝑅4
- 𝑅3
- 1 + 𝑅2
- 𝑅1
- 11

![Trang 11](../../figures/lectures/EP5 Circuits for Sensors_page_11.png)

![Hình ảnh trang 11](../../figures/lectures/EP5 Circuits for Sensors_page_11_img_1.png)

---

## Trang 12

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Instrumentation Amplifier
- 12
- 𝑣𝑜= 𝑅4
- 𝑅3
- 1 + 𝑅2
- 𝑅1
- 𝑣𝐼𝑑
- 𝐴𝑑=
- 𝑅4
- 𝑅3
- 1 + 𝑅2
- 𝑅1

![Trang 12](../../figures/lectures/EP5 Circuits for Sensors_page_12.png)

![Hình ảnh trang 12](../../figures/lectures/EP5 Circuits for Sensors_page_12_img_1.png)

---

## Trang 13

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Instrumentation Amplifier
- 13

![Trang 13](../../figures/lectures/EP5 Circuits for Sensors_page_13.png)

![Hình ảnh trang 13](../../figures/lectures/EP5 Circuits for Sensors_page_13_img_1.png)

---

## Trang 14

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Instrumentation Amplifier
- 14

![Trang 14](../../figures/lectures/EP5 Circuits for Sensors_page_14.png)

![Hình ảnh trang 14](../../figures/lectures/EP5 Circuits for Sensors_page_14_img_1.png)

---

## Trang 15

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- Detect and measure very small AC signals (down to a
- few nanovolts) even when the small signal is
- obscured by larger noise source.
- 15

![Trang 15](../../figures/lectures/EP5 Circuits for Sensors_page_15.png)

![Hình ảnh trang 15](../../figures/lectures/EP5 Circuits for Sensors_page_15_img_1.png)

---

## Trang 16

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in Amplifier
- 16

![Trang 16](../../figures/lectures/EP5 Circuits for Sensors_page_16.png)

![Hình ảnh trang 16](../../figures/lectures/EP5 Circuits for Sensors_page_16_img_1.png)

---

## Trang 17

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- 17

![Trang 17](../../figures/lectures/EP5 Circuits for Sensors_page_17.png)

![Hình ảnh trang 17](../../figures/lectures/EP5 Circuits for Sensors_page_17_img_1.png)

---

## Trang 18

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- Signal of interest: 𝑉𝑠𝑖𝑔sin(𝜔𝑟𝑡+ 𝜃𝑠𝑖𝑔)
- Reference signal: 𝑉𝐿sin(𝜔𝑜𝑡+ 𝜃𝑟𝑒𝑓)
- 𝑉𝑝𝑠𝑑= 𝑉𝑠𝑖𝑔𝑉𝐿sin 𝜔𝑟𝑡+ 𝜃𝑠𝑖𝑔sin 𝜔𝐿𝑡+ 𝜃𝑟𝑒𝑓
- = 1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos
- 𝜔𝑟−𝜔𝐿𝑡+ 𝜃𝑠𝑖𝑔−𝜃𝑟𝑒𝑓
- −1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos
- 𝜔𝑟+ 𝜔𝐿𝑡+ 𝜃𝑠𝑖𝑔+ 𝜃𝑟𝑒𝑓
- 18

![Trang 18](../../figures/lectures/EP5 Circuits for Sensors_page_18.png)

![Hình ảnh trang 18](../../figures/lectures/EP5 Circuits for Sensors_page_18_img_1.png)

---

## Trang 19

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- If 𝜔𝐿= 𝜔𝑟, the difference frequency component will
- be a DC signal.
- 𝑉𝑝𝑠𝑑= 1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos 𝜃𝑠𝑖𝑔−𝜃𝑟𝑒𝑓−1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos(2𝜔𝑡+ 𝜃𝑠𝑖𝑔+ 𝜃𝑟𝑒𝑓)
- 19

![Trang 19](../../figures/lectures/EP5 Circuits for Sensors_page_19.png)

![Hình ảnh trang 19](../../figures/lectures/EP5 Circuits for Sensors_page_19_img_1.png)

![Hình ảnh trang 19](../../figures/lectures/EP5 Circuits for Sensors_page_19_img_2.png)

---

## Trang 20

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- If 𝜔𝐿= 𝜔𝑟, the difference frequency component will
- be a DC signal.
- 𝑉𝑝𝑠𝑑= 1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos 𝜃𝑠𝑖𝑔−𝜃𝑟𝑒𝑓−1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos(2𝜔𝑡+ 𝜃𝑠𝑖𝑔+ 𝜃𝑟𝑒𝑓)
- 20

![Trang 20](../../figures/lectures/EP5 Circuits for Sensors_page_20.png)

![Hình ảnh trang 20](../../figures/lectures/EP5 Circuits for Sensors_page_20_img_1.png)

---

## Trang 21

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- 
- If 𝜔𝐿≠𝜔𝑟, signal components with different frequencies make
- new signals, but they still have an average vale of zero
- 21

![Trang 21](../../figures/lectures/EP5 Circuits for Sensors_page_21.png)

![Hình ảnh trang 21](../../figures/lectures/EP5 Circuits for Sensors_page_21_img_1.jpeg)

![Hình ảnh trang 21](../../figures/lectures/EP5 Circuits for Sensors_page_21_img_2.jpeg)

![Hình ảnh trang 21](../../figures/lectures/EP5 Circuits for Sensors_page_21_img_3.jpeg)

![Hình ảnh trang 21](../../figures/lectures/EP5 Circuits for Sensors_page_21_img_4.jpeg)

---

## Trang 22

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- If 𝜔𝐿≠𝜔𝑟, signal components with different
- frequencies make new signals, but they still have an
- average vale of zero
- 22

![Trang 22](../../figures/lectures/EP5 Circuits for Sensors_page_22.png)

![Hình ảnh trang 22](../../figures/lectures/EP5 Circuits for Sensors_page_22_img_1.png)

---

## Trang 23

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Lock-in amplifier
- 𝑋=
- 1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿cos 𝜃𝑠𝑖𝑔−𝜃𝑟𝑒𝑓
- 𝑌=
- 1
- 2 𝑉𝑠𝑖𝑔𝑉𝐿sin 𝜃𝑠𝑖𝑔−𝜃𝑟𝑒𝑓
- 23
- 𝐴= 2 ×
- 𝑋2 + 𝑌2
- 𝑃ℎ𝑎𝑠𝑒= tan−1 𝑌
- 𝑋

![Trang 23](../../figures/lectures/EP5 Circuits for Sensors_page_23.png)

![Hình ảnh trang 23](../../figures/lectures/EP5 Circuits for Sensors_page_23_img_1.jpeg)

---

## Trang 24

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Log Amplifier
- 𝑉𝑜𝑢𝑡= −𝑉𝑇ln 𝑉𝑖𝑛
- 𝐼𝑠𝑅
- 24

![Trang 24](../../figures/lectures/EP5 Circuits for Sensors_page_24.png)

![Hình ảnh trang 24](../../figures/lectures/EP5 Circuits for Sensors_page_24_img_1.png)

---

## Trang 25

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Anti-Log Amplifier
- 𝑉𝑜𝑢𝑡= −𝑅𝑓𝐼𝑠𝑒
- 𝑉𝑖
- 𝑉𝑇
- 25

![Trang 25](../../figures/lectures/EP5 Circuits for Sensors_page_25.png)

![Hình ảnh trang 25](../../figures/lectures/EP5 Circuits for Sensors_page_25_img_1.jpeg)

---

## Trang 26

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bias (zero drift) removal
- 26

![Trang 26](../../figures/lectures/EP5 Circuits for Sensors_page_26.png)

![Hình ảnh trang 26](../../figures/lectures/EP5 Circuits for Sensors_page_26_img_1.png)

---

## Trang 27

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Signal integration
- 27

![Trang 27](../../figures/lectures/EP5 Circuits for Sensors_page_27.png)

![Hình ảnh trang 27](../../figures/lectures/EP5 Circuits for Sensors_page_27_img_1.png)

---

## Trang 28

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Signal differentiation
- 28

![Trang 28](../../figures/lectures/EP5 Circuits for Sensors_page_28.png)

![Hình ảnh trang 28](../../figures/lectures/EP5 Circuits for Sensors_page_28_img_1.png)

---

## Trang 29

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Voltage comparator
- 29

![Trang 29](../../figures/lectures/EP5 Circuits for Sensors_page_29.png)

![Hình ảnh trang 29](../../figures/lectures/EP5 Circuits for Sensors_page_29_img_1.png)

---

## Trang 30

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Schmitt trigger
- 30

![Trang 30](../../figures/lectures/EP5 Circuits for Sensors_page_30.png)

![Hình ảnh trang 30](../../figures/lectures/EP5 Circuits for Sensors_page_30_img_1.png)

![Hình ảnh trang 30](../../figures/lectures/EP5 Circuits for Sensors_page_30_img_2.png)

![Hình ảnh trang 30](../../figures/lectures/EP5 Circuits for Sensors_page_30_img_3.png)

---

## Trang 31

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Signal addition
- 31

![Trang 31](../../figures/lectures/EP5 Circuits for Sensors_page_31.png)

![Hình ảnh trang 31](../../figures/lectures/EP5 Circuits for Sensors_page_31_img_1.png)

---

## Trang 32

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Signal multiplication
- 32

![Trang 32](../../figures/lectures/EP5 Circuits for Sensors_page_32.png)

![Hình ảnh trang 32](../../figures/lectures/EP5 Circuits for Sensors_page_32_img_1.png)

---

## Trang 33

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Signal multiplication
- 33

![Trang 33](../../figures/lectures/EP5 Circuits for Sensors_page_33.png)

![Hình ảnh trang 33](../../figures/lectures/EP5 Circuits for Sensors_page_33_img_1.png)

---

## Trang 34

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Low Pass Filter
- 34
- Passive Low Pass Filter
- Active Low Pass Filter

![Trang 34](../../figures/lectures/EP5 Circuits for Sensors_page_34.png)

![Hình ảnh trang 34](../../figures/lectures/EP5 Circuits for Sensors_page_34_img_1.png)

![Hình ảnh trang 34](../../figures/lectures/EP5 Circuits for Sensors_page_34_img_2.png)

---

## Trang 35

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- High Pass Filter
- 35
- Passive High Pass Filter
- Active High Pass Filter

![Trang 35](../../figures/lectures/EP5 Circuits for Sensors_page_35.png)

![Hình ảnh trang 35](../../figures/lectures/EP5 Circuits for Sensors_page_35_img_1.png)

![Hình ảnh trang 35](../../figures/lectures/EP5 Circuits for Sensors_page_35_img_2.png)

---

