""" 

Nhập số lượng nhân viên
sau đó nhập thông tin nhân viên:
    + tên
    + số ngày đi làm
        kiểm tra số ngày đi làm
        + dưới 20: hiển thị cần cải thiện chuyên cần
        + trên 20: nhân viên chuyên cần tốt

 """
while True:
    count = int(input("nhập số lượng nhân viên"))
    for i in range(1,count+1):
        print(f("nhập thông tin nhân viên thứ {i}"))
        name= input("nhập tên nhân viên")
        work_day = int(input("nhập số ngày đi làm !"))
        if work_day>=20:
            print("nhân viên chuyên cần tốt!")
        else:
            print("cần cải thiện chuyên cần")
        print(f"thông tin nhân viên thứ {i}: tên_ {name}, ngày làm việc_ {work_day}")
    choose = input("bạn có muốn thoát hay ở lại yes|no")
    if choose!="yes":
        print("thoát chương trình!")
        break
