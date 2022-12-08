# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# 42 44 46 48 50

n = 1
for _ in range(5):
    for i in range(10):
        if n%2 == 0:
            print(n, end=" ")
        n += 1
    print()