import math

    # Size: 9 x 27 
    # ------------.|.------------
    # ---------.|..|..|.---------
    # ------.|..|..|..|..|.------
    # ---.|..|..|..|..|..|..|.---
    # ----------WELCOME----------
    # ---.|..|..|..|..|..|..|.---
    # ------.|..|..|..|..|.------
    # ---------.|..|..|.---------
    # ------------.|.------------

    # ------------.|.------------
    # ---------.|..|..|.---------
    # ------.|..|..|..|..|.------
    # ---.|..|..|..|..|..|..|.---
    # ----------WELCOME----------
    # ---.|..|..|..|..|..|..|.---
    # ------.|..|..|..|..|.------
    # ---------.|..|..|.---------
    # ------------.|.------------

N = int(input("what's N?\n"))
M = int(input("what's M?\n"))
p = '.|.'
o = 1
copy_of_m = M

def midPoint(x):
    mid = x/2
    mid = math.ceil(mid)
    return mid

for _ in range(1, N+1):
    if _ < midPoint(N):
        M = copy_of_m - (len(p)*o)
    elif _ == midPoint(N):
        M = copy_of_m - len('WELCOME')
    elif _ > midPoint(N):
        M = copy_of_m - (len(p)*o)
        
    for i in range(1, M+1):
        if _ < midPoint(N) and i == M//2:
            print("-", end="")
            print(p*o, end="")
            o += 2
        elif _ == midPoint(N) and i == M//2:
            print("-", end="")
            print("WELCOME", end="")
            o -= 2
        elif _ > midPoint(N) and i == M//2:
            print("-", end="")
            print(p*o, end="")
            o -= 2
        else:
            print("-", end="")
    print()