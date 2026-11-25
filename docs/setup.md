# Cài đặt Financial Modelling OS

## Claude Chat
1. Clone hoặc tải ZIP repository về máy, giải nén.
2. Tại thư mục repository, chạy `python scripts/manage_skills.py package` (có thể dùng `py` trên Windows).
3. Tải riêng `dist/financial-modelling.zip` lên Claude Customize > Skills nếu tài khoản hỗ trợ. Bật Skill và quyền tạo file khi phù hợp.
4. Nếu không có tính năng Skills, dùng file prompt v2 và SKILL.md trong Project Knowledge. Kết nối GitHub với Project không tự cài Skill; kiểm tra đồng bộ khi có thay đổi.

## Claude Code và Codex
- Mở terminal tại repository, cần Python 3.10+.
- Claude Code: `python scripts/manage_skills.py install --agent claude`.
- Codex: `python scripts/manage_skills.py install --agent codex`.
- Script sao chép skill vào thư mục cài đặt cục bộ và không tải mạng. Để thay thế bản đã cài, xem diff trước rồi thêm `--replace`.
- Kiểm tra agent có nhận diện Skill và quyền tạo, chỉnh sửa, tính lại file .xlsx.

## ChatGPT
- Nếu có tính năng upload Skills thì dùng ZIP riêng; nếu không, thêm prompt gốc và SKILL.md vào Project hoặc cung cấp trực tiếp cùng yêu cầu.
- Khả năng tạo, tính lại và kiểm tra workbook phụ thuộc công cụ được cấp quyền.

## Lệnh kiểm tra cấu trúc
`python scripts/manage_skills.py validate`

## Yêu cầu mẫu
Use the financial-modelling skill and my original financial modelling Excel prompt v2. Build a formula-driven, editable financial model using the attached case and data. Validate what can be tested, disclose limitations, and explain the findings in Vietnamese.

Không tải dữ liệu nhạy cảm lên dịch vụ chưa được phép. Chỉ xác nhận tính toán, render và validation thực sự đã chạy.
