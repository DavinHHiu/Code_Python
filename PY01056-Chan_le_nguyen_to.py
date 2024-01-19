import math

def checkNguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % 3 == 0: return False
    return True

def check(s): 
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if i % 2 == 0: 
            if int(s[i]) % 2 != 0: return False
        else:
            if int(s[i]) % 2 == 0: return False
    if checkNguyenTo(sum) == False: return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t -= 1
