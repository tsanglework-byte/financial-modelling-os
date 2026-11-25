# Financial Modelling OS

Hệ thống độc lập để xây dựng, cập nhật và kiểm tra mô hình tài chính Excel cho Business Case, thẩm định đầu tư, dự báo, định giá, ngân sách và dòng tiền.

## Nguồn tiêu chuẩn
[Prompt tài chính Excel v2 gốc](skills/financial-modelling/references/Prompt_Xay_Mo_Hinh_Tai_Chinh_Excel_v2.md) do người dùng cung cấp là tiêu chuẩn chính. [SKILL.md](skills/financial-modelling/SKILL.md) là hướng dẫn thực thi, không thay thế prompt.

## Bắt đầu
- Đọc [hướng dẫn cài đặt](docs/setup.md).
- Tạo ZIP Skill: `python scripts/manage_skills.py package`.
- Claude Code: `python scripts/manage_skills.py install --agent claude`.
- Codex: `python scripts/manage_skills.py install --agent codex`.
- Claude Chat hoặc ChatGPT: cài ZIP nếu nền tảng hỗ trợ, hoặc cung cấp prompt và tài liệu hướng dẫn trong Project.
- [Test cases](tests/evaluation-cases.md) là các bài kiểm thử đề xuất; chưa chạy benchmark tạo Excel trên các AI.

## Phạm vi
Mô hình ba báo cáo, FCFF/FCFE, NPV, IRR, WACC, hoàn vốn, so sánh phương án, kịch bản, độ nhạy, kiểm tra mô hình, định dạng Excel và chuẩn bị phản biện. Không có dữ liệu doanh nghiệp hay engine Excel độc lập được đóng gói.

Repository riêng tư, tách hoàn toàn khỏi Consulting Slide OS. Cài đặt Skills và đồng bộ GitHub là hai việc khác nhau. Không tự động tải hay đăng dữ liệu nhạy cảm.
