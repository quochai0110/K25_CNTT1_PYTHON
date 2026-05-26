""" 

    HỆ THỐNG QUẢN LÝ DOANH THU CỬA HÀNG CAFE
    INPUT:
        TÊN CHI NHÁNH:
        branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", 
        "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
        DOANH THU: daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] (Đơn vị: VNĐ)
        TRẠNG THÁI ĐẠT CHỈ TIÊU CỦA TỪNG CHI NHÁNH: 
        target_achieved = [True, True, False, True, False] (True là Đạt chỉ tiêu, False là Không đạt)
    OUT: 
        + Hiển thị báo cáo doanh thu tổng hợp 
        + Thống kê chi nhánh có doanh thu cao nhất và thấp nhất
        + Lọc danh sách cơ sở không đạt chỉ tiêu

 """
branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] 
target_achieved = [True, True, False, True, False] 
max= daily_revenues[0]
max_index=0
for index, value in enumerate(daily_revenues):
    if max < value:
        max= value
        max_index = index
print(f"Tên chi nhánh có doanh thu cao nhất là: {branch_names[max_index]} với doanh thu là: {max}")

#  lọc danh sách chi nhánh không đạt chỉ tiêu
for index, value in enumerate(target_achieved):
    if value==False:
        print(f"tên chi nhánh không đạt: {branch_names[index]}")


