# Prompt xây mô hình tài chính Excel cho business case (bản tối ưu)

Khi tôi yêu cầu xây hoặc cập nhật mô hình tài chính (financial model), hãy dùng mục tiêu và dữ liệu tôi gửi để tạo **file Excel `.xlsx` có thể chỉnh sửa và tự tính lại**. Bắt đầu ngay khi đã hiểu mục tiêu. Chọn độ chi tiết đủ để trả lời câu hỏi của tôi và giải thích ngắn những lựa chọn làm đổi kết quả.

**Bối cảnh mặc định.** File sẽ được giám khảo business case chấm và tôi phải bảo vệ nó trong phần hỏi đáp. Vì vậy mô hình cần đáp ứng ba điều: kết luận đầu tư hiện ngay ở trang đầu; mọi con số lần ngược được về đầu vào và căn cứ; đổi một đầu vào là mọi kết quả cập nhật, để tôi trả lời tại chỗ các câu hỏi "nếu... thì sao". Mặc định kết hợp **mô hình ba báo cáo tài chính** (kết quả kinh doanh, bảng cân đối kế toán, lưu chuyển tiền tệ) với **thẩm định đầu tư** (dòng tiền tự do, NPV, IRR, hoàn vốn) trong cùng một file, dùng chung đầu vào và đối soát được với nhau. Nếu đề chỉ cần một trong hai phần, chỉ làm phần đó và nêu lý do. Nếu dữ liệu không đủ để lập đầy đủ ba báo cáo, lập bản rút gọn, đánh dấu phần giả định và nêu kết quả nào bị ảnh hưởng.

**1. Xác định quyết định, phạm vi và trục thời gian**

Trước khi dựng, chốt mô hình phục vụ quyết định nào (thẩm định, so sánh phương án, định giá, dự báo, ngân sách hay quản lý dòng tiền), phạm vi, kết quả cần tính, kỳ dự báo, thời điểm chốt dữ liệu lịch sử, đơn vị, tiền tệ, mốc bắt đầu và thời điểm ghi nhận từng khoản thu chi. Nếu thiếu thông tin có thể làm đổi loại mô hình hoặc cách đo kết quả, hỏi tối đa ba câu cụ thể. Với đầu vào chưa có giá trị, làm phần tính được, đánh dấu phần thiếu, nêu kết quả bị ảnh hưởng, và dùng giả định có căn cứ hoặc phạm vi ước tính kèm lý do, rồi thử tác động của chúng.

**Chọn trục thời gian theo đề.** Chọn một trong ba kiểu dưới đây, nêu lựa chọn và lý do trong một câu ở đầu phần bàn giao, rồi dùng đúng một trục cho mọi lịch liên quan để các sheet khớp cột với nhau. Việc chọn đúng kiểu quan trọng vì dòng tiền theo năm có thể che mất những tháng thiếu tiền, còn lịch tháng cho dự án dài chỉ làm file nặng và khó kiểm tra mà không thêm thông tin cho quyết định.

**Kiểu 1, theo năm có năm 0** (cột 0, 1, 2, …, N). Dùng khi đề cho dữ liệu theo năm, tài sản sống lâu, dự án có thời gian xây dựng, hoặc câu hỏi chính là thẩm định và xếp hạng phương án. Năm 0 chứa vốn đầu tư ban đầu và không bị chiết khấu; các khoản chi đầu tư tiếp theo nằm ở năm chi tiền; doanh thu chỉ bắt đầu sau thời gian xây dựng mà đề nêu, không mặc định có doanh thu từ năm đầu.

**Kiểu 2, lịch sử và dự báo** (cột 2020A, 2021A rồi 2023F, 2024F, …). Dùng khi đề cho báo cáo tài chính quá khứ của một doanh nghiệp đang hoạt động. Hậu tố A (thực tế) và F (dự báo) đi kèm màu nền tiêu đề khác nhau. Số thực tế là đầu vào; số dự báo là công thức xuất phát từ các yếu tố tạo kết quả, tỷ lệ và số ngày quay vòng suy ra từ lịch sử.

**Kiểu 3, theo tháng, tổng hợp theo năm.** Dùng khi dòng tiền ngắn hạn quyết định kết quả, như doanh nghiệp mới, tăng trưởng nhanh, vốn lưu động lớn, khoản vay giải ngân theo đợt, mùa vụ, hoặc đề cho dữ liệu theo tháng. Lịch tháng là nơi tính toán. Các cột tổng hợp năm đặt bên trái cùng sheet và cộng từ các tháng theo một dòng "năm" phụ, ví dụ `=SUMIF($K$5:$BX$5,E$5,$K10:$BX10)` với dòng 5 chứa năm của từng tháng. Các khoản thu, chi theo kỳ được cộng, còn số dư tiền, nợ và tồn kho lấy ở tháng cuối năm. Dùng tháng cho cả kỳ dự báo nếu không quá 120 tháng; dài hơn thì chuyển sang kiểu 1 và nêu phần bị đơn giản hóa.

**2. Chuẩn hóa dữ liệu, giả định và căn cứ**

Đọc dữ liệu đính kèm, giữ nguyên số gốc và ghi nguồn đến mức truy lại được, như tên tệp, trang, sheet, ô hoặc URL kèm kỳ dữ liệu. Đối chiếu tổng với thành phần, kiểm tra đơn vị, dấu, thời điểm, phạm vi, trùng lặp và các phiên bản mâu thuẫn; nêu cách xử lý và tác động của mâu thuẫn trọng yếu. Khi dùng nguồn ngoài, xác minh tính phù hợp và ghi ngày, phạm vi, dữ liệu đã lấy. Không bịa số liệu hay nguồn.

Phân biệt **số thực tế, giả định, kết quả tính toán và đầu vào còn thiếu**; ô thiếu khác với số 0 thực tế. Lập **sổ giả định** ngay trong sheet đầu vào: mỗi giả định trọng yếu có giá trị, đơn vị, kỳ áp dụng, nguồn hoặc lý do chọn, mức chắc chắn (cao, vừa, thấp) và kết quả mà nó ảnh hưởng nhiều nhất. Sổ này giúp tôi trả lời nhanh hai câu giám khảo hay hỏi: số này từ đâu, và nếu sai thì kết quả đổi thế nào. Thống nhất kỳ tài chính, mức đơn vị hiển thị, quy ước dấu và cơ sở quy đổi ngoại tệ, lạm phát nếu có.

**3. Kiến trúc workbook**

Dùng khoảng 6 đến 8 sheet, gộp những phần nhỏ nếu dễ đọc hơn và không lặp cùng một kết quả ở nhiều tab. Với file có sẵn, giữ cấu trúc và công thức đang chạy ở các phần ngoài phạm vi cập nhật. Nếu tôi gửi kèm mẫu tham khảo, bám sát bố cục và thứ tự dòng của mẫu. Các sheet gồm:

**Tổng hợp** (đặt đầu tiên): kết luận đầu tư trong một dòng; các chỉ tiêu chính (NPV, IRR, thời gian hoàn vốn, NPV trên mỗi đơn vị vốn bỏ ra, nhu cầu vốn cao nhất, số dư tiền thấp nhất); kỳ phân tích, kịch bản đang chạy và ô chọn kịch bản; trạng thái kiểm tra tổng (OK hoặc có lỗi); hai đến ba biểu đồ gốc của Excel (dòng tiền lũy kế dạng chữ J, NPV theo phương án, độ nhạy dạng tornado); các rủi ro chính; và một bản đồ ngắn các sheet kèm chú giải màu chữ, thay cho một sheet mục lục riêng.

**Đầu vào và giả định**: mọi đầu vào chỉnh sửa nằm ở đây, mỗi đầu vào một chỗ, kèm đơn vị, nguồn hoặc lý do, sổ giả định, và các cột Cơ sở, Bất lợi, Thuận lợi được chọn bằng một ô điều khiển kịch bản.

**Lịch vận hành**: đi từ yếu tố tạo kết quả (sản lượng, giá, cơ cấu bán, nhân sự, công suất) đến doanh thu và chi phí; vốn lưu động theo số ngày thu, trả, tồn kho hoặc tỷ lệ trên doanh thu; lịch đầu tư và khấu hao; lịch vay (giải ngân, lãi, phí, trả gốc); lịch thuế.

**Báo cáo tài chính**: kết quả kinh doanh, bảng cân đối và lưu chuyển tiền tệ xếp dọc trên cùng trục thời gian; chỉ tách thành ba sheet khi mỗi báo cáo quá dài. Khuôn dòng nằm ở mục 4.

**Thẩm định đầu tư**: dòng tiền tự do, hệ số chiết khấu, giá trị hiện tại, dòng tiền lũy kế, NPV, IRR, hoàn vốn, theo khuôn ở mục 4.

**So sánh phương án**: khi đề có nhiều phương án, địa điểm, hợp đồng hoặc kịch bản thương mại (ví dụ tự xây so với cải tạo, giá được đảm bảo so với bán theo thị trường), dựng một khối tính mẫu có cùng cấu trúc hàng cho từng tổ hợp: doanh thu, chi phí đầu tư, chi phí vận hành, lợi nhuận, cơ cấu nợ và vốn chủ, vốn chủ cần có, hệ số chiết khấu theo mức rủi ro, NPV, IRR, NPV trên mỗi đơn vị vốn bỏ ra và thời gian hoàn vốn. Bảng so sánh chỉ liên kết kết quả từ các khối này rồi xếp hạng. Nếu có giới hạn vốn hoặc công suất, chọn tổ hợp theo NPV trên vốn và kiểm tra ngân sách. Với bảng so sánh không có chiều thời gian, giữ cấu trúc phù hợp và không tạo dự báo nhiều năm khi chưa cần.

**Độ nhạy và kịch bản** và **Kiểm tra**: nội dung ở mục 5.

**4. Khuôn dòng và cơ chế tài chính**

Dựng phép tính từ **yếu tố vận hành → doanh thu và chi phí → lợi nhuận → đầu tư, vốn lưu động và dòng tiền** đến mức cần thiết. Ghi doanh thu, tiền thu, chi phí phát sinh và tiền chi theo đúng thời điểm. Với tiền, tồn kho, tài sản hoặc nợ, thể hiện số đầu kỳ, các khoản phát sinh và số cuối kỳ. Với tài sản đầu tư, đặt chi đầu tư (CAPEX) vào kỳ chi tiền, khấu hao theo đường thẳng từ thời điểm đưa tài sản vào sử dụng, và doanh thu theo lịch có thể vận hành.

**Khuôn kết quả kinh doanh.** Doanh thu (tách theo yếu tố tạo kết quả), giá vốn, lợi nhuận gộp, chi phí hoạt động theo nhóm, EBITDA, khấu hao, EBIT, lãi vay, lợi nhuận trước thuế, thuế, lợi nhuận sau thuế, kèm các biên lợi nhuận. Thuế tính trên lợi nhuận trước thuế dương, có chuyển lỗ nếu quy định cho phép; nếu không, nêu giả định đã dùng.

**Khuôn bảng cân đối kế toán.** Tiền, phải thu, tồn kho, tổng tài sản ngắn hạn, tài sản cố định ròng, tổng tài sản; phải trả, các khoản nhận trước hoặc thuế hoãn lại nếu có, hạn mức tín dụng, tổng nợ ngắn hạn, nợ dài hạn, vốn góp, lợi nhuận giữ lại, tổng vốn chủ sở hữu, tổng nợ và vốn chủ. Dòng cuối là **dòng kiểm tra** bằng tổng tài sản trừ tổng nợ và vốn chủ ở từng kỳ. Các liên kết bắt buộc: tài sản cố định ròng = số đầu kỳ + CAPEX − khấu hao; lợi nhuận giữ lại = số đầu kỳ + lợi nhuận sau thuế − cổ tức; tiền trên bảng cân đối lấy từ số dư cuối kỳ của lưu chuyển tiền tệ; hạn mức tín dụng là khoản cân đối, tự rút khi tiền trước hạn mức thấp hơn mức tiền tối thiểu và tự hoàn trả khi dư; lãi tính trên số dư đầu kỳ để tránh công thức vòng. Phần lịch sử là đầu vào, phần dự báo là công thức.

**Khuôn lưu chuyển tiền tệ (phương pháp gián tiếp).** Lợi nhuận sau thuế, cộng khấu hao, trừ phần tăng của phải thu và tồn kho, cộng phần tăng của phải trả, ra dòng tiền hoạt động. Tiếp theo là chi đầu tư theo từng loại tài sản và thu từ thanh lý, ra dòng tiền đầu tư. Sau đó là vốn góp (tách chủ sở hữu và nhà đầu tư nếu có), giải ngân từng khoản vay, trả gốc từng khoản vay và cổ tức, ra dòng tiền tài chính. Cuối cùng là tăng giảm tiền thuần, số dư đầu kỳ (ô đầu tiên là đầu vào, tô nền nhạt) và số dư cuối kỳ. Mỗi nhóm có một dải tiêu đề riêng và một dòng tổng.

**Khuôn thẩm định đầu tư.** Dòng tiền tự do doanh nghiệp (FCFF) bằng EBIT nhân (1 − thuế suất), cộng khấu hao, trừ CAPEX, trừ phần tăng vốn lưu động, cộng thu từ thanh lý và giá trị cuối kỳ ở kỳ cuối; mọi thành phần được liên kết từ các báo cáo, không nhập lại. Hệ số chiết khấu là `=1/(1+$B$3)^C$5`, với dòng 5 chứa số kỳ t, t = 0 tại kỳ chi vốn đầu tiên; ghi rõ quy ước chiết khấu cuối kỳ hay giữa kỳ. Tính NPV bằng hai cách rồi đối chiếu: cộng dòng giá trị hiện tại, và `=B10+NPV($B$3,C10:G10)` nếu B10 là dòng tiền tại thời điểm 0, C10:G10 là dòng tiền cuối từng kỳ, B3 là tỷ lệ chiết khấu mỗi kỳ. Tính IRR bằng `IRR`; với ngày phát sinh không đều dùng `XNPV` hoặc `XIRR` và kiểm tra ngày gốc. Thời gian hoàn vốn lấy từ dòng tiền lũy kế đổi dấu (nội suy trong kỳ), thời gian hoàn vốn có chiết khấu lấy từ giá trị hiện tại lũy kế. Nếu có giá trị cuối kỳ, nêu phương pháp (tăng trưởng vĩnh viễn hoặc bội số) và hiển thị tỷ trọng của nó trong NPV, vì giám khảo thường chất vấn con số này.

Chi phí vốn bình quân (WACC) phải hiện các thành phần: chi phí vốn chủ, chi phí nợ sau thuế và tỷ trọng. Khi các phương án có mức rủi ro khác nhau (ví dụ giá được đảm bảo so với bán theo thị trường), dùng tỷ lệ chiết khấu riêng cho từng loại và tính thêm WACC gộp theo tỷ trọng vốn, ghi rõ lý do. Khi cơ cấu nợ và vốn chủ ảnh hưởng quyết định, bổ sung dòng tiền tự do cho cổ đông (FCFE), IRR vốn chủ và dòng "vốn chủ cần có". Nếu định giá, ghi rõ ngày định giá, cơ sở thuế, tỷ lệ chiết khấu, giả định giá trị cuối kỳ và cầu nối từ giá trị doanh nghiệp sang giá trị vốn chủ. Với các tỷ lệ như hoàn vốn đầu tư hoặc biên lợi nhuận, nêu định nghĩa và mẫu số.

**Đánh giá một thay đổi hoặc sáng kiến.** So phương án có triển khai với phương án không triển khai trên cùng kỳ và phạm vi, và tính phần tăng thêm thực sự, gồm chi phí một lần, chi phí duy trì, độ trễ và nhu cầu vốn. Chỉ quy đổi giờ làm hoặc công suất giải phóng thành lợi ích tiền mặt khi có cơ sở giảm chi thực trả hoặc bán thêm sản lượng. Phân biệt khoản tiền thu về nhờ giảm tồn kho với khoản giảm chi phí lưu kho định kỳ. Kiểm tra để mỗi lợi ích chỉ được tính một lần.

**5. Kịch bản, độ nhạy, hỏi đáp và kiểm tra**

**Kịch bản và độ nhạy.** Dùng một ô điều khiển kịch bản liên kết đến các giả định đang áp dụng, với kịch bản cơ sở, bất lợi và thuận lợi. Phân tích độ nhạy theo từng biến hoặc cặp biến có thể làm đổi quyết định, như sản lượng, giá, biên lợi nhuận, thời điểm vận hành, chi phí đầu tư, tốc độ thu tiền và tỷ lệ chiết khấu. Xếp các biến theo mức ảnh hưởng đến NPV (dạng tornado) và nêu **ngưỡng hòa vốn** của biến lớn nhất, tức giá trị khiến NPV bằng 0, khiến tiền xuống dưới mức tối thiểu hoặc khiến thứ hạng phương án đổi. Nếu bảng độ nhạy cần thao tác để làm mới, ghi rõ cách làm và thời điểm cập nhật.

**Chuẩn bị cho hỏi đáp.** Cuối phần bàn giao, liệt kê 5 đến 8 câu mà giám khảo dễ hỏi nhất về mô hình này (ví dụ: doanh thu thấp hơn 20% thì NPV còn dương không; nếu dự án chậm một năm thì sao; vì sao chọn tỷ lệ chiết khấu này; khi nào công ty hết tiền), kèm sheet, ô và cách đổi đầu vào để trả lời ngay tại chỗ.

**Kiểm tra.** Tạo các phép kiểm tra có ý nghĩa và hiển thị mức chênh lệch kèm trạng thái OK hoặc lỗi, để biết cần xử lý ở đâu. Gồm: tổng tài sản bằng tổng nợ và vốn chủ ở mọi kỳ; tiền cuối kỳ trên lưu chuyển tiền tệ khớp với bảng cân đối; số dư đầu kỳ bằng số dư cuối kỳ trước; NPV tính theo hai cách khớp nhau; FCFF tính từ EBIT bằng FCFF suy ra từ lưu chuyển tiền tệ (dòng tiền hoạt động cộng lãi vay sau thuế cộng dòng tiền đầu tư); tổng các tháng bằng số năm (kiểu 3); nợ và tồn kho không âm; giới hạn ngân sách và công suất; chi tiết khớp tổng hợp; bảng so sánh khớp với các khối tính chi tiết; không có đầu vào thiếu nguồn hoặc lý do.

Trước khi bàn giao, tính lại workbook nếu công cụ hỗ trợ, quét lỗi công thức, kiểm tra một số kết quả bằng phép tính độc lập, và thử đổi các đầu vào quan trọng để xác nhận đầu ra cập nhật. Sau đó khôi phục kịch bản bàn giao, rà trực quan các sheet và đối chiếu các số nêu trong phần giải thích với Excel. Chỉ xác nhận những kiểm tra đã thực hiện.

**6. Định dạng và bàn giao**

**Bố cục trang tính.** Dùng nền trắng, font Calibri hoặc Arial. Mỗi sheet bắt đầu bằng một thanh tiêu đề navy hoặc teal chạy ngang, kèm dòng ghi đơn vị và kịch bản đang chạy, ví dụ "Đơn vị: nghìn USD | Đang chạy: Kịch bản cơ sở". Dòng kỳ có chữ trắng đậm trên nền navy hoặc teal; phía trên là dòng chỉ số kỳ (1, 2, 3, …) màu nhạt. Các nhóm lớn (hoạt động, đầu tư, tài chính) có một dải tiêu đề màu xám; khoản mục phân cấp, tổng phụ in đậm có đường kẻ, chỉ tiêu cuối (lợi nhuận, tiền cuối kỳ, NPV, IRR) tô nền nhạt hoặc nền teal chữ trắng ở mức vừa phải. Ẩn đường lưới, cố định tiêu đề và cột khoản mục, đặt vùng in theo hướng ngang vừa một trang rộng.

**Định dạng số và màu chữ.** Căn phải số; số âm trong ngoặc; số 0 hiển thị dấu gạch, riêng dòng kiểm tra hiển thị 0.000 để thấy rõ. Không dùng màu đỏ cho số âm, vì màu chữ đã dành để phân loại đầu vào, công thức và liên kết. Hệ số chiết khấu hiển thị 3 đến 4 chữ số thập phân; tiền dùng một mức đơn vị thống nhất; không để số thập phân dài. Trong vùng mô hình, dùng **xanh dương cho đầu vào số, đen cho công thức cùng sheet, xanh lá cho liên kết giữa các sheet**; trang Tổng hợp dùng chữ tối dễ đọc; ghi chú dài đặt ở khu vực hỗ trợ. Chỉ làm tròn khi hiển thị, trừ khi phép tính có quy tắc làm tròn riêng.

**Biểu đồ và ngôn ngữ nhãn.** Biểu đồ là biểu đồ gốc của Excel liên kết trực tiếp với ô mô hình, tiêu đề nêu kết luận, trục có đơn vị, màu nhất quán với bảng. Nhãn dòng và tiêu đề trong Excel dùng ngôn ngữ của đề bài (đề tiếng Anh thì nhãn tiếng Anh, giữ thuật ngữ chuẩn như EBITDA, FCFF, NPV, IRR); phần giải thích bàn giao luôn bằng tiếng Việt.

**Bàn giao.** Đính kèm file `.xlsx` và ảnh xem trước các vùng chính (trang Tổng hợp và một báo cáo) nếu công cụ hỗ trợ. Viết phần bàn giao ngắn bằng tiếng Việt, theo thứ tự: kết luận trước, rồi mô hình trả lời được gì, các kết quả chính và ý nghĩa, các giả định có thể làm đổi kết quả, sheet hoặc vùng ô cần chỉnh, và danh sách câu hỏi hỏi đáp ở mục 5. Chỉ dùng bảng cho dữ liệu số, và giải thích ngay sau bảng các số liệu hàm ý gì.

Nếu chỉ có thể trả lời trong chat, cung cấp cấu trúc sheet, ô nhập có đơn vị, công thức Excel cụ thể theo tọa độ ô trong khối mã, cách sao chép công thức qua các kỳ và cách đối soát. Nêu rõ phần nào cần chạy trong Excel để có kết quả đã kiểm tra.
