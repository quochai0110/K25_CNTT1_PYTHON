#  quản lý sản phẩm

#  tạo danh sách sản phẩm
import currency
print(1111,currency.convert_money(100000) )
print(2222,currency.money )
products = [
    {
        "id":1,
        "name":"iphone 14",
        "price": 15000000
    },
    {
        "id":2,
        "name":"iphone 15",
        "price": 18000000
    },
    {
        "id":3,
        "name":"iphone 16",
        "price": 25000000
    }
]
#  thêm mới sản phẩm
#  viết hàm thêm mới sản phẩm

def add_product(product_name, price):
    if len(product)==0:
        new_id=1
    else:
        new_id=product[-1]["id"]+1
    product= {
        "id":new_id,
        "name": product_name,
        "price":price
    }
    products.append(product)
# hàm hiển thị thông tin sản phẩm
def print_products (list):
    for item in list:
        print(f"tên sản phẩm: {item["name"]}, giá : {currency.convert_money(item["price"])} VND")
print_products(products)