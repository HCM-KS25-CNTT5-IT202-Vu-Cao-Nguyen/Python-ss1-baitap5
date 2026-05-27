      
# (1) THIẾT KẾ KIẾN TRÚC & LUỒNG DỮ LIỆU
# 1. ĐỊNH NGHĨA 5 TRƯỜNG THÔNG TIN CẦN THU THẬP
# - Thông tin cá nhân: Họ tên bệnh nhân, Mã định danh (CCCD/BHYT).
# - Chỉ số sinh hiệu: Nhiệt độ cơ thể, Nhịp tim, Cân nặng.
# 2. BẢNG THIẾT KẾ DỮ LIỆU (DATA DICTIONARY)
# Tên biến (snake_case) | Nội dung input             | Kiểu dữ liệu mong muốn
# patient_name         | Họ và tên của bệnh nhân     | str
# patient_id           | Số CCCD hoặc mã thẻ BHYT    | str
# body_temperature     | Nhiệt độ cơ thể đo được     | float
# heart_rate           | Chỉ số nhịp tim hiện tại    | int
# body_weight          | Cân nặng hiện tại           | float
# 3. THIẾT KẾ LUỒNG CHƯƠNG TRÌNH (PSEUDOCODE)
# Begin
#   Hiển thị màn hình chào mừng (Banner chào đón Kiosk)
#   Thu thập dữ liệu (Input) qua các câu hỏi thân thiện:
#     Nhập patient_name (Dạng chuỗi)
#     Nhập patient_id (Dạng chuỗi ký tự số)
#     Nhập raw_temperature (Dạng chuỗi số thực)
#     Nhập raw_heart_rate (Dạng chuỗi số nguyên)
#     Nhập raw_weight (Dạng chuỗi số thực)
#   Xử lý ngầm (Type Casting):
#     body_temperature = Chuyển_đổi_sang_số_thực(raw_temperature)
#     heart_rate = Chuyển_đổi_sang_số_nguyên(raw_heart_rate)
#     body_weight = Chuyển_đổi_sang_số_thực(raw_weight)
#   Đầu ra (Output):
#     In "Phiếu Khám Bệnh Điện Tử" rõ ràng cho bệnh nhân di chuyển phòng khám
#     In "System Log" hiển thị kết quả kiểm tra kiểu dữ liệu cho bộ phận IT
# End
# 4. THIẾT KẾ CÂU HỎI INPUT() THÂN THIỆN (UX PROMPT)
# - Câu 1: input("Vui lòng nhập Họ và Tên của bạn (Ví dụ: NGUYEN VAN A): ")
# - Câu 2: input("Vui lòng nhập số CCCD hoặc mã thẻ BHYT (Ví dụ: 0123456789): ")
# - Câu 3: input("Vui lòng nhập nhiệt độ cơ thể hiện tại (Ví dụ: 36.5 - Sử dụng dấu chấm): ")
# - Câu 4: input("Vui lòng nhập chỉ số nhịp tim của bạn (Ví dụ: 80 - Chỉ nhập số): ")
# - Câu 5: input("Vui lòng nhập cân nặng hiện tại của bạn (Ví dụ: 60.2 - Sử dụng dấu chấm): ")

#  KHỞI TẠO HỆ THỐNG
hospital_name = 'BỆNH VIỆN ĐA KHOA "SỨC KHỎE VÀNG"'
kiosk_version = "v1.0.0 - Production"

print(f"Chào mừng quý khách đến với {hospital_name}")
print(f"HỆ THỐNG KIOSK KHAI BÁO Y TẾ TỰ ĐỘNG ({kiosk_version})")
print("Vui lòng làm theo hướng dẫn trên màn hình để hoàn thành thủ tục.")

# THU THẬP VÀ ÉP KIỂU TRỰC TIẾP
# 1. Thu thập và xử lý thông tin cá nhân
patient_name = input("1/5. Nhập Họ và Tên (Ví dụ: NGUYEN VAN A): ")
patient_id = input("2/5. Nhập số CCCD hoặc thẻ BHYT (Ví dụ: 0123456789): ")
# 2. Thu thập và ép kiểu trực tiếp chỉ số sinh hiệu (Inline Casting)
body_temperature = float(input("3/5. Nhập nhiệt độ cơ thể hiện tại (Ví dụ: 36.5 - Dùng dấu chấm): "))
heart_rate = int(input("4/5. Nhập nhịp tim đo được từ máy (Ví dụ: 80 - Chỉ nhập số nguyên): "))
body_weight = float(input("5/5. Nhập cân nặng hiện tại của bạn (Ví dụ: 62.5 - Dùng dấu chấm): "))

# HIỂN THỊ ĐẦU RA TÁCH BIỆT
# 1 PHIẾU KHÁM BỆNH ĐIỆF TỬ (Giao diện hiển thị trực quan cho Bệnh nhân & Bác sĩ)
print("\nPHIẾU KHÁM BỆNH ĐIỆN TỬ")
print(f"Bệnh nhân : {patient_name}")
print(f"Mã số     : {patient_id}")
print(f"CHỈ SỐ SINH HIỆU ĐO ĐƯỢC:")
print(f" * Nhiệt độ : {body_temperature} °C")
print(f" * Nhịp tim : {heart_rate} nhịp/phút")
print(f" * Cân nặng : {body_weight} kg")
print("Vui lòng cầm phiếu này di chuyển thẳng tới PHÒNG KHÁM LÂM SÀNG.")

# 2 LOG HỆ THỐNG (Giao diện giám sát dữ liệu dành cho bộ phận kỹ thuật IT)
print("\n[SYSTEM LOG - FOR IT DEPARTMENT ONLY]")
print(">>> Trạng thái chuẩn hóa dữ liệu đầu vào:")
print(f" - Biến 'patient_name'     : Kiểu dữ liệu hiện tại = {type(patient_name)}")
print(f" - Biến 'patient_id'       : Kiểu dữ liệu hiện tại = {type(patient_id)}")
print(f" - Biến 'body_temperature' : Kiểu dữ liệu hiện tại = {type(body_temperature)}")
print(f" - Biến 'heart_rate'       : Kiểu dữ liệu hiện tại = {type(heart_rate)}")
print(f" - Biến 'body_weight'      : Kiểu dữ liệu hiện tại = {type(body_weight)}")
print(">>> Kiểm tra cấu trúc: Hoàn thành chuẩn hóa (Data Type Validated).")
