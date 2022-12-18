# A F K P U
# B G L Q V
# C H M R W
# D I N S X
# E J O T Y

n = 5
for i in range(n):
    c = 65
    c += i
    for j in range(n):
        print(chr(c), end=" ")
        c += n
    print()