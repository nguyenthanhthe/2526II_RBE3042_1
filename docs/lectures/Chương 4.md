---
layout: default
title: "Chương 4: Phân loại Cảm biến"
nav_order: 7
parent: Bài giảng
---

# Chương 4

> Tài liệu chuyển đổi từ DOCX: `Chương 4.docx`

---

Chương 4: Mạch đo lường và xử lý tín hiệu lối ra cảm biến (Signal Conditioning)
Trong các chương trước, chúng ta đã trình bày các nguyên lý chuyển đổi (transducer) nhằm biến đổi các đại lượng vật lý và môi trường thành tín hiệu điện. Tuy nhiên, trong hầu hết các trường hợp, tín hiệu điện thu được từ cảm biến không thể đưa trực tiếp vào các thiết bị đọc, hiển thị hoặc làm đầu vào cho hệ thống đo lường và điều khiển, mà cần phải được xử lý trước.
Cụ thể, tín hiệu từ cảm biến thường có mức năng lượng thấp, đặc tính chưa tuyến tính hoặc chưa nằm trong dải đo phù hợp với các mạch xử lý phía sau. Bên cạnh đó, các nguồn nhiễu từ môi trường và từ chính hệ thống điện tử cũng có thể ảnh hưởng đáng kể đến độ chính xác của phép đo. Vì vậy, việc thiết kế các mạch xử lý tín hiệu là hết sức cần thiết nhằm thực hiện các chức năng như khuếch đại tín hiệu, lọc nhiễu, điều chỉnh dải đo, tuyến tính hóa đặc tính cảm biến và đảm bảo tín hiệu đầu ra đáp ứng yêu cầu của hệ thống.
Bên cạnh các đặc tính chuyển đổi giữa đại lượng vật lý và tín hiệu điện, cảm biến còn được đặc trưng bởi các tham số điện quan trọng như trở kháng đầu ra và công suất tín hiệu. Những tham số này có ảnh hưởng trực tiếp đến khả năng truyền tín hiệu và hiệu quả ghép nối giữa cảm biến với các khối xử lý tín hiệu phía sau.
Trở kháng đầu ra của cảm biến ( $$Z_{out}$$ ) biểu thị khả năng cung cấp tín hiệu điện của cảm biến tới tải bên ngoài. Khi cảm biến được kết nối với một mạch đo hoặc mạch xử lý tín hiệu có trở kháng đầu vào  $$Z_{in}$$ , mối quan hệ giữa hai giá trị trở kháng này sẽ quyết định mức tín hiệu thực sự được truyền tới mạch tiếp theo. Nếu trở kháng đầu vào của mạch đo không đủ lớn so với trở kháng đầu ra của cảm biến, tín hiệu điện áp sẽ bị suy giảm do hiện tượng phân áp trên các phần tử trở kháng.
Trong nhiều trường hợp, công suất tín hiệu từ cảm biến là rất nhỏ. Theo nguyên lý truyền công suất tối đa, công suất truyền từ nguồn đến tải đạt giá trị lớn nhất khi trở kháng tải bằng trở kháng nguồn. Tuy nhiên, trong các hệ đo lường và cảm biến, mục tiêu thường không phải là truyền công suất tối đa mà là duy trì độ chính xác của tín hiệu điện áp. Vì vậy, mạch đo hoặc mạch tiền xử lý tín hiệu thường được thiết kế sao cho trở kháng đầu vào lớn hơn nhiều so với trở kháng đầu ra của cảm biến, nhằm giảm thiểu sự suy giảm tín hiệu.
Để đảm bảo tín hiệu từ cảm biến được truyền tới hệ thống xử lý dữ liệu một cách chính xác, cần thực hiện phối hợp trở kháng giữa các khối chức năng trong hệ thống. Cụ thể, khối xử lý tín hiệu bao gồm các mạch khuếch đại, lọc và chuyển đổi – thường được thiết kế với trở kháng đầu vào cao để không làm tải cảm biến. Sau đó, tín hiệu đã được khuếch đại và điều chỉnh sẽ được truyền tới như bộ chuyển đổi tương tự–số (ADC) hoặc vi điều khiển. Việc phối hợp trở kháng hợp lý giữa các khối này giúp tối ưu hóa việc truyền tín hiệu, giảm suy hao và nâng cao độ chính xác của toàn bộ hệ thống đo lường.
Trong quá trình chuyển đổi tín hiệu, tín hiệu đầu ra của cảm biến thường có biên độ nhỏ hoặc năng lượng thấp. Do đó, cần sử dụng các mạch khuếch đại để tăng biên độ và công suất của tín hiệu. Chẳng hạn, đối với một số cảm biến nhiệt độ, sự thay đổi điện áp đầu ra chỉ nằm trong dải vài chục microvolt (µV). Vì vậy, tín hiệu này cần được khuếch đại lên mức điện áp cỡ volt (V) để các hệ đo lường hoặc bộ xử lý có thể nhận biết và xử lý một cách hiệu quả.

![Image](../../figures/lectures/Chương 4_rId6.png)

Hình 4.1 Sơ đồ mạch mô tả mô hình lối ra của cảm biến với hệ đo lường 
Hình 4.1 mô tả mô hình truyền tín hiệu điện áp từ đầu ra của cảm biến. Trong đó, tín hiệu điện áp  $$V_{1}$$ xuất hiện tại đầu ra của cảm biến, biểu diễn giá trị của đại lượng cần đo sau khi đã được chuyển đổi từ môi trường sang dạng tín hiệu điện. Tín hiệu này được truyền tới một vôn kế có điện trở đầu vào  $$R_{L}$$ thông qua các dây nối có điện trở hữu hạn  $$R_{w}$$ .
Do dây dẫn có điện trở khác không nên sẽ xuất hiện sụt áp  $$ΔV$$ trên các dây nối. Vì vậy, điện áp đo được tại vôn kế  $$V_{2}$$ sẽ nhỏ hơn điện áp đầu ra ban đầu của cảm biến  $$V_{1}$$ . Ngoài ra, trong thực tế, các dây dẫn còn có thể thu nhận nhiễu điện từ từ môi trường xung quanh do chúng hoạt động như một anten thu nhiễu. Các yếu tố này làm cho tín hiệu nhận được tại thiết bị đo bị sai lệch so với tín hiệu ban đầu của cảm biến.
Truyền tín hiệu ở dạng điện áp thường chỉ phù hợp trong các hệ thống có khoảng cách truyền ngắn và môi trường nhiễu thấp. Trong các trường hợp cần cải thiện chất lượng tín hiệu, người ta có thể sử dụng dây dẫn có lớp bọc chống nhiễu (shielded cable) để hạn chế ảnh hưởng của nhiễu điện từ. Đồng thời, các mạch khuếch đại tín hiệu cũng được sử dụng nhằm giảm ảnh hưởng của sụt áp trên dây dẫn và nâng cao tỷ số tín hiệu trên nhiễu.
Một phương pháp khác là truyền tín hiệu dưới dạng dòng điện thay vì điện áp. Với phương pháp này, tín hiệu được truyền trong một vòng dòng điện kín, trong đó giá trị dòng điện tỉ lệ với giá trị đại lượng đo được từ cảm biến. Phương pháp truyền tín hiệu dòng điện có ưu điểm ít bị ảnh hưởng bởi điện trở của dây dẫn và nhiễu môi trường. Trong công nghiệp, chuẩn truyền tín hiệu dòng điện thường được sử dụng là 4–20 mA.

![Image](../../figures/lectures/Chương 4_rId7.png)

Hình 4.2. Cấu hình hoạt động chuyển đổi tín hiệu của cảm biến dưới dạng tín hiệu dòng điện.
Hình 4.2 mô tả cấu hình hoạt động của cảm biến dưa trên nguyên lý biến đổi dòng điện. Thay vì thay đổi giá trị điện áp thì tín hiệu sẽ đặc trưng biến đổi bởi dòng điện một chiều tạo thành một mạch kín. Việc sử dụng tín hiệu dạng này giúp giảm nhiễu đường dây và tăng độ tin cậy của việc đọc tín hiệu từ cảm biến. Đây cũng là một chuẩn chuyển đổi hay được sử dụng trong công nghiệp khi các cảm biến thương mại có chế độ đọc giá trị dựa trên chuyển đổi dòng điện. 
Ưu điểm quan trọng của phương pháp truyền tín hiệu dòng điện là ít bị ảnh hưởng bởi điện trở của dây dẫn. Dù dây dẫn có gây ra sụt áp, giá trị dòng điện trong mạch vẫn được duy trì gần như không đổi, miễn là nguồn cung cấp đủ điện áp để duy trì vòng dòng điện. Vì vậy, phương pháp này có khả năng truyền tín hiệu ổn định trên khoảng cách xa và trong môi trường có nhiều nhiễu điện từ.
4.1. Mạch khuếch đại tín hiệu (Đảo, Không đảo, Vi sai)
4.1.1 Mạch khuếch đại đảo
 
 Hình 4.3 minh họa sơ đồ nguyên lý của mạch khuếch đại đảo (Inverting amplifier) sử dụng bộ khuếch đại thuật toán (Operational Amplifier – Op-Amp). Trong cấu hình này, tín hiệu đầu vào  $$V_{in}$$ cần được khuếch đại được đưa vào cực đảo của bộ khuếch đại thông qua điện trở  $$R_{in}$$ , trong khi điện trở hồi tiếp  $$R_{f}$$ nối từ đầu ra  $$V_{out}$$ về nút vào đảo. Cực không đảo của bộ khuếch đại được nối với đất (0 V).

![Image](../../figures/lectures/Chương 4_rId8.gif)

Hình 4.3. Sơ đồ nguyên lý của mạch khuếch đại đảo
Do bộ khuếch đại thuật toán có hệ số khuếch đại vòng hở rất lớn, điện áp tại hai đầu vào của op-amp gần như bằng nhau. Vì cực không đảo được nối đất nên điện áp tại nút vào đảo (điểm X trong hình) xấp xỉ bằng 0 V. Điểm này được gọi là điểm đất ảo (virtual ground). Nhờ đặc tính trở kháng đầu vào rất lớn của op-amp, dòng điện đi vào các cực đầu vào gần như bằng không. Do đó, dòng điện  $$I_{in}$$ chạy qua điện trở  $$R_{in}$$ sẽ đi hoàn toàn qua điện trở hồi tiếp  $$R_{f}$$ .
Áp dụng định luật Ohm và định luật Kirchhoff cho nút tại điểm X, ta có:
                                                         $$I_{in}=\frac{V_{in}}{R_{in}}=\frac{-V_{out}}{R_{f}}$$                    (4.1)  
Từ đó thu được hệ số khuếch đại điện áp của mạch:
                                        $$                     V_{out}=-\frac{R_{f}}{R_{in}}V_{in}$$                                                 (4.2)
Dấu âm trong biểu thức cho thấy tín hiệu đầu ra bị đảo pha 180° so với tín hiệu đầu vào. Mạch khuếch đại đảo thường được sử dụng trong các hệ thống xử lý tín hiệu cảm biến (signal conditioning) để khuếch đại các tín hiệu điện áp nhỏ từ cảm biến, đồng thời cung cấp khả năng điều chỉnh hệ số khuếch đại thông qua việc lựa chọn tỉ số giữa hai điện trở  $$R_{f}$$ và  $$R_{in}$$ . Ngoài ra, nhờ đặc tính điểm đất ảo, mạch còn giúp đơn giản hóa việc phân tích dòng điện và giảm ảnh hưởng của tải lên nguồn tín hiệu đầu vào.
Do op-amp lý tưởng có trở kháng đầu vào rất lớn, dòng điện đi vào các cực đầu vào gần như bằng không. Đồng thời, nhờ hồi tiếp âm, điện áp tại hai đầu vào của op-amp gần như bằng nhau ( $$V_{+}≈V_{-}$$ ). Vì cực không đảo được nối đất nên điện áp tại nút vào đảo (điểm X) cũng xấp xỉ bằng 0. Điểm này được gọi là đất ảo (virtual ground).
Dòng điện từ nguồn tín hiệu đi vào mạch là:
                                                       $$I_{in}=\frac{V_{in}-V_{X}}{R_{in}}$$  (4.3)  Do  $$V_{X}≈0$$ :
                                                            $$I_{in}=\frac{V_{in}}{R_{in}}$$              (4.4)  Trở kháng lối vào của mạch được định nghĩa là:
                                                          $$Z_{in}=\frac{V_{in}}{I_{in}}$$                (4.5)  Thay vào ta được:  $$Z_{in}=R_{in}$$  .
        Như vậy, trong cấu hình khuếch đại đảo, trở kháng lối vào của mạch được xác định trực tiếp bởi điện trở  $$R_{in}$$ .  Đối với kháng lối ra của mạch khuếch đại không đảo, Để tính trở kháng lối ra, ta đặt tín hiệu đầu vào bằng 0:  $$V_{in}=0$$  và đặt một nguồn thử  $$V_{t}$$ tại đầu ra để xác định dòng  $$I_{t}$$ .
Trong op-amp thực tế, tồn tại trở kháng đầu ra nội tại  $$Z_{o}$$ . Khi có hồi tiếp âm, trở kháng lối ra của toàn mạch được giảm theo hệ số vòng lặp. Hệ số hồi tiếp của mạch khuếch đại đảo là:
                                                             $$β=\frac{R_{in}}{R_{in}+R_{f}}$$  (4.7)  Nếu  $$A$$  là hệ số khuếch đại vòng hở của op-amp, thì trở kháng lối ra của mạch xấp xỉ:
                                                            $$Z_{out}≈\frac{Z_{o}}{1+Aβ}$$   (4.8)  Do  $$A$$ của op-amp thường rất lớn (cỡ  $$10^{5}-10^{6}$$ ), nên:  $$Z_{out}≪Z_{o}$$ Vì vậy:  $$Z_{out}≈0$$ Việc xác định trở kháng lối vào và trở kháng lối ra của mạch khuếch đại đóng vai trò quan trọng trong thiết kế các hệ thống đo lường và điều khiển. Các tham số này cho phép đánh giá khả năng ghép nối giữa các khối chức năng trong hệ thống, từ cảm biến, mạch tiền xử lý tín hiệu cho đến khối xử lý dữ liệu. Khi các khối được thiết kế với sự phối hợp trở kháng hợp lý, tín hiệu sẽ được truyền đi một cách ổn định và ít bị suy hao. Ngược lại, nếu không chú ý đến vấn đề phối hợp trở kháng, tín hiệu có thể bị suy giảm hoặc biến dạng trong quá trình truyền giữa các khối, làm ảnh hưởng đến độ chính xác và độ tin cậy của toàn bộ hệ thống đo lường và điều khiển. Như vậy, đối với mạch khuếch đại đảo, một đặc trưng cần lưu ý là trở kháng lối vào của mạch được quy định bởi trở phối hợp Rin.
4.1.2 Mạch khuếch đại không đảo
Hình 4.2 mô tả sơ đồ nguyên lý của bộ khuếch đại không đảo sử dụng bộ khuếch đại thuật toán (Operational Amplifier – Op-Amp). Trong sơ đồ nguyên lý này, tín hiệu đầu vào  $$V_{in}$$ được đưa trực tiếp vào cực không đảo (+) của op-amp, trong khi cực đảo (−) được nối với mạng hồi tiếp gồm hai điện trở  $$R_{1}$$ và  $$R_{2}$$ . Điện trở  $$R_{1}$$ nối từ đầu ra  $$V_{out}$$ về cực đảo, còn  $$R_{2}$$ nối từ cực đảo xuống đất.

![Image](../../figures/lectures/Chương 4_rId9.gif)

Hình 4.4. Sơ đồ nguyên lý của mạch khuếch đại không đảo
Do op-amp có hệ số khuếch đại vòng hở rất lớn và mạch có hồi tiếp âm, điện áp tại hai đầu vào gần như bằng nhau: ( $$V_{+}≈V_{-}$$ ) Vì tín hiệu  $$V_{in}$$ được đưa vào cực không đảo nên:
Điện áp tại cực đảo được xác định bởi mạch chia áp gồm  $$R_{1}$$ và  $$R_{2}$$ :
                                                           $$V_{-}=V_{out}\frac{R_{2}}{R_{1}+R_{2}}$$  (4.9)  Do  $$V_{-}≈V_{in}$$ , ta có:
                                                           $$V_{in}=V_{out}\frac{R_{2}}{R_{1}+R_{2}}$$   (4.10)  Từ phương trình trên có thể suy ra hệ số khuếch đại điện áp của mạch:
                                                            $$V_{out}=\left(1+\frac{R_{1}}{R_{2}}\right)V_{in}$$  (4.11)  Như vậy, tín hiệu đầu ra cùng pha với tín hiệu đầu vào, và hệ số khuếch đại được xác định bởi tỉ số giữa hai điện trở hồi tiếp.
Trong cấu hình khuếch đại không đảo, tín hiệu đầu vào được đưa trực tiếp vào cực không đảo của op-amp. Do op-amp lý tưởng có trở kháng đầu vào rất lớn, dòng điện đi vào cực này gần như bằng không ( $$I_{in}≈0$$ ), do đó:
                                                   $$Z_{in}=\frac{V_{in}}{I_{in}}→∞$$   (4.12)  Trong thực tế, trở kháng lối vào của mạch xấp xỉ bằng trở kháng đầu vào của op-amp, thường nằm trong khoảng từ megaohm đến gigaohm. Nhờ đó mạch gần như không làm tải nguồn tín hiệu, rất phù hợp để khuếch đại tín hiệu từ các cảm biến có trở kháng đầu ra lớn.
Đối với trở kháng lối ra, một khuếch đại thuật thực tế có một trở kháng đầu ra nội tại  $$Z_{o}$$ . Tuy nhiên, nhờ có hồi tiếp âm thông qua mạng điện trở  $$R_{1}$$ và  $$R_{2}$$ , trở kháng lối ra của toàn mạch được giảm đáng kể:
                                                       $$Z_{out}≈\frac{Z_{o}}{1+Aβ}$$  (4.13)  
	trong đó:  $$A$$  là hệ số khuếch đại vòng hở của op-amp,  $$β$$ là hệ số hồi tiếp của mạch
Với mạch khuếch đại không đảo:
                                                          $$β=\frac{R_{2}}{R_{1}+R_{2}}$$    (4.14)  
Do  $$A$$  rất lớn, nên trở kháng lối ra xấp xỉ bằng không ( $$Z_{out}≈0$$ ). Điều này giúp mạch có khả năng cung cấp tín hiệu ổn định cho các tải hoặc các khối xử lý tiếp theo như bộ lọc, bộ ADC hoặc vi điều khiển.

![Image](../../figures/lectures/Chương 4_rId10.gif)

Hình 4.5. Sơ đồ nguyên lý của mạch khuếch đại lặp lại tín hiệu (Buffer amplifier)
Hình 4.5 mô tả cấu hình của mạch khuếch đại đệm (buffer amplifier) sử dụng bộ khuếch đại thuật toán (Op-Amp). Trong cấu hình này, tín hiệu đầu vào  $$V_{in}$$ được đưa trực tiếp vào cực không đảo (+) của op-amp, trong khi đầu ra  $$V_{out}$$ được hồi tiếp trực tiếp về cực đảo (−) của bộ khuếch đại. Do đó mạch tạo thành một vòng hồi tiếp âm trực tiếp.
Với đặc tính của op-amp có hệ số khuếch đại vòng hở rất lớn, khi có hồi tiếp âm thì điện áp tại hai đầu vào gần như bằng nhau. Do đó điện áp đầu ra sẽ xấp xỉ tín hiệu điện áp đầu vào ( $$V_{out}≈V_{in}$$ ). 
Do đó hệ số khuếch đại điện áp của mạch xấp xỉ bằng 1, tức là tín hiệu đầu ra có biên độ và pha giống với tín hiệu đầu vào. Mạch không thực hiện khuếch đại biên độ mà chủ yếu dùng để cách phối hợp kháng giữa các khối trong hệ thống.
Một đặc điểm quan trọng của mạch đệm là trở kháng lối vào rất lớn và trở kháng lối ra rất nhỏ. Nhờ vậy mạch gần như không làm tải nguồn tín hiệu ở đầu vào, đồng thời có khả năng cung cấp tín hiệu ổn định cho tải hoặc các khối xử lý phía sau. Vì lý do này, mạch khuếch đại đệm thường được sử dụng trong các hệ thống xử lý tín hiệu cảm biến (signal conditioning) để ghép nối giữa cảm biến có trở kháng cao với các mạch đo, bộ lọc hoặc bộ chuyển đổi tương tự–số (ADC).
4.1.3 Mạch khuếch đại vi sai
Hình 4.6 minh họa việc sử dụng mạch khuếch đại vi sai (differential amplifier) kết hợp với cầu điện trở (resistive bridge) để đo sự thay đổi nhỏ của điện trở trong các cảm biến. Trong cấu hình này, các phần tử điện trở của cầu có thể bao gồm các điện trở chuẩn và một hoặc nhiều điện trở cảm biến. Khi hệ thống ở trạng thái cân bằng, điện áp tại hai nút của cầu bằng nhau nên hiệu điện áp giữa hai đầu ra của cầu gần như bằng không.
Khi đại lượng vật lý cần đo (như áp suất, lực, nhiệt độ hoặc biến dạng) tác động lên cảm biến, giá trị điện trở của phần tử cảm biến thay đổi, làm mất cân bằng cầu điện trở. Sự mất cân bằng này tạo ra hai điện áp  $$V_{1}$$ và  $$V_{2}$$ tại hai nút của cầu. Các tín hiệu này được đưa vào hai đầu vào của bộ khuếch đại vi sai. Bộ khuếch đại sẽ khuếch đại hiệu điện áp giữa hai tín hiệu đầu vào, theo quan hệ:
                                                $$ V_{out}=A(V_{2}-V_{1})$$   (4.15)  trong đó  $$A$$  là hệ số khuếch đại của mạch.

![Image](../../figures/lectures/Chương 4_rId11.png)

Hình 4.6. Mạch khuếch đại vi sai mắc kết hợp với khối cầu điện trở
Nhờ chỉ khuếch đại sai khác giữa hai tín hiệu, mạch khuếch đại vi sai có khả năng loại bỏ các thành phần nhiễu chung xuất hiện đồng thời trên cả hai đường tín hiệu, đồng thời tăng độ nhạy đối với các thay đổi nhỏ của cảm biến. Vì vậy, cấu hình này được sử dụng rộng rãi trong các hệ đo lường chính xác, đặc biệt trong các cảm biến sử dụng cầu Wheatstone như cảm biến áp suất, cảm biến lực hoặc cảm biến biến dạng (strain gauge).
Hình 4.7 minh họa cấu hình mạch khuếch đại vi sai (differential amplifier) sử dụng bộ khuếch đại thuật toán. Trong mạch này, hai tín hiệu đầu vào  $$v_{I1}$$ và  $$v_{I2}$$  được đưa vào hai cực của op-amp thông qua các điện trở  $$R_{1}$$ và  $$R_{3}$$ . Điện trở  $$R_{2}$$  đóng vai trò hồi tiếp từ đầu ra về cực đảo, trong khi điện trở  $$R_{4}$$ nối từ cực không đảo xuống đất nhằm thiết lập mạng phân áp cho tín hiệu đầu vào.

![Image](../../figures/lectures/Chương 4_rId12.png)

      Hình 4.6. Cấu hình mạch khuếch đại vi sai sử dụng bộ khuếch đại thuật toán
Do op-amp có hệ số khuếch đại vòng hở rất lớn và mạch có hồi tiếp âm, điện áp tại hai đầu vào của op-amp gần như bằng nhau ( $$v_{+}≈v_{-}$$ ).  Trước hết xét điện áp tại cực không đảo. Điện áp này được xác định bởi mạch chia áp giữa  $$R_{3}$$ và  $$R_{4}$$ :
                                                         $$v_{+}=v_{I2}\frac{R_{4}}{R_{3}+R_{4}}$$   (4.16)  Do  $$v_{-}≈v_{+}$$ , ta có:
                                                          $$v_{-}=v_{I2}\frac{R_{4}}{R_{3}+R_{4}}$$   (4.17)  Áp dụng định luật Kirchhoff tại nút vào đảo:
                                                          $$\frac{v_{I1}-v_{-}}{R_{1}}=\frac{v_{-}-v_{o}}{R_{2}}$$  (4.18)  Thay biểu thức của  $$v_{-}$$ vào và biến đổi, ta thu được điện áp đầu ra của mạch:          
                                                $$v_{o}=\left(1+\frac{R_{2}}{R_{1}}\right)v_{-}-\frac{R_{2}}{R_{1}}v_{I1}$$  (4.19)  Thay tiếp giá trị  $$v_{-}$$ :
                                             $$v_{o}=\left(1+\frac{R_{2}}{R_{1}}\right)\frac{R_{4}}{R_{3}+R_{4}}v_{I2}-\frac{R_{2}}{R_{1}}v_{I1}$$  (4.20)  Trong trường hợp các điện trở được lựa chọn thỏa mãn điều kiện:
                                                                   $$\frac{R_{2}}{R_{1}}=\frac{R_{4}}{R_{3}}$$     (4.21)  mạch sẽ hoạt động như bộ khuếch đại vi sai lý tưởng, và biểu thức đầu ra trở thành:
                                                          $$v_{o}=\frac{R_{2}}{R_{1}}(v_{I2}-v_{I1})$$  (4.22)  Kết quả này cho thấy điện áp đầu ra tỉ lệ với hiệu điện áp giữa hai tín hiệu đầu vào. Nhờ đó, mạch có khả năng khuếch đại các tín hiệu sai khác nhỏ đồng thời loại bỏ các thành phần nhiễu chung xuất hiện trên cả hai đầu vào. Chính vì vậy, cấu hình khuếch đại vi sai thường được sử dụng trong các hệ xử lý tín hiệu cảm biến, đặc biệt khi kết hợp với các mạch cầu điện trở (Wheatstone bridge) để đo các thay đổi rất nhỏ của điện trở trong các cảm biến như cảm biến biến dạng, cảm biến áp suất hoặc cảm biến lực.
- Common-Mode Rejection Ratio (CMRR) Hệ số khử tín hiệu chế độ chung

	CMRR là tham số được sử dụng để đánh giá khả năng của bộ khuếch đại vi sai trong việc khuếch đại tín hiệu sai khác giữa hai đầu vào và loại bỏ các tín hiệu nhiễu đồng pha. CMRR được định nghĩa là tỉ số giữa hệ số khuếch đại vi sai và hệ số khuếch đại chế độ chung:
                                                   $$CMRR=\frac{A_{d}}{A_{c}}$$  (4.23)  trong đó:
  $$A_{d}$$ : hệ số khuếch đại vi sai.
  $$A_{c}$$ : hệ số khuếch đại chế độ chung được xác định dựa trên 
CMRR thường được biểu diễn dưới dạng decibel (dB):
                                         $$CMRR_{\text{dB}}=20\log_{10}\left(\frac{A_d}{A_c}\right)$$  (4.24)  

![Image](../../figures/lectures/Chương 4_rId13.png)

Hình 4.7. Cấu hình mạch mắc chung đầu vào để xác định hệ số CMRR

4.2. Mạch khuếch đại công cụ (Instrumentation Amplifier) và ứng dụng 

![Image](../../figures/lectures/Chương 4_rId14.png)

Hình 4.8. Cấu hình mạch khuếch đại công cụ
Mạch trong hình bạn đưa là một mạch khuếch đại công cụ (instrumentation amplifier – INA) điển hình, gồm ba op-amp: hai tầng đầu (A1, A2) và một tầng vi sai phía sau (A). Đây là cấu trúc rất phổ biến khi cần đo các tín hiệu nhỏ từ cảm biến trong môi trường nhiễu.
	Hai op-amp A1 và A2 hoạt động như buffer khuếch đại đầu vào, giúp: Tăng trở kháng vào (không làm ảnh hưởng sensor), tiền khuếch đại hiệu điện áp  $$V_{I1}$$ và  $$V_{I2}$$ . Điện trở  $$2R1$$  nối giữa hai nhánh đóng vai trò điều chỉnh hệ số khuếch đại vi sai. Tầng thứ ba (op-amp A) nhận tín hiệu từ A1 và A2 qua các điện trở  $$R3$$ , thực hiện phép trừ (khuếch đại vi sai), Loại bỏ nhiễu đồng pha (common-mode). Ở tầng đầu (A1, A2), do op-amp lý tưởng nên  $$V_{-}≈V_{+}$$  , suy ra điện áp tại hai đầu vào đảo bằng  $$V_{I1}$$ và  $$V_{I2}$$  dòng qua điện trở  $$2R1$$ :

$$
I=\frac{V_{I1}-V_{I2}}{2R1}
$$

Dòng này chạy qua các điện trở hồi tiếp  $$R2$$ , tạo ra điện áp ra của hai op-amp:

$$V_{o1}=V_{I1}+I\cdot R_2, \quad V_{o2}=V_{I2}-I\cdot R_2$$

Lấy hiệu:

$$
V_{o1}-V_{o2}=(V_{I1}-V_{I2})\left(1+\frac{R2}{R1}\right)
$$

Ở tầng  vi sai (op-amp A), mạch này là khuếch đại vi sai chuẩn với tỉ số điện trở:

$$
V_{o}=\frac{R4}{R3}(V_{o1}-V_{o2})
$$

Kết hợp hai tầng:

$$
V_{o}=\left(1+\frac{R2}{R1}\right)\frac{R4}{R3}(V_{I1}-V_{I2})
$$

Ý nghĩa của mạch
Chỉ khuếch đại hiệu điện áp giữa hai đầu vào
Loại bỏ tín hiệu chung (nhiễu)
Có thể điều chỉnh gain bằng cách thay  $$R1$$ 

4.3. Mạch cầu Wheatstone (DC/AC) và Kỹ thuật cầu  cân bằng
		Để xử lý tín hiệu từ cảm biến thành tín hiệu chuẩn, cần sử dụng các mạch điện tử. Một trong những mạch quan trọng nhất là mạch cầu. Có rất nhiều loại cảm biến sử dụng mạch cầu để làm bộ chuyển đổi (Variable conversion element). Có thể ví dụ như các cảm biến lực dạng load cell, cảm biến áp suất, cảm biến nhiệt độ theo nguyên lý thay đổi điện trở. Mạch cầu có thể được phân loại theo một số cách như theo nguồn cấp như mạch cầu DC và mạch cầu AC hoặc theo phương pháp đo điện áp đầu ra như mạch cầu cân bằng (balanced bridge) và mạch cầu không cân bằng. Trong mạch cầu không cân bằng, điện áp đầu ra được đo trực tiếp bằng vôn kế.Trong mạch cầu cân bằng, các phần tử được điều chỉnh cho đến khi điện áp đầu ra bằng 0.
4.3.1 Mạch cầu DC
Mạch cầu DC được sử dụng cho các cảm biến có sự thay đổi điện trở và có cấu hình bao gồm một điện trở tham chiếu mắc nối tiếp với điện trở cần đo là cảm biến. Trong mạch DC không có thành phần điện dung hoặc điện cảm. Mạch cầu hoạt động như một chuyển đổi sự thay đổi nhỏ của điện trở thành điện áp nhỏ gây ra bởi sự thay đổi của dòng điện khi điện trở thay đổi. Điện áp này thường cần được khuếch đại thêm bằng bộ khuếch đại DC.
4.3.2 Mạch cầu Wheatstone
Mạch cầu Wheatstone được cấu tạo bởi bốn điện trở R1, R2, R3 và R4 (trong đó một hoặc nhiều điện trở có thể là cảm biến) và được cấp nguồn điện áp  $$V$$ . Điện áp đầu ra:  $$V_{0}$$  thường nối với vôn kế hoặc mạch xử lý (khuếch đại DC, instrumentation amplifier). Điện trở nguồn  $$R_{i}$$ thường rất nhỏ so với  $$R_{1}$$ đến  $$R_{4}$$ , nên có thể bỏ qua trong tính toán đơn giản (Hình 4.9).

![Image](../../figures/lectures/Chương 4_rId15.png)

                                 Hình 4.9. Cấu hình mạch cầu Wheatstone
Áp dụng định lý Thevenin, ta có thể thay thế mạch bằng một nguồn điện áp  $$V_{0}$$  nối tiếp với điện trở tương đương  $$R_{k}$$ . Điện áp tại các nút:
                                                            $$V_{c}=\frac{R_{1}}{R_{1}+R_{2}}⋅V$$                                                                $$V_{d}=\frac{R_{3}}{R_{3}+R_{4}}⋅V$$                             (4.25)  Ta có điện áp đầu ra: 
                                                            $$V_{0}=V_{c}-V_{d}$$                                                       $$V_{0}=\frac{R_{1}}{R_{1}+R_{2}}⋅V-\frac{R_{3}}{R_{3}+R_{4}}⋅V$$  (4.26)  
Điện trở tương đương Thevenin khi ngắn mạch nguồn điện áp và hở mạch nguồn dòng, ta thu được:
                                                     $$R_{k}=\frac{R_{3}R_{4}}{R_{3}+R_{4}}+\frac{R_{1}R_{2}}{R_{1}+R_{2}}$$  (4.27)  
Dòng điện đầu ra khi nối với vôn kế có điện trở trong  $$R_{v}$$ :
                                                          $$I=\frac{V_{0}}{R_{k}+R_{v}}$$  (4.28)  
Khai triển:
                          $$I=\frac{V(R_{2}R_{3}-R_{1}R_{4})}{R_{1}R_{2}(R_{3}+R_{4})+R_{3}R_{4}(R_{1}+R_{2})+R_{v}(R_{1}+R_{2})(R_{3}+R_{4})}$$  (4.29)  Trường hợp mạch cầu cân bằng sẽ thỏa mãn điều kiện I=0 và ngược lại nếu mạch cầu không cân bằng thì dòng điện I khác 0. 
4.3.3 Mạch cầu một phần tư (Quarter-bridge)
Mạch cầu ¼  là mạch cầu Wheatstone trong đó có 1 điện trở biến thiên có thể là một cảm biến và các điện trở còn lại là là cố định. Thông thường, ta chọn:
                                 $$R_{1}=R_{2}=R_{3}=R_{4}=R_{0}$$  (4.30)  
Điện trở cảm biến có giá trị danh định là  $$R_{0}$$ , và thay đổi:
                                               $$R=R_{0}±ΔR$$    (4.30)  


Mạch cầu 1/4 được minh họa trong Hình 2.8. Dòng điện đầu ra của mạch cầu:

$$
I=\frac{V⋅R_{0}R_{0}-(R_{0}±ΔR)⋅R_{0}}{\left(R_{0}±ΔR)R_{0}(R_{0}+R_{0})+R_{0}R_{0}((R_{0}±ΔR)+R_{0})+R_{v}((R_{0}±ΔR)+R_{0})(R_{0}+R_{0}\right)}(2.10)
$$

Biểu thức trên là phi tuyến theo  $$ΔR$$  điện áp và dòng đo được còn phụ thuộc vào điện trở trong của vôn kế  $$R_{v}$$ .
Quan hệ giữa điện áp đầu ra và  $$ΔR$$  là phi tuyến (non-linear). Xấp xỉ tuyến tính đạt được (khi biến thiên nhỏ) Với:

$$
ΔR≪R_{0}
$$

Ta có thể đơn giản hóa:
                                               $$I=\frac{V}{4(R_{v}+R_{0})}⋅\frac{±ΔR}{R_{0}}$$    $$(4.31)$$ Độ nhạy dòng (Current Sensitivity)
Độ nhạy của dòng theo sự thay đổi điện trở:  
                               $$ S_{I}=\frac{∂I}{∂(ΔR/R_{0})}=\frac{V}{4(R_{v}+R_{0})}$$     $$(4.32)$$ Điện áp đầu ra

$$
V_{CD}=R_{v}⋅I=R_{v}⋅\frac{V}{4(R_{v}+R_{0})}⋅\frac{±ΔR}{R_{0}}(4.33)
$$

Độ nhạy điện áp (Voltage Sensitivity)

$$
S_{V}=\frac{∂V_{CD}}{∂(ΔR/R_{0})}=R_{v}⋅\frac{V}{4(R_{v}+R_{0})}(4.34)
$$

4.4. Mạch Logarit, mạch lọc, và khuếch đại Lock-in 
Mạch khuếch đại logarit là một mạch điện tử đặc biệt có khả năng biến đổi tín hiệu đầu vào theo quy luật logarit, thay vì tuyến tính như các mạch khuếch đại thông thường. Nói đơn giản, khi điện áp đầu vào tăng theo cấp số nhân thì điện áp đầu ra chỉ tăng theo cấp số cộng. Điều này rất hữu ích trong những hệ thống cần nén dải động rộng, chẳng hạn như xử lý tín hiệu âm thanh, đo lường tín hiệu rất nhỏ hoặc trong các thiết bị cảm biến.
Nguyên lý hoạt động của mạch dựa trên đặc tính phi tuyến của các linh kiện bán dẫn, phổ biến nhất là diode hoặc transistor. Khi một diode được phân cực thuận, dòng điện qua nó có quan hệ logarit với điện áp. Bằng cách đặt diode trong vòng phản hồi của một op-amp, người ta có thể “khai thác” đặc tính này để tạo ra đầu ra tỷ lệ với logarit của đầu vào. Kết quả là một mạch vừa ổn định nhờ op-amp, vừa mang đặc tính nén tín hiệu nhờ diode.

![Image](../../figures/lectures/Chương 4_rId16.png)

Hình 4.10. Sơ đồ nguyên lý của mạch khuếch đại Logarit 
Trong thực tế, mạch khuếch đại logarit thường xuất hiện trong các thiết bị đo công suất tín hiệu RF, máy đo decibel, hay các hệ thống xử lý âm thanh chuyên nghiệp. Ví dụ, tai người cảm nhận âm thanh gần với thang logarit, nên việc xử lý tín hiệu theo kiểu này giúp âm thanh nghe tự nhiên hơn. Ngoài ra, trong các hệ thống đo lường, mạch logarit cho phép hiển thị các giá trị rất lớn và rất nhỏ trên cùng một thang đo mà vẫn dễ quan sát.
Tuy nhiên, thiết kế mạch này không đơn giản. Đặc tính của diode phụ thuộc mạnh vào nhiệt độ, nên nếu không có biện pháp bù nhiệt, kết quả có thể sai lệch đáng kể. Vì vậy, các mạch thực tế thường sử dụng cặp transistor ghép đôi hoặc IC chuyên dụng để tăng độ chính xác và ổn định.
	Tóm lại, mạch khuếch đại logarit là một công cụ mạnh trong điện tử, cho phép xử lý tín hiệu theo cách phù hợp hơn với nhiều hiện tượng tự nhiên và nhu cầu kỹ thuật, đặc biệt khi phải làm việc với dải tín hiệu rộng. Do op-amp lý tưởng nên  $$V_{-}≈V_{+}=0$$    (đất ảo). Dòng qua điện trở sẽ có dạng:
                                                       $$I=\frac{V_{in}}{R}$$   (4.35)
Ta có dòng diode có dạng:
                                          $$I=I_{s}\left(e^{\frac{V_{D}}{nV_{T}}}−1\right)$$       (4.36)
Với:  $$I_{s}$$  là dòng bão hòa,  $$V_{T}≈26mV$$ ,  $$n≈1∼2$$ . Vì  $$I≫I_{s}$$ , ta xấp xỉ:
                                                  $$I≈I_{s}e^{\frac{V_{D}}{nV_{T}}}$$    (4.37)
Do diode nằm trong hồi tiếp nên  $$V_{out}=-V_{D}$$ . Thay  $$I=\frac{V_{in}}{R}$$  ta có:
                                                 $$\frac{V_{in}}{R}=I_{s}e^{\frac{-V_{out}}{nV_{T}}}$$   (4.38)
Lấy logarit phương trình trên ta thu được:
                                              $$ ln⁡\left(\frac{V_{in}}{RI_{s}}\right)=\frac{-V_{out}}{nV_{T}}$$    (4.39)
Từ phương trình trên ta được:
                                              $$V_{out}=-nV_{T}ln⁡\left(\frac{V_{in}}{RI_{s}}\right) $$  (4.40)

Từ công thức trên ta thấy đầu ra tỷ lệ với log của đầu vào, khi  $$V_{in}$$ tăng 10 lần →  $$V_{out}$$  chỉ tăng tuyến tính.

- 4.5. Mạch chuyển đổi Quang-Điện (Photodiode, Phototransistor)

