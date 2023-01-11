#      *
#     **
#    ***
#   ****
#  *****
# ******
#  *****
#   ****
#    ***
#     **
#      *

a = 5
b = 1
for i in range(1, 12):
    for j in range(1):
        print(" "*a, end="")
        print("*"*b, end="")
        if i < 6:
            a-= 1
            b+= 1
        elif i >= 6:
            a+= 1
            b-= 1
    print()