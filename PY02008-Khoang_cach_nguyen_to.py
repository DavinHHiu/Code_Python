import math
listNT = []

def checkNguyenTo(n):
    if n  == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

for i in range(2, 9000):
    if len(listNT) > 1001: break
    if checkNguyenTo(i): 
        listNT.append(i)

"""Main"""
n, x = map(int, input().split())
print(x, '', end = '')
for i in range(n):
    print(x + listNT[i], '', end = '')
    x += listNT[i]