# 5 6 15 16 25
# 4 7 14 17 24
# 3 8 13 18 23
# 2 9 12 19 22
# 1 10 11 20 21

n = 5
for i in range(5, 0, -1):
    a = i
    b = n-i+1
    for j in range(1, 6):
        if j%2 == 1:
            print(a, end=" ")
        else:
            print(b, end=" ") 
        a = a+n
        b = b+n
    print()