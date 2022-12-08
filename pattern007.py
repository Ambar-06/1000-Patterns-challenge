# 1 3 5 7 9
# 11 13 15 17 19
# 21 23 25 27 29
# 31 33 35 37 39
# 41 43 45 47 49

n = 1
for _ in range(5):
    for i in range(10):
        if n%2 != 0:
            print(n, end=" ")
        n += 1
    print()