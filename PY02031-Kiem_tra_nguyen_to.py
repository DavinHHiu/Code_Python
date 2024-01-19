import math

def checkNguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

"""Main"""
dong, cot = map(int, input().split())
arr = [[0 for _ in range(cot)] for _ in range(dong)]
for i in range(dong):
    arr[i] = list(map(int, input().split()))

for i in range(dong):
    for j in range(cot):
        if checkNguyenTo(arr[i][j]):
            print(1, '', end = '')
        else: print(0, '', end = '')
    print()