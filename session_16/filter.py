numbers = [4,7,8,3,2]
# lọc các số chẵn trong mảng
result = list(filter( lambda x:x%2==0,numbers))
print("mảng số chẵn sau khi lọc", result)
stds =[
    {
        "id":1,
        "score":4
    },
    {
        "id":1,
        "score":9
    },
    {
        "id":1,
        "score":6
    },
    {
        "id":1,
        "score":1
    }
]
# lọc ra những sinh viên có điểm lớn hơn 5
filtered = list(filter(lambda std:std["score"]>=5,stds))
print(filtered)