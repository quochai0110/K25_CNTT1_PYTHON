""" 
Các bước làm:
B1: Khai báo các biến chứa thông tin bệnh nhân
B2: Cho người dùng nhập và ép kiểu dữ liệu tương ứng
B3: Hiển thị theo yêu cầu
 """
import random
#  tên bệnh nhân
patient_name = input("mời nhập tên bệnh nhân")
#  giới tính
gender = input("mời nhập giới tính")
#  năm sinh
birth_year= int(input("mời nhập năm sinh"))
#  số điện thoại
phone_number= input("mời nhập số điện thoại")
#  email
email = input("mời nhập email")
#  triệu chứng ban đầu
initial_symptoms = input("mời nhập triệu chứng")
#  chi phí khám điều trị
examination_cost = float(input("nhập chi phí khám"))

# 3. Hiển thị theo yêu cầu:
#  Mã bệnh nhân: theo quy tắc: "BN" + năm sinh + 3 số ngẫu nhiên 
random_number = random.randint(100,999)
print("mã bệnh nhân là: ", "BN"+ str(birth_year)+ str(random_number))

