import math

def nguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2): 
        if n % i == 0: return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
dic = dict()

for x in a:
    if x in dic: 
        dic[x] += 1
    elif nguyenTo(x): dic[x] = 1
for x in dic:
    print(x, dic[x])
    

