""" 
Các phương thức làm việc với string
NHÓM ĐỊNH DẠNG 
1. upper(): viết hoa toàn bộ string
2. lower(): viết thường toàn bộ
3. title(): viết hoa chữ cái đầu tiên mỗi từ
4. capitalize(): viết hoa mình chữ cái đầu tiên

NHÓM TÌM KIẾM
1. find : nếu tìm thấy ra vị trí còn không thấy trả về -1
2. count
3. startWiths, endWiths

NHÓM CHỈNH SỬA
1. strip(): loại bỏ khoảng trắng đầu và cuối
2. lstrip(): loại bỏ ở đầu
3. replace(old, new): thay thế
4. split(): tách chuỗi

NHÓM KIỂM TRA DỮ LIỆU
isdigit(): kiểm tra có phải là số hay không?
isalpha(): kiểm tra có phải ký tự hay không?
isalnum(): kiểm tra cả 2 ký tự và số
isupper(): kiểm tra có phải viết hoa hay không?



 """
my_string = "python"
print(my_string.upper())
full_name ="lê minh thu"
print(full_name.lower())
print(full_name.title())
print("viết hoa mình chữ cái đầu tiên:",full_name.capitalize())
print("tìm kiếm xem trong string có tồn tại", full_name.find("minh"))



