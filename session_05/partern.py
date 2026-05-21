""" 
    Vẽ hình bằng code
    VD: tạo hình tam giác

    *
    **
    ***
    ****
    *****
 """
for i in range(5):
    #  i chạy: 0,1,2,3,4
    #  i=0 thì chạy hết for j
    #  i=1 
    #  i=2 
    for j in range(i+1):
        #  0, 1, 2, 3
        print("*", end=" ")
    print()
