""" 
        HỆ THỐNG QUẢN LÝ GIỎ HÀNG AMAZON
INPUT:  Dữ liệu đề bài cho
    + cho dữ liệu giỏ hàng : list []
    [
        {},
        {},
        {}
    ]
    + từng sản phẩm sẽ có các thuộc tính
        + id sản phẩm
        + tên sản phẩm
        + số lượng sản phẩm
        + đơn giá 1 sản phẩm
OUTPUT: kết quả
    1. Xem chi tiết giỏ hàng
        + Xem thông tin từng sản phẩm trong giỏ hàng
    2. Thêm sản phẩm vào giỏ hàng
        + Nhập mã sản phẩm:
            TH1: mã sản phẩm đã tồn tại: thì nhập số lượng để cộng dồn
             ( kiểm tra người không đúng số, số âm)
            TH2: mã sản phẩm không tồn tại: 
                cho nhập tên, số lượng, giá, (kiểm tra số lượng, giá : thỏa mãn
                điều kiện không âm...)
    3. Cập nhật số lượng sản phẩm
        -Nhập mã sản phẩm cần cập nhật
            + Nếu đã tồn tại thì nhập số lượng mới: kiểm tra dữ liệu rồi cập nhật
            + Nếu không tồn tại thì thông báo
    4. Xóa sản phẩm trong giỏ hàng
        - Nhập mã sản phẩm cần xóa
            + Kiểm tra mã sản phẩm có tồn tại hay không
                TH1: Nếu có thì xóa: theo index hoặc giá trị
                TH2: Nếu không có thì thông báo mã sản phẩm không tồn tại
    5. Thoát chương trình

 """
cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]
sum = 0
while True:
    print(""" 1. Xem chi tiết giỏ hàng và tính tổng tiền
              2. Thêm sản phẩm
              5. Thoát     
           """)
    choice = input("Nhập vào lựa chọn : ")
    if choice =='1':
        for item in cart_items:
            print(f"Tên sản phẩm:_ {item['name']} , số lượng:_{item['number']}, giá tiền:_{item['price']}" )
            sum += item['number'] * item['price']
        print('Tổng tiền: ', sum )
    elif choice == '2' :
        status = False
        product_id = input("Nhập mã sản phẩm").strip().upper()
        for product in cart_items:
            if product_id == product['id'] :
                quantity = input("Nhập vào số lượng: ")
                status = True
                if quantity.isdigit():
                    if int(quantity) > 0:
                        product["number"] += int(quantity)
                    else:
                        print("Số lương không hợp lệ")
                else:
                    print("Số lượng không hợp lệ")    
                break
        
        if status == False:
            # cho nhập tên, số lượng, giá
            product_name = input("mời nhập tên sản phẩm")
            price = input("mời nhập giá")
            quantity = input("mời nhập số lượng")
            # thêm try except
            try:
                price = float(price)
                if price <= 0:
                    print("Giá phải lớn hơn 0.")
                    continue
            except:
                print("Giá không hợp lệ.")
                continue
            if not quantity.isdigit():
                    print("số lượng không hợp lệ")
                    continue
            quantity = int(quantity)
            if quantity <= 0:
                print("Số lượng phải lớn hơn 0.")
                continue

            #  hợp lệ
            new_product = {
                "id": product_id,
                "name":product_name,
                "price":price,
                "quantity": quantity
            }
            # thêm vào cuối mảng
            cart_items.append(new_product)

    if choice == "5":
        break

    