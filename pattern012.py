# 1 6 11 16 21
# 2 7 12 17 22
# 3 8 13 18 23
# 4 9 14 19 24
# 5 10 15 20 25

temp_var = 0
for i in range(5):
    n = 1 + temp_var
    m = 5
    for j in range(5):
        print(n, end=" ")
        n = n + m
    temp_var += 1
    print()