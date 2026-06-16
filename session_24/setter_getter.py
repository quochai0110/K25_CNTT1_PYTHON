class Bank:
    def __init__(self, owner, balance):
        self.__owner= owner
        self.__balance= balance

    def display_account(self):
        print(f"chủ tài khoản {self.__owner}")
        print(f"số dư tài khoản {self.__balance}")
    #  getter để lấy dữ liệu
    #  setter cập nhật dữ liệu 
    #  phương thức nạp tiền 
    def deposit(self,amount):
        if amount <= 0:
            print("số tiền nạp phải lớn hơn 0")
            return
        self.__balance += amount
    #  phương thức rút tiền
    def withdraw (self, amount):
        if amount > self.__balance:
            print("số dư không đủ")
            return
        self.__balance -= amount
    #  phương thức cập nhật thông tin tài khoản

    #  phương thức hiển thị số dư
    @property
    def display_balance(self):
        print(f" số dư còn lại : ", self.__balance)
    # def update_accont(self,new_name):
    #     self.__owner = new_name
    #  trong python cho phép truy cập phương thức như thuộc tính

account = Bank ("Nguyễn Tấn Dũng", 5000000)
# account.update_accont("Nguyễn Tuấn Dũng")
# account.update_accont
print("thông tin tài khoản", account.display_account)
# print("thông tin tài khoản: ", account.__dict__)