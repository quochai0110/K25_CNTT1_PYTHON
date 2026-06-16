""" 

STATIC_METHOD: là những phương thức khi dùng không cần dùng dữ liệu của đối tượng
@static method
 """

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price= price
        self.stock= stock
       
    def display_info(self):
        print(f"tên sản phẩm: {self.name}")
        print(f"giá sản phẩm: {self.price}")
        print(f"số lượng sản phẩm: {self.stock}")
    @staticmethod
    def say_hello():
        print("chào bạn đến với cửa hàng")

new_product = Product("iphone 15",18000000,50)
print('thông tin điện thoại', new_product.__dict__)
new_product.say_hello()

