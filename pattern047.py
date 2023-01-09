# 1
# 24
# 369
# 481216
# 510152025

a = 1
for i in range(1, 6):
    b = 1
    for j in range(i):
        print(a*b, end="")
        b += 1
    a += 1
    print()