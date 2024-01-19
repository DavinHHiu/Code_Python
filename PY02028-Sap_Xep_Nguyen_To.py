import math

def checkNT(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2): 
        if n % i == 0: return False
    return True

n = int(input())
a = []
b = []
for x in input().split():
    if checkNT(int(x)): b.append(int(x))
    a.append(int(x))

b = sorted(b)
i = 0

for x in a:
    if checkNT(x): 
        print(b[i], end = ' ')
        i += 1
    else: print(x, end = ' ')

