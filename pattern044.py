# 1
# 32
# 654
# 10987

a=1
for i in range(0, 8, 2):
    a += i
    for j in range(-1, i, 2):
        print(a, end="")
        a -= 1
    a += 1
    print()