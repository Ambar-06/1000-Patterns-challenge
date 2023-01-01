# 2
# 24
# 246
# 2468
# 246810

for i in range(1, 6):
    a = 2
    for j in range(i):
        if a%2 == 0:
            print(a, end="")
            a += 2
    print()
