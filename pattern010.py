# 1 1 2 1 3 1
# 1 2 2 2 3 2
# 1 3 2 3 3 3
# 1 4 2 4 3 4
# 1 5 2 5 3 5

a = 1
for i in range(1, 6):
    b = 1
    for n in range(1, 7):
        if n%2 != 0:
            print(b, end=" ")
            b += 1
        else:
            print(a, end=" ")
    print()
    a += 1
    