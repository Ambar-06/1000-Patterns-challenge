# 1
# 35
# 579
# 791113
# 911131517

for i in range(0, 10, 2):
    a = 1
    a += i
    for j in range(-1, i, 2):
        print(a, end="")
        a += 2
    
    print()