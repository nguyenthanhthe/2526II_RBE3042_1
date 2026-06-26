# EP4 Variable conversion elements

> Tài liệu chuyển đổi từ PDF: `EP4 Variable conversion elements.pdf`

---

## Trang 1

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Variable Conversion Elements
- 1

![Trang 1](../../figures/lectures/EP4 Variable conversion elements_page_1.png)

---

## Trang 2

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Variable Conversion Elements
- 2

![Trang 2](../../figures/lectures/EP4 Variable conversion elements_page_2.png)

![Hình ảnh trang 2](../../figures/lectures/EP4 Variable conversion elements_page_2_img_1.jpeg)

---

## Trang 3

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- Balanced, DC bridge (Wheatstone bridge)
- 3
- 
- Unknown resistance 𝑅𝑢
- 
- Two equal value resistor 𝑅2
- and 𝑅3
- 
- Variable resistor 𝑅𝑣
- Assume 𝐼𝑚= 0
- 𝐼1 = 𝐼3 and 𝐼2 = 𝐼4
- 𝑅𝑢𝑅2 = 𝑅3𝑅𝑣or 𝑅𝑢=
- 𝑅3𝑅𝑣
- 𝑅2

![Trang 3](../../figures/lectures/EP4 Variable conversion elements_page_3.png)

![Hình ảnh trang 3](../../figures/lectures/EP4 Variable conversion elements_page_3_img_1.png)

---

## Trang 4

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- Unblanced DC bridge
- 4
- Unknown resistance 𝑅𝑢
- Two equal value resistor
- 𝑅2 and 𝑅3
- 𝑅1 has the same value of
- the nominal value of 𝑅𝑢
- 𝑉0 = 𝑉𝑖
- 𝑅𝑢
- 𝑅𝑢+ 𝑅3
- −
- 𝑅1
- 𝑅1 + 𝑅2
- 𝑉0 varies non-linearly with 𝑅𝑢

![Trang 4](../../figures/lectures/EP4 Variable conversion elements_page_4.png)

![Hình ảnh trang 4](../../figures/lectures/EP4 Variable conversion elements_page_4_img_1.png)

---

## Trang 5

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- 
- Deflection-type DC bridge
- Example
- Một loại đầu dò áp suất được thiết kế để đo áp suất trong
- phạm vi 0-10bar. Cảm biến áp suất có điện trở danh định là
- 120Ω và tạo thành một nhánh của mạch cầu Wheatstone, với
- ba nhánh còn lại, mỗi nhánh có điện trở 120Ω. Đầu ra của
- mạch cầu được đo bằng một thiết bị có trở kháng đầu vào vô
- hạn.
- Để hạn chế tác động do nhiệt, dòng điện cực đại cho phép
- qua cảm biến áp suất là 30mA, hãy tính điện áp kích mạch
- cầu lớn nhất.
- Nếu độ nhạy của máy đo biến dạng là 338mΩ/bar và sử dụng
- điện áp kích thích mạch cầu lớn nhất, hãy tính điện áp đầu ra
- của mạch cầu khi đo áp suất 10 bar.
- 5

![Trang 5](../../figures/lectures/EP4 Variable conversion elements_page_5.png)

![Hình ảnh trang 5](../../figures/lectures/EP4 Variable conversion elements_page_5_img_1.png)

---

## Trang 6

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- 
- Deflection-type DC bridge
- Example
- 𝑅1 = 𝑅2 = 𝑅3 = 120Ω
- Defining 𝐼1 to be the current flowing in path ADC of the bridge
- 𝑉𝑖= 𝐼1 𝑅𝑢+ 𝑅3
- At balance, 𝑅𝑢= 120, the maximum value allowable for 𝐼1is 0.03 A.
- 𝑉𝑖= 0.03 120 + 120 = 7.2 𝑉
- For a pressure of 10 bar applied, the resistance change is 3.38 Ω, i.e.
- 𝑅𝑢is then equal to 123.38 Ω.
- 𝑉0 = 𝑉𝑖
- 𝑅𝑢
- 𝑅𝑢+ 𝑅3
- −
- 𝑅1
- 𝑅1 + 𝑅2
- = 7.2 123.38
- 243.38 −120
- 240
- = 50 𝑚𝑉
- 6

![Trang 6](../../figures/lectures/EP4 Variable conversion elements_page_6.png)

---

## Trang 7

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- AC balanced impedance bridges
- 7
- 𝐼1𝑅1 = 𝐼2𝑅2; I1Zu = I2Zv
- 𝑍𝑢= 𝑍𝑣𝑅1
- 𝑅2
- 
- If 𝑍𝑢is capacitive, 𝑍𝑢= 1/𝑗𝜔𝐶𝑢, variable capacitance.
- 
- If 𝑍𝑢is inductive, 𝑍𝑢= 𝑅𝑢+ 𝑗𝜔𝐿𝑢, variable-resistance and a
- variable-inductance.

![Trang 7](../../figures/lectures/EP4 Variable conversion elements_page_7.png)

![Hình ảnh trang 7](../../figures/lectures/EP4 Variable conversion elements_page_7_img_1.png)

---

## Trang 8

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- AC null-type impedance bridges
- 8
- 𝑸= 𝝎𝑳
- 𝑹
- Q factor = inductance/resistance.

![Trang 8](../../figures/lectures/EP4 Variable conversion elements_page_8.png)

![Hình ảnh trang 8](../../figures/lectures/EP4 Variable conversion elements_page_8_img_1.png)

![Hình ảnh trang 8](../../figures/lectures/EP4 Variable conversion elements_page_8_img_2.jpeg)

---

## Trang 9

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- Maxwell bridge
- 9
- 𝑅𝑢= 𝑅2𝑅3
- 𝑅1
- ; 𝐿𝑢= 𝑅2𝑅3𝐶
- 𝑄= 𝜔𝐿𝑢
- 𝑅𝑢= 𝜔𝐶𝑅1 → measure the Q value of a coil.

![Trang 9](../../figures/lectures/EP4 Variable conversion elements_page_9.png)

![Hình ảnh trang 9](../../figures/lectures/EP4 Variable conversion elements_page_9_img_1.png)

![Hình ảnh trang 9](../../figures/lectures/EP4 Variable conversion elements_page_9_img_2.png)

---

## Trang 10

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Bridge circuits
- Unbalanced AC bridge
- 10
- For capacitance measurement:
- 𝑍𝑢=
- 1
- 𝑗𝜔𝐶; 𝑍1 =
- 1
- 𝑗𝜔𝐶
- For inductance measurement:
- 𝑍𝑢= 𝑗𝜔𝐿𝑢; 𝑍1 = 𝑗𝜔𝐿
- 𝑉0 = 𝑉𝑠
- 𝑍𝑢
- 𝑍1 + 𝑍𝑢
- −
- 𝑅3
- 𝑅2 + 𝑅3
- For capacitances: 𝑉0 = 𝑉𝑠
- 𝐶1
- 𝐶1+𝐶𝑢−
- 𝑅3
- 𝑅2+𝑅3
- For inductances: 𝑉0 = 𝑉𝑠
- 𝐿𝑢
- 𝐿1+𝐿𝑢−
- 𝑅3
- 𝑅2+𝑅3

![Trang 10](../../figures/lectures/EP4 Variable conversion elements_page_10.png)

![Hình ảnh trang 10](../../figures/lectures/EP4 Variable conversion elements_page_10_img_1.png)

---

## Trang 11

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Inductance measurement
- 
- Connecting the unknown
- inductance in series with a
- variable resistance in a circuit
- excited with a sinusoidal voltage.
- 
- The variable resistance is adjusted
- until the voltage measured across
- the resistance is equal to that
- measured across the inductance.
- 𝐿=
- 𝑅2 −𝑟2
- 2𝜋𝑓
- 11
- 
- Output in the form of a change in inductance: inductive
- displacement sensor
- 
- Measured by an AC bridge circuit

![Trang 11](../../figures/lectures/EP4 Variable conversion elements_page_11.png)

![Hình ảnh trang 11](../../figures/lectures/EP4 Variable conversion elements_page_11_img_1.png)

---

## Trang 12

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Capacitance measurement
- 
- Connecting the unknown
- capacitor in series with a variable
- resistance in a circuit excited with
- a sinusoidal voltage.
- 
- An AC voltmeter is used to
- measure the voltage drop across
- both the resistor and the
- capacitor
- 𝐶=
- 𝑉𝑟
- 2𝜋𝑓𝑅𝑉𝑐
- 12
- 
- Output in the form of a change in capacitance: capacitive
- displacement sensor, capacitive moisture meter and capacitive
- hygrometer.
- 
- Measured by an AC bridge circuit.

![Trang 12](../../figures/lectures/EP4 Variable conversion elements_page_12.png)

![Hình ảnh trang 12](../../figures/lectures/EP4 Variable conversion elements_page_12_img_1.png)

---

## Trang 13

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- 13
- 𝑓𝑜=
- 𝑐+ 𝑣0
- 𝑐+ 𝑣𝑠
- 𝑓𝑠
- •
- 𝑓0: observer frequency of sound
- •
- 𝑐: speed of sound waves
- •
- 𝑣𝑜: observer velocity
- •
- 𝑣𝑠: source velocity
- •
- 𝑓𝑠: actual frequency of sound waves
- Doppler effect

![Trang 13](../../figures/lectures/EP4 Variable conversion elements_page_13.png)

![Hình ảnh trang 13](../../figures/lectures/EP4 Variable conversion elements_page_13_img_1.png)

---

## Trang 14

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- Digital counter-timers
- 14
- The accuracy of measurement depends upon how far the unknown
- frequency is above the reference frequency.
- 𝐟𝐫𝐞𝐪𝐮𝐞𝐧𝐜𝐲= 𝐓𝐫𝐢𝐠𝐠𝐞𝐫𝐥𝐞𝐯𝐞𝐥𝐜𝐫𝐨𝐬𝐬𝐢𝐧𝐠𝐬
- 𝐭𝐢𝐦𝐞𝐢𝐧𝐬𝐞𝐜𝐨𝐧𝐝𝐬

![Trang 14](../../figures/lectures/EP4 Variable conversion elements_page_14.png)

![Hình ảnh trang 14](../../figures/lectures/EP4 Variable conversion elements_page_14_img_1.png)

---

## Trang 15

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- 15

![Trang 15](../../figures/lectures/EP4 Variable conversion elements_page_15.png)

![Hình ảnh trang 15](../../figures/lectures/EP4 Variable conversion elements_page_15_img_1.png)

![Hình ảnh trang 15](../../figures/lectures/EP4 Variable conversion elements_page_15_img_2.jpeg)

---

## Trang 16

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- 16

![Trang 16](../../figures/lectures/EP4 Variable conversion elements_page_16.png)

![Hình ảnh trang 16](../../figures/lectures/EP4 Variable conversion elements_page_16_img_1.png)

![Hình ảnh trang 16](../../figures/lectures/EP4 Variable conversion elements_page_16_img_2.png)

---

## Trang 17

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- 17

![Trang 17](../../figures/lectures/EP4 Variable conversion elements_page_17.png)

![Hình ảnh trang 17](../../figures/lectures/EP4 Variable conversion elements_page_17_img_1.png)

---

## Trang 18

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- Phase-locked loop
- 18
- The DC output from the VCO is then proportional to the
- input signal frequency

![Trang 18](../../figures/lectures/EP4 Variable conversion elements_page_18.png)

![Hình ảnh trang 18](../../figures/lectures/EP4 Variable conversion elements_page_18_img_1.png)

---

## Trang 19

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- Phase-locked loop
- 19

![Trang 19](../../figures/lectures/EP4 Variable conversion elements_page_19.png)

![Hình ảnh trang 19](../../figures/lectures/EP4 Variable conversion elements_page_19_img_1.png)

---

## Trang 20

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- Cathode ray oscilloscope
- 20

![Trang 20](../../figures/lectures/EP4 Variable conversion elements_page_20.png)

![Hình ảnh trang 20](../../figures/lectures/EP4 Variable conversion elements_page_20_img_1.png)

![Hình ảnh trang 20](../../figures/lectures/EP4 Variable conversion elements_page_20_img_2.png)

---

## Trang 21

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Frequency measurement
- The Wien bridge
- 21
- The instrument is very accurate at audio frequencies, but at higher
- frequencies errors due to losses in the capacitors become significant.
- 𝑓=
- 1
- 2𝜋𝑅3𝐶3

![Trang 21](../../figures/lectures/EP4 Variable conversion elements_page_21.png)

![Hình ảnh trang 21](../../figures/lectures/EP4 Variable conversion elements_page_21_img_1.png)

---

## Trang 22

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Phase measurement
- 22

![Trang 22](../../figures/lectures/EP4 Variable conversion elements_page_22.png)

![Hình ảnh trang 22](../../figures/lectures/EP4 Variable conversion elements_page_22_img_1.jpeg)

![Hình ảnh trang 22](../../figures/lectures/EP4 Variable conversion elements_page_22_img_2.png)

---

## Trang 23

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Phase measurement
- Electronic counter-timer
- 23

![Trang 23](../../figures/lectures/EP4 Variable conversion elements_page_23.png)

![Hình ảnh trang 23](../../figures/lectures/EP4 Variable conversion elements_page_23_img_1.png)

---

## Trang 24

- Khoa Điện tử- Viễn thông
- Trường Đại học Công nghệ, ĐHQGHN
- Cảm biến và đo lường cho robot
- Voltage-Controlled Oscillator (VCO)
- 24

![Trang 24](../../figures/lectures/EP4 Variable conversion elements_page_24.png)

![Hình ảnh trang 24](../../figures/lectures/EP4 Variable conversion elements_page_24_img_1.jpeg)

---

