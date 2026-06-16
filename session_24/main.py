""" 
    LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG? OOP_ Object oriented programming
    ĐỐI TƯỢNG SẼ GỒM CÓ 2 THÀNH PHẦN CHÍNH
        + DỮ LIỆU: thuộc tính của đối tượng
        + HÀNH VI: phương thức của đối tượng

        LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG GOM NHÓM DỮ LIỆU VÀ HÀNH VI BÊN TRONG ĐỐI TƯỢNG

        VD: đối tượng chiếc xe
        + dữ liệu: hãng xe, loại xe, tốc độ di chuyển
        + hành vi: di chuyển, khởi động, dừng lại


        CLASS: BẢN THIẾT KẾ, KHUNG ĐỂ KHỞI TẠO ĐỐI TƯỢNG
        INSTANCE: ĐỐI TƯỢNG ĐƯỢC TẠO RA TỪ BẢN THIẾT KẾ

        CÁC TÍNH CHẤT CỦA LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG
        1. Tính đóng gói (bao đóng)
            + để việc truy cập ĐÚNG vào các thuộc tính 
        2. Tính kế thừa
            + Lớp con khi kế thừa lớp cha thì sẽ có các thuộc tính và phương thức
            của lớp cha
        3. Tính đa hình
            + Cùng 1 phương thức nhưng triển khai bên trong lại khác nhau
        4. Tính trừu tượng
            + Quan tâm đến kết quả chức năng thay vì xem bên trong

    những bài trước đây các em dùng lập trình hướng thủ tục, hướng hàm



 """
#  ví dụ lập trình hướng hàm tạo dữ liệu chiếc xe
def create_vehical(brand, model, speed):
    return {
        "brand": brand,
        "model":model,
        "speed":speed
    }
#  lập trình hướng hàm để tạo hành vi của chiếc xe
def run():
    print(f"chiếc xe {create_vehical("toyota","vios",120)["model"]} bắt đầu di chuyển")

# run()

#  CHUYỂN SANG LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG

class Vehical:
    #  __init__ (self): bắt buộc phải ghi như thế hàm tạo constructor
    #  khởi tạo dữ liệu
    def __init__(self,brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    #  khởi tạo các hành vi
    #  tạo phương thức khởi động xe
    def start(self):
        print(f"chiếc xe {self.model} đã khởi động thành công")
    # tạo phương thức hiển thị thông tin chiếc xe
    def display_info(self):
        print(f"hãng xe: {self.brand}")
        print(f"loại xe: {self.model}")
        print(f"tốc độ: {self.speed}")

car = Vehical("Toyota","vios",100)
car.speed = -5
print("thông tin chiếc xe", car.__dict__)
#  truy cập vào các thương thức của đối tượng
# car.start()
# car.display_info()

len("python")
len([1,2,3])
print(1+1)
print("py"+"python")

class Animal:
    def __init__(self, name):
        self.name= name
        pass
    def sound(self, sound):
        print(f"loài {self}. name kêu {self.sound} ")
cat = Animal("Mèo")
bird = Animal("con chim")
cat.sound("meo meo")
bird.sound("chíp chip")

