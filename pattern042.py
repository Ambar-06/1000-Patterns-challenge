# 1
# 23
# 345
# 4567
# 56789

for i in range(5):
    a = 1
    a += i
    for j in range(-1, i):
        print(a, end="")
        a += 1
    print()