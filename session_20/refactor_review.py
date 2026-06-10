""" 
    REFACTOR & REVIEW
    1. Đặt tên hàm, têm biến rõ ràng có ý nghĩa
    2. Nguyên tắc đơn nhiệm của hàm
        + Hàm thực hiện 1 chức năng duy nhất
    3. Khai báo type hints ( gợi ý)
    4. Xử lý Arrow Anti-Pattern
 """
price= 5000
a=5000
#  hàm tìm kiếm sinh viên
def find_student():
    # chỉ mục đích là tìm kiếm
    #  cập nhất sinh viên là sai
    pass
# TYPESCRIPT

def payment(price:float, quantity:int)-> float:
    return price * quantity
# payment("5",6)
def check_number(number):
    # if number > 0:
    #     if number <= 50:
    #         if number % 2 == 0:
    #             print("even number")
    if number < 0:
        return
    if number >= 50:
        return
    if number % 2 != 0:
        return
    print ("even number")
        
    

    