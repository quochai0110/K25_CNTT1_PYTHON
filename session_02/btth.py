""" 
Viết chương trình python hỗ trợ đánh nhanh tình trạng của bệnh nhân
khi đến khám ở phòng khám!

gồm các yêu cầu:
    1. nhập thông tin bệnh nhân:
        + tên BN
        + năm sinh
        + số ngày bị bệnh
        + nhiệt độ cơ thể
        + chi phí khám bệnh
    2. kiểm tra dữ liệu đã hợp lệ hay chưa
        + tên không được để trống
        + sinh năm phải nằm trong khoảng (1900- hiện tại)
        + số ngày bị bệnh >= 0
        + nhiệt độ nằm trong khoảng : 30_45
        + chi phí khám >0
        + Nếu không hợp lệ thì in ra thông tin
        
    3. Tính toán thông tin
        Tính tuổi bệnh nhân
        Tính phụ phí = 10% chi phí khám
        Tính tổng chi phí = chi phí khám + phụ phí
    4. phân loại tình trạng sức khỏe
        Nếu nhiệt độ > 38°C và số ngày bệnh > 3 → "Nguy hiểm"
        Nếu nhiệt độ > 38°C → "Sốt cao"
        Nếu nhiệt độ > 37.5°C → "Sốt nhẹ"
        Ngược lại → "Bình thường"
    5. phân loại mức độ ưu tiên
    6. đánh giá mức chi phí ( dùng toán tử 3 ngôi)
 """
#  khai báo các biến thông tin bệnh nhân cho người dùng nhập dữ liệu
patient_name = input ("mời nhập tên bệnh nhân")
brith_year = int(input("mời nhập năm sinh"))
sick_days = int(input("số ngày bị bệnh"))
temperature = float(input("nhiệt độ cơ thể"))
medical_fee = float(input("nhập chi phí khám bệnh"))
#  validate dữ liệu

if patient_name == "" or (brith_year<1900 or brith_year>2026) or (temperature<30 or temperature>45) or medical_fee<=0 or sick_days<0 :
    print(" nhập sai dữ liệu")
else:
    age = 2026- brith_year
    print("tuổi bệnh nhân là: ", age)
    print("phụ phí: ", medical_fee*0.1)
    print("tổng chi phí =: ",medical_fee+ medical_fee*0.1 )
    #  4.phân loại tình trạng sức khỏe
    if temperature > 38 and sick_days>3:
        print("nguy hiểm")
    elif temperature>38:
        print("sốt cao")
    elif temperature>37.5:
        print ("sốt nhẹ")
    else:
        print("bình thường")
    # 5. phân loại mức độ ưu tiên
    # 6. đánh giá chi phí

    
