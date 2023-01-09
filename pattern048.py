# 1
# 6 2
# 10 7 3
# 13 11 8 4
# 15 14 12 9 5

n = 1
r = 5
for i in range(1, 6):
    n2 = n
    c = 5
    for j in range(i):
        if j == 0:
            print(n2, end=" ")
            c = c-i+1
        elif j >= 1:
            n2 -= c
            print(n2, end=" ")
            c += 1
    n += r
    r -= 1
    print()