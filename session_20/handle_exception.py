""" 

    XỬ LÝ NGOẠI LỆ

 """
try:
    #  đoạn code xử lý
    pass
    # nếu bỏ else đi viết code trong này
except:
    pass
    # cảnh báo lỗi
else:
    pass
finally:
    # bug hay không bug đều chạy
    #  thường dùng xử lý file, dọn dẹp bộ nhớ
    pass

#  cho người dùng nhập vào số nguyên bất kì, kiểm tra xem số chẵn hay lẻ

try:
    number = int(input("mời bạn nhập số cần kiểm tra: "))
except:
    print("không phải là số nguyên")
else:
    if number%2 == 0:
        print("là số chẵn")
    else:
        print("là số lẻ")

