""" 

    Các nội dung trong bài học
    1. string, index, immutable
    2. clice(cắt chuỗi) và các toán tử làm việc với string
    3. method (các phương thức làm việc với string)
    4. format (định dạng string)

 """
#  string là gì? đây là chuỗi dùng để khai text
my_string = "python" 
#            012345
new_text ='python basic'


print("'python basic'")
#  index : chỉ mục , bắt đầu =0
print("lấy kí tự có chỉ số:",my_string[-5])
# immutable : bất biến 
# một biến khi khai báo string thì không thay đổi được giá trị
# new_text[0] ="T"
# Tython basic
print("T"+new_text[1:])

