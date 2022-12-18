# A B C D E
# B C D E F
# C D E F G
# D E F G H
# E F G H I

for i in range(5):
    c = 65+i
    for j in range(5):
        print(chr(c), end=" ")
        c += 1
    print()