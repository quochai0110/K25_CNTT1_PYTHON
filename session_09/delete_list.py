students = ["Hoa", "Hồng", "Nhung"]
# del students[1:3]
print("danh sách sv", students)

#  del và pop khác nhau như thế nào
# duyệt trực tiếp các phần tử
for item in students:
    print("item: ",item)
#  duyệt theo index
for index in range(len(students)):
    print("index",index)
    print ("student_name", students[index])
# enumarate(liệt kê): 
for index,value in enumerate(students):
    print("vị trí:", index)
    print("giá trị:",value)