""" 
    Câu điều kiện trong python
    if
    elif
    else
    switch-case (js)
    match-case (python)

 """
age = int(input("mời nhập tuổi của bạn"))

if age>=18 :
    print(" đủ tuổi làm căn cước công dân")

#  nhập điểm tổng kết python của bạn Bình LỚP CNTT1

score = float(input("mời nhập điểm"))
if score>=8 and score <= 10:
    print("loại giỏi")
elif score>=6.5 and score <8:
    print("loại khá")
elif score >=5:
    print("loại trung bình")
else:
    print("loại yếu")
#  chuyển cú pháp if_ else sang dạng match case

match score:
    case score if score >= 8 and score <= 10:
        print("Loại giỏi")
    case score if score >= 6 and score < 8:
        print("Loại khá")
    #  tương tự default trong switch-case
    case _:
        print("")

