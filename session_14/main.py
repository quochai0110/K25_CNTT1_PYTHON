""" 

    FUNCTION:
    1. Công dụng: bao gồm khối mã code có chức năng tối ưu code, dễ bảo trì
    (chỉnh sửa cập nhật ), có khả năng tái sử dụng (viết 1 lần gọi được nhiều
    lần.)
    2. Cách khai báo hàm
        + hàm không có tham số
        CÚ PHÁP: def function_name():
        GỌI HÀM: function_name()
        QUY TẮC ĐẶT TÊN: 
            + đặt tên bằng tiếng anh, đúng mục đích, quy tắc snake case
            + tránh đặt trùng tên với các từ khóa đặc biệt: (try, except)
            + thường bắt đầu bằng động từ 
        + hàm có tham số
        CÚ PHÁP: def function_name(param1,param2...):
            + THAM SỐ : PARAMETER _ khi khai báo hàm khai báo tham số bên trong
            dấu ()
            + ĐỐI SỐ : ARGUMENT _ khi gọi hàm truyền giá trị vào

        + hàm có giá trị trả về
        RETURN:
            + dừng chương trình, kết thúc hàm
            + trả về kết quả cho hàm

 """
def happy_birthday(name):
    print(f"chúc mừng sinh nhật {name}")
happy_birthday("Khánh")
happy_birthday("Nam")

#  hàm tính tổng 2 số
def sum(a,b):
    print(f"tổng 2 số a và b là: {a+b}")
sum(4,8)

#  hàm tính tổng dãy số 
#  tính tổng các số 1,2,3,4,5
def total (*numbers):
    print("dãy số:", numbers)
    sum =0
    for i in numbers:
        sum+=i
    print("tổng dãy số:",sum)
total(1,2,3,4,5)

students =[
    {
        "id":1,
        "name":"Khánh"
    },
    {
        "id":1,
        "name":"Đức"
    },
]

#  tạo hàm hiển thị danh sách sinh viên
def print_students(data):
    for std in data:
        print("tên sinh viên: ",std["name"])
print_students(students)
# thêm học vào thời khóa biểu

timetable =[
    {
        "id":1,
        "subject":"lập trình python"
    }
]
def add_subject():
    """ 
     Tạo id tự động
     Nếu mảng ban đầu chưa có phần tử thì gán id = 1
     Nếu có rồi lấy ID của phần tử cuối cùng + 1
     """
    if len(timetable) ==0:
        new_id =1
    else:
        new_id = timetable[-1]["id"] + 1
    subject_name = input("mời nhập tên môn")
    new_subject ={
        "id":new_id,
        "subject":subject_name
    }
    timetable.append(new_subject)
    print("danh sách các môn trong thời khóa biểu:", timetable)
add_subject()



# đi siêu thị phải tính tiền thanh toán đơn hàng
carts =[
    {
        "id":1,
        "product":"mì tôm hảo hảo",
        "quantity":5,
        "price":5000
    },
     {
        "id":2,
        "product":"bánh mì sài gòn",
        "quantity":3,
        "price":35000
    }
]
#  viết hàm tính tiền để thanh toán , nhận vào tham số là giỏ hàng
def payment(list):
    total=0
    for item in list:
        total+= item["quantity"]*item["price"]
    print(f"tổng tiền phải thanh toán: {total}")
payment(carts)


products =[
    {
        "id":1,
        "name":"iphone14",
        "price": 11000000
    },
    {
        "id":2,
        "name":"iphone15",
        "price": 15000000
    },
     {
        "id":3,
        "name":"iphone16",
        "price": 20000000
    }
]
#  HIỂN THỊ DANH SÁCH CÁC SẢN PHẨM CÓ GIÁ TỪ 15TR TRỞ LÊN
# TẠO HÀM KIỂM TRA
def check_price(product):
    if product["price"]>=15000000:
        return 1
    return 0
# TẠO HÀM HIỂN THỊ
def show_products(list):
    for item in list:
        if check_price(item):
            print(f"sản phẩm {item["name"]} có giá >= 15.000.000")
show_products(products)