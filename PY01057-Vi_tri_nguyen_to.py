import math
nt = ['2', '3', '5', '7']

def checkNguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False 
    for i in range(3, math.isqrt(n) + 1, 2): 
        if n % i == 0: return False
    return True

def check(s):
    for i in range(len(s)): 
        if checkNguyenTo(i):
            if s[i] not in nt: return False
        else:
            if s[i] in nt: return False
    return True

"""Main"""
t = int(input())
while t > 0: 
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t -= 1
    