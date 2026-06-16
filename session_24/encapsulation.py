""" 

    TÍNH ĐÓNG GÓI
        + GIÚP TRUY CẬP ĐÚNG VÀO DỮ LIỆU
        3 BỔ TỪ TRUY CẬP
            + public
            + protected  _
            + private    __
        GETTER: lấy dữ liệu
        SETTER: cập nhật dữ liệu

 """
class Phone:
    def __init__(self,name, price):
        self.name = name
        self.__price= price
phone_1 = Phone ("iphone15", 18000000)
phone_1.__price = -1
phone_1._Phone__price = -5
print("thông tin chiếc điện thoại",phone_1.__dict__)