""" 
HÀM SẮP XẾP
sort (): sắp xếp từ bé đến lớn
sort(reverce=True): từ lớn xuống bé
 """
numbers =[5,2,7,1,8]
numbers.sort(reverse=True)
print("giá trị mảng sau khi sáp xếp",numbers)

students =[
    {
        "id":1,
        "score":7
    },
     {
        "id":2,
        "score":6
    },
     {
        "id":3,
        "score":9
    },
     {
        "id":4,
        "score":8
    }
]
result= sorted(students,key=lambda std: std["score"])
print("giá trị mảng sinh viên sau khi sắp xếp", result)

sdt_cntt1 = ["Hiển","Bình", "Na","Phương"]
# sdt_cntt1.sort()
sdt_cntt1.sort(key=len)
print("cntt1:",sdt_cntt1)