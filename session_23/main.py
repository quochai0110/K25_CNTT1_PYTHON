""" 

    1. Module : 
        + Bản chất là các file.py bên trong các file đó sẽ chứa hàm, class, biến
        mục đích: dễ quản lý code, dễ bảo trì, có thể tái sử dụng được
    2. Import
    3. Package
        + đóng gói các module lại với nhau dễ quản lý code


 """
""" 
HỆ THỐNG QUẢN LÝ BÁN HÀNG
1. QUẢN LÝ USER
2. QUẢN LÝ SẢN PHẨM
3. QUẢN LÝ ĐƠN HÀNG
4. QUẢN LÝ BÌNH LUẬN SẢN PHẨM
--> CHIA THÀNH CÁC MODULE
 """
#  hiển thị full_name
from module_a.module_c.module_c import full_name, age
print("full_name", full_name)
print("age", age)

