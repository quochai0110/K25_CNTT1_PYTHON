""" 
input: dữ liệu đầu vào
    - dùng hàm input để cho người dùng nhập dữ liệu
output: dữ liệu đầu ra 
    - dùng hàm print để hiển thị

- dùng f_string để hiển thị theo format
 """

# viết chương trình yêu cầu người dùng nhập tuổi
age = input("mời nhập tuổi")
print("tuổi của bạn là", age)
print("kiểu dữ liệu của tuổi là", type(age))
student_name ="Hồng Vân"

# xin chào Hồng Vân năm nay 18 tuổi
# print("Xin Chào",student_name,"năm nay",age,"tuổi")
print(f"Xin chào {student_name} năm nay {age} tuổi")
