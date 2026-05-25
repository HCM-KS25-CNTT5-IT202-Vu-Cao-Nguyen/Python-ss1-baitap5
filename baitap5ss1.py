#Thông tin bệnh nhân:
patient_name = input("Nhập tên bệnh nhân: ") #tên bệnh nhân
patient_code = input("Nhập mã bệnh nhân: ") #mã bệnh nhân
patient_age = input("Nhập tuổi bệnh nhân: ") #tuổi bệnh nhân

#Chỉ số tín hiệu của bệnh nhân
heart_rate = input("Nhập nhịp tim bệnh nhân: ") #nhịp tim bệnh nhân
body_temperation = input("Nhập nhiệt độ bệnh nhân: ") #nhiệt độ bệnh nhân
patient_weight = input("Cân nặng bệnh nhân: ") #cân nặng bệnh nhân

# Ép kiểu dữ liệu
patient_name = str(patient_name)
patient_code = str(patient_code)
patient_age = int(patient_age)
heart_rate = int(heart_rate)
body_temperation = float(body_temperation)
patient_weight = float(patient_weight)

# Hiển thị hồ sơ bệnh nhân
#1.Thông tin bệnh nhân
print(f"Tên bệnh nhân: {patient_name} - Tuổi bệnh nhân: {patient_age} - Mã bệnh nhân: {patient_code}")
#2.Chỉ số tín hiệu của bệnh nhân
print(f"Nhịp tim của bệnh nhân: {heart_rate} - Nhiệt độ của bệnh nhân: {body_temperation} - Cân nặng bệnh nhân: {patient_weight}")

#Kiểm tra kiểu dữ liệu
print(f"  patient_name      = {repr(patient_name):<25} | {type(patient_name)}")
print(f"  patient_code      = {repr(patient_code):<25} | {type(patient_code)}")
print(f"  patient_age       = {repr(patient_age):<25} | {type(patient_age)}")
print(f"  body_temperature  = {repr(body_temperation):<25} | {type(body_temperation)}")
print(f"  heart_rate        = {repr(heart_rate):<25} | {type(heart_rate)}")
print(f"  body_weight       = {repr(patient_weight):<25} | {type(patient_weight)}")
