# form từ file nào và import hàm nào?
from unit_test import aver

#  case test tính điểm trung bình --> tính đúng

def average_normal():
    assert aver([4,5,6]) == 6

def average_normal():
    assert aver([]) == 0