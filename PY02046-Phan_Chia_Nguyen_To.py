import math

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2): 
        if n % i == 0: return False
    return True

n = int(input())
a = []
sumA = 0

for x in input().split():
    if int(x) not in a:
        a.append(int(x))
        sumA += int(x)

sumI = 0
ok = 1
for i in range(len(a)):
    sumI += a[i]
    if isPrime(sumI) and isPrime(sumA - sumI):
        print(i)
        ok = 0
        break
if ok: print('NOT FOUND')