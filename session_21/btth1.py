import logging

""" 
    CHỨC NĂNG 1: NẠP TIỀN VÀO VÍ
        + Tạo hàm nạp tiền vào ví
        + Khởi tạo số tiền trong ví ban đầu = 0
        + validate dữ liệu khi nhập số tiền âm,  chữ cái không phải số
        + tạo log 
    CHỨC NĂNG 2: CHUYỂN TIỀN
        + Tạo hàm chuyển tiền
            + cho người dùng nhập tiền cần chuyển
            + validate dữ liệu :   
                + nhập số điện thoại yêu cầu 10 số
                + số tiền cần chuyển <= số dư trong ví
                + sau đó ghi log


 """
balance = 5000000
logging.basicConfig(
    filename='momo_log.log',
    level = logging.INFO,
    format='[%(asctime)s]-[%(levelname)s]-[%(message)s]'
)
# viết hàm kiểm tra đúng định dạng số điện thoại
# gồm 10 số, bắt đầu bằng số 0
def check_phone(phone):
    if len(phone)!=10 or not phone.isdigit() or not phone.startswith('0'):
        return False
    return phone
print("test case1: ", check_phone("0987654321"))
print("test case2: ", check_phone("098765432a"))
print("test case3: ", check_phone("9087654321"))

#  hàm chuyển tiền
def draw_amout():
    global balance
    phone_number = input("mời nhập số điện thoại")
    if check_phone(phone_number):
        try:
            amount = int(input("nhập số tiền cần chuyển"))
            if amount <0:
                logging.error("money cannot < 0")
                return
            if amount > balance:
                logging.error("balance so poor")
                return
            if amount > 10000000:
                logging.warning("big transaction")
                balance -= amount
                return
            balance -= amount
        except ValueError as e:
            logging.error("error", e)
    else:
        logging.error("wrong format")

# nên tách để validate khi nhập số tiền cần nạp
def handle_deposit():
    global balance
    try:
      money_input =  int(input('nhập số tiền nạp: '))
      if money_input < 0:
        logging.error("invalid!")
        return
      if money_input > balance:
        logging.error("invalid!")
        return
      if money_input>10000000:
          logging.warning("")
          pass
    except:
          pass

def deposit(balance):
    try:
        amount = int(input("Nhập vào số tiền cần nạp: "))
        if amount <= 0:
            logging.error(f'error-amount')
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
            return
        balance += amount
        logging.info(f'add successfully,balance:{balance}')
    except ValueError as e:
        logging.error(f'Value-error')
        print("lỗi ",e)
while True:
    print(""" 
        ========== VÍ MOMO GIẢ LẬP ==========
        1. Nạp tiền vào ví
        2. Chuyển tiền
        3. Xem lịch sử hệ thống
        4. Xem số dư tài khoản
        5. Thoát chương trình 
        ===============================================
        Chọn chức năng (1-5):
 """)
    choice = input("Nhập vào lựa chọn: ")
    if choice == '1':
        deposit(balance)
        pass
    elif choice == '2':
        draw_amout()
        print(f"số dư hiện tại {balance}")
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print('Thoát chương trình...')
        break