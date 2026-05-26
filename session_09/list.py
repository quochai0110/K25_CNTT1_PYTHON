""" 
    LIST: DANH SÁCH:
    1. CÔNG DỤNG: gom các phần tử thường cùng kiểu dữ liệu để:
    quản lý, thao tác, đỡ tốn bộ nhớ
    2. Các thao tác làm việc với list
        2.1 : tạo mới list
        TEN_DANHSACH = []  _ thường dùng
        TEN_DANHSACH = list()
        2.2: thêm phần tử
            + append(value): thêm phần tử vào cuối mảng
            + insert(index, value): 
        2.3: sửa phần tử
            + sửa theo vị trí (index)
        2.4: xóa phần tử
            + remove(value):
            + pop (): xóa phần tử cuối cùng
            + del() : xóa phần tử theo index
    3. Duyệt danh sách (list)
        

            

 """
#  TẠO DANH SÁCH QUẢN LÝ SINH VIÊN
students = []
students.append("Bình")
students.append("Đức")
students.insert(1,"Mạnh")
students[0] = "Bảo"
students.append("Đức")
students.remove("Đức")
students.pop()

print("danh sách sinh viên CNTT1",students)
