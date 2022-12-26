# 5
# 45
# 345
# 2345
# 12345

for i in range(5):
    a = 5
    a -= i
    for j in range(-1, i):
        print(a, end="")
        a += 1
    print()