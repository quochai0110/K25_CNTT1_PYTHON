""" 
LOGGING: 
    ghi lại lịch sử của người dùng khi thao tác với chương trình
 """
import logging
try:
    x = int(input("Nhập một số: "))
    y = 10 / x  # Có thể lỗi chia cho 0
    logging.info(f"Kết quả ",y)
except ValueError:
    logging.error("Bạn phải nhập số nguyên!")
except ZeroDivisionError:
    logging.error("Không thể chia cho 0!")