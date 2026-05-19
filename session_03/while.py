""" 
Khi nào dùng while?
Khi chương trình không biết trước số lần lặp:
    + Khi người dùng nhập mật khẩu
    + Trong các bài toán menu chọn chức năng
        1. chức năng A
        2. chức năng B
        3. Thoát
CÚ PHÁP WHILE
WHILE condition :
    code
    --> kiểm tra điều kiện 
        + nếu điều kiện đúng thì chạy tiếp
        + nếu sai thoát vòng lặp
NOTE: tránh trường hợp vòng lặp vô tận.

 """
#  in các số từ 1-15
count =1
while count <=15:
    print(count)
    # count = count + 1
    count +=1
""" 
    THẦY CÓ THẺ CÀO ĐIỆN THOẠI VINAPHONE MỆNH GIÁ 50.OOO Đ
    CHO NGƯỜI NHẬP 3 LẦN
        + NẾU NHẬP ĐÚNG THÔNG BÁO TÀI KHOẢN + 50.000
        + NẾU NHẬP SAI CHO NHẬP LẠI
    MÃ THẺ CÀO : CARD = "12345"

 """
code = "12345"
attempt = 0
while attempt < 3:
    user_input = input("Nhập mã thẻ cào: ")
    if code == user_input:
        print("Có Tiền")
        attempt = 3
    else:
        attempt += 1
        print(f'Bạn còn {3 -attempt} lần nhập')


""" 
    ví dụ viết chương trình dạng người dùng chọn menu
    Viết chương trình quản lý sinh viên gồm các chức năng sau
    1. xem danh sách sinh viên
    2. thêm sinh viên
    3. xóa sinh viên
    0. thoát
    
 """
fag = 1
while fag ==1:
    print("1. xem ds, 2. thêm sinh viên, 3 xóa sinh viên")
    choose = int(input("mời nhập lựa chọn"))
    if choose==1:
        print("danh sách sinh viên là:")
    elif choose ==2:
        print("tiến hành thêm sinh viên")
    elif choose ==3:
        print("tiến hành xóa")
    elif choose==0:
        print("thoát")
        fag =2
    else:
        print("lựa chọn không hợp lệ ")


    
