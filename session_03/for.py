""" 
for:
ứng dụng:
    + Dùng trong các bài toán biết trước số lần lặp.
cú pháp: 
 for variable_name in range()
 range: có 3 tham số
    1 tham số : range(stop): tức là sẽ chạy: 0<= value <stop
    2 tham số: range(start, stop) : start <= value < stop
    3 tham số: range(start, stop, step)
 

 """
for item in range(5):
    print("giá trị item: ", item)
for i in range(4,8):
    print("giá trị i: ", i)
#  in các số chia hết cho 3 từ 1 đến 15
for i in range (1,16):
    if i%3==0:
        print(i)
for i in range (0,16,3):
    print("mới:", i)
# in các số từ 10 -> 1

for i in range (10,0,-1):
    print ("số giảm dần:", i)
# luồng thực thi của for: 
