# 1 10 11 20 21
# 2 9 12 19 22
# 3 8 13 18 23
# 4 7 14 17 24
# 5 6 15 16 25

n = 5
for i in range(1, 6):
    x = i
    y = n - i + 1
    for j in range(1, 6):
        if j%2 == 1:
            print(x, end=" ")
        else:
            print(y, end=" ")
        x = x+n
        y = y+n
    print()

#COPIED