# 0 1 0 1 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# 0 1 0 1 0

for i in range(1, 6):
    for j in range(1, 6):
        if i%2 == 0:
            print(0, end=" ")
        elif j%2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()