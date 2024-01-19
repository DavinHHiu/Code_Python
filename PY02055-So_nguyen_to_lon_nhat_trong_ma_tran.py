import math

def nguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

n, m = map(int, input().split())
a = [[]] * n
Max = 0

for i in range(n):
    a[i] = [int(x) for x in input().split()]

for i in range(n):
    for j in range(m):
        if nguyenTo(a[i][j]) and a[i][j] > Max:
            Max = a[i][j]
if Max == 0: print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max:
                print(f'Vi tri [{i}][{j}]')
