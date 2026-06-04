students = [
    {
        "id":1,
        "name":"Minh Thu"
    },
      {
        "id":2,
        "name":"Lan Hồng"
    },
    {
        "id":3,
        "name":"Minh Phương"
    }
]
""" 
    cho người dùng nhập id:
    tìm kiếm sinh viên theo id vừa nhập
        + nếu không có hiển thị thông báo
        + nếu có hiển thị thông tin sinh viên vừa tìm thấy
 """

def search_student_id(id_student):      
    flag = 0

    for elm in students:
        if id_student == str(elm["id"]):
            flag = 1
            print(f"Thông tin sinh viên: {elm}")
            return
    if flag == 0:
        print("Không tìm thấy id người dùng")



input_id = input("Nhập id người dùng: ").strip()
while input_id == "":
    print("Id người dùng không được để trống!")
    input_id = input("Nhập id người dùng: ").strip()
search_student_id(input_id)