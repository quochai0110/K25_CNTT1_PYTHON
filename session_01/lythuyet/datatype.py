""" 

    Các kiểu dữ liệu trong python:
    1. int: số nguyên
    2. str: chuỗi
    3. float : số thực
    4. bool : kiểu đúng sai (True||False)
    ngoài ra còn có các kiểu dữ liệu: tuple, list, enum...

    Cách kiểm tra kiểu dữ liệu: type()
 """
#  int : số nguyên
#  khai báo tuổi của một sinh viên
age = 19
#  str: chuỗi
#  khai báo tên sinh viên
student_name ="Thu"
# float: kiểu số thực
#  khai báo điểm môn javascript của sinh viên
score = 6.5
#  bool : kiểu đúng sai 
#  khai báo biến kiểm tra xem sinh viên đã đăng nhập hay chưa?
is_login =True

print("kiểu dữ liệu của điểm số là: ",type(score))
print("kiểu dữ liệu của biến kiểm tra đăng nhập",type(is_login))

