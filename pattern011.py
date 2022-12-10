# 1 1 1 2 1 3
# 2 1 2 2 2 3
# 3 1 3 2 3 3
# 4 1 4 2 4 3
# 5 1 5 2 5 3

m = 1
for i in range(5):
    n = 1
    for j in range(1, 7):
        if j%2 ==0:
            print(n, end=" ")
            n += 1
        else:
            print(m, end=" ")
    print()
    m += 1