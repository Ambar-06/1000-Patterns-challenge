# 1 3 5 7 9
# 3 5 7 9 11
# 5 7 9 11 13
# 7 9 11 13 15
# 9 11 13 15 17

for i in range(1, 10):
    if i%2 != 0:
        for j in range(10):
            if j%2 == 0:
                print(i+j, end=" ")
        print()