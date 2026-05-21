""" 
Clean code loop: viết code sạch
    1. đặt tên tiến rõ ràng có ý nghĩa, đặt theo tên tiếng anh
    2. đối với input : có promt yêu cầu rõ ràng
    3. viết code gọn gàng

 """
# cho người dùng nhập vào 1 số, sau đó tính tổng từ 1 cho tới số đó.

number = int (input("mời nhập số: "))
total = 0
for i in range(number+1):
    total+=i
print("total", total)