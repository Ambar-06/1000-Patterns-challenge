# 5 10 15 20 25
# 4 9 14 19 24
# 3 8 13 18 23
# 2 7 12 17 22
# 1 6 11 16 21
    
n = 5
for i in range(5, 0, -1):
    a = i
    for j in range(1, 6):
        if j%2 == 1:
            print(a, end=" ")
        else:
            print(a, end=" ")
        a = a+n
    print()