""" 
    NGÂN HÀNG ĐIỂM VÀ ĐỔI THƯỞNG

    INPUT:
        + LIST HỒ SƠ SINH VIÊN: []
        + 1 HỒ SƠ SINH VIÊN GỒM CÁC THUỘC TÍNH:
            {
                student_id : mã sinh viên
                current_points: điểm r_point hiện có
                spent_points: điểm đã tiêu
                refunded_point: điểm được hoàn trả do phúc khảo
                multiplier: hệ số nhân điểm thưởng
            }
    
    OUTPUT:
    THỰC HIỆN ĐẦY ĐỦ 6 CHỨC NĂNG
    TƯƠNG ỨNG CÁC CHỨC NĂNG
        1. HIỂN THỊ SAO KÊ ĐIỂM SỐ
            + Điểm hiện có < 500: "Cần tích lũy thêm "
            + 500 <= Điểm hiện có <= 1500: "Thành viên tiềm năng "
            + Điểm hiện có > 1500: "Thành viên ưu tú "
        6 CHỨC NĂNG
        1. Hiển thị sao kê điểm số
        2. Đổi điểm lấy phần thưởng
        3. Phúc khảo bài thi (Hoàn điểm)
        4. Kích hoạt (Hệ số nhân điểm)
        5. Chấm bài (thêm điểm)
        6. Thoát chương trình
 """
student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]
#  tạo hàm kiểm tra trạng thái
def check_status(student):
    print("kiểm tra trạng thái")
    if student["current_points"] <500:
        return "cần tích lũy thêm!"
    elif student["current_points"]<1500:
        return "Thành viên tiềm năng"
    else:
        return "Thành viên ưu tú"
# chức năng 1:  tạo hàm hiển thị danh sách hồ sơ
def  display_statements(records):
    for item in records:
        print(f"mã sinh viên: {item["student_id"]}")
        print(f"tên sinh viên: {item["name"]} ")
        print(f"điểm hiện có: {item["current_points"]}")
        print(f"điểm đã tiêu: {item["spent_points"]}")
        print(f"hoàn trả : {item["refunded_points"]}")
        print(f"hệ số: {item["multiplier"]}")
        print(f"trạng thái: {check_status(item)}")
#  tạo hàm kiểm tra sinh viên có tồn tại hay không
def find_student_by_id(students,id):
    for index, std in enumerate(students):
        if std["student_id"] == id:
            return index
    return -1
#  chức năng số 2: Đổi điểm lấy phần thưởng
def redeem_rewards(records):
    student_id= input("mời nhập mã sinh viên : ").strip().upper()
    index = find_student_by_id(student_records,student_id)
    if index== -1:
        print("sinh viên tồn tại!")
        return
    #  nhập số điểm cần tiêu
    try:
        spent_point = float(input("mời nhập số điểm cần tiêu")) 
        if spent_point < records[index]["current_points"]:
            print("đúng")
            records[index]["current_points"] -= spent_point
            records[index]["spent_points"] += spent_point
        else:
            print("điểm chi tiêu phải nhỏ hơn điểm hiện tại!") 
    except ValueError:
        print("thông báo lỗi")
#  chức năng số 3: phúc khảo bài thi
def appeal_score(records):
    """ 
     CÁC BƯỚC LÀM 
     B1: NHẬP MÃ SINH VIÊN, KIỂM TRA SINH VIÊN TỒN TẠI HAY KHÔNG?
     B2: NHẬP ĐIỂM CẦN HOÀN LẠI, KIỂM TRA SỐ ĐIỂM HOÀN KHÔNG ĐƯỢC VƯỢT QUÁ
     SỐ ĐIỂM ĐÃ TIÊU
     """
    student_id= input("mời nhập mã sinh viên : ").strip().upper()
    index = find_student_by_id(student_records,student_id)
    if index==-1:
        print("sinh viên không tồn tại!")
        return
    try:
        return_score = float(input("mời nhập điểm phúc khảo!"))
        if return_score <=0 or return_score> records[index]["spent_points"]:
            print("điểm hoàn trả không hợp lệ!")
            return
        records[index]["spent_points"]-= return_score
        records[index]["current_points"]+= return_score
    except ValueError:
        print("lỗi!")
#  chức năng 4:  activate_multiplier(records). 
def  activate_multiplier(records):
    """ 
     Nhập mã sinh viên
     kiểm tra sinh viên có tồn tại:
        + Nếu không có dừng chương trình hiển thị thông báo
        + Nếu có nhập hệ số nhân
            + kiểm tra hệ số nhân trong khoảng 1.0-3.0:
            + Nếu nhập sai dừng chương trình và hiển thị thông báo
            + Nhập đúng: kích hoạt nhân hệ số
     """
    student_id= input("mời nhập mã sinh viên : ").strip().upper()
    index = find_student_by_id(student_records,student_id)
    if index== -1:
        print("sinh viên không tồn tại!")
        return
    
    try:
        
        pass 
    except ValueError:
        print("lỗi!")
def main():
    while True:
        print("""
            HỆ THỐNG QUẢN LÝ ĐIỂM SỐ
            1. Hiển thị sao kê điểm số
            2. 
            6. Thoát
    """)
        choice = input("mời bạn nhập lựa chọn! ")
        if choice == "1":
            # thực hiện chức năng 1
            display_statements(student_records)
            print("chức năng 1")
        elif choice == "2":
            print("chức năng 2")
            redeem_rewards(student_records)
        elif choice =="3":
            print("chức năng 3")
            appeal_score()
        elif choice =="4":
            print("chức năng 4: Kích hoạt hệ số nhân điểm cho học viên trong các dịp lễ.  ")


        elif choice == "6":
            break
        else:
            print("lựa chọn không hợp lệ!")
main()
