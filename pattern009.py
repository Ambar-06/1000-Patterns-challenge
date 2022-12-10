# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

m = 1
for n in range(1, 6):
    for i in range(5):
        if i == 0:
            print(n, end=" ")
        else:
            n = n+m
            print(n, end=" ")
    m += 1
    print()