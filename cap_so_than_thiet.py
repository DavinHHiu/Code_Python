import math

a, b = [int(t) for t in input().split()]

sumGCDa = a + 1
sumGCDb = b + 1

for i in range(2, math.isqrt(a)):
    if a % i == 0: 
        if i != a / i: 
            sumGCDa += i + a / i
        else: sumGCDa += i

for i in range(2, math.isqrt(b)):
    if b % i == 0: 
        if i != b / i: 
            sumGCDb += i + b / i
        else: sumGCDb += i

if sumGCDa == sumGCDb: print('YES')
else: print('NO')