""" 

    CONTINUE: bỏ qua lần lặp và quay về lần lặp tiếp theo.
    VD1:
        In các số từ 1 đến 10 trừ số 5

 """
for i in range(1,11):
    if i!=5 :
      print("i",i)

for j in range (1,11):
   if j==5:
      continue
   print("j",j)