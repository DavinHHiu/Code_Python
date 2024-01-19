import math

def checkNguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

def check(s):
    sum = 0
    for c in s:
        if c != '2' and c != '3' and c!= '5' and c != '7':
            return False
        sum += int(c)
    if not checkNguyenTo(sum): return False
    if not checkNguyenTo(int(s[::-1])): return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    if check(s): print("Yes")
    else: print("No")
    t -= 1
