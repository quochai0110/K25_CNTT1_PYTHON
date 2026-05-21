""" 
    1. break dùng để thoát vòng lặp.
    2. viết code sau break không có ý nghĩa.
    3. ví dụ
        Muốn tạo game đoán số.
        Tạo mặc định 1 số từ 1_10
        Sau đó cho người dùng nhập 1 số bất kì
            + Nếu số người nhập trùng với số ban đầu thì in ra bạn đã chiến thắng
            + Nếu sai cho người dùng nhập 


 """
secret =5
while True :
    number = int(input("mời nhập số bạn dự đoán"))
    if number == secret:
        print("bạn đã chọn đúng và chiến thắng!")
        break
    print("bạn chọn sai rồi, mời chọn lại!")