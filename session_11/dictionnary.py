""" 

dictionnary: Từ điển _ Đây là kiểu dữ liệu dùng để lưu trữ dữ liệu dưới dạng 
key và value
vd : lưu thông tin của một sinh viên, lưu thông tin của một sản phẩm, bài viết, bình luận,
...
cú pháp :
my_dictionnary = {
                    "key": value
                }

 """

student= {
    "name":"Đức",
    "age" :19,
    "course":["C++","C","Python"],
    "age":20
}
print("student",student)
#  khai báo dictionnary 1 sản phẩm bất kì ( tên sản phẩm, mã sản phẩm, giá, số lượng)
""" 
Các thao tác làm việc với dictionnary: CRUD
1. CREATE
     thêm các key và value
     C1: dictionnary ["tên key"]= "giá trị"
     C2: dùng hàm update
         tên dictionary.update({"tên key":"giá trị"})
     C3: dùng setdefault
2. READ : hiển thị 
3. UPDATE : cập nhật
4. DELETE : xóa
    + dùng pop(tên key) : nếu key không tồn tại thì chương trình báo bug
    + dùng del dictionnary_name["key_name"]  ( sẽ không trả về giá trị, nếu key không tồn
    tại chương trình báo bug)
    + pop (tên key, None) : nếu không có chương trình không báo bug


 """
product ={}
product["product_name"]= "iphone 16"
product.update({"product_id":"SP01"})
product.setdefault("price",32000000)

# print("thông tin sản phẩm", product)

for key in product:
    print("key", key)
for abc in product:
    print("value",abc)
# hiển thị tên key (thuộc tính)
for key_name  in product.keys():
    print("tên key:", key_name)
#  hiển thị value ( giá trị)
for value in product.values():
    print("giá trị từng key:", value)
#  lấy cả key và value
for key,value in product.items():
    print(f"tên key : {key} _ giá trị: {value}")

#  cập nhật giá trị của key 
product["price"] =31000000
product["quantily"] =5
print("sản phẩm sau khi cập nhật", product)
#  cập nhật key
#  bỏ key cũ đi , thêm key mới vào
#  xóa key

result= product.pop("quantily")
print("giá trị vừa xóa", result)
 
# del product["product_name"]
product.pop("price",None)
print("thông tin sản phẩm sau khi xóa", product)

