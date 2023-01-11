# 1
# 9 2
# 10 8 3
# 14 11 7 4
# 15 13 12 6 5

a = 1
b = 7
n = 5
temp = 2
for i in range(1, n+1):
    for j in range(i):
        if j == i-1:
            print(a, end=" ")
        elif j > 0 and j < i:
            if i%2 == 0:
                print(a+b-temp, end=" ")
                temp -= 1
            else:
                print(a+b-temp, end=" ")
                temp += 1
        else:
            c = a+b
            print(c, end=" ")
    if i > n//2:
        b = 10
    a += 1
    print()