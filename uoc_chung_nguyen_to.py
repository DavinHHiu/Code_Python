import math

def checkNguyenTo(n):
    if n == 2: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True
t = int(input())
while t > 0: 
    a, b = map(int, input().split())
    GCD = math.gcd(a, b)
    sum = 0
    while GCD > 0: 
        sum += GCD % 10
        GCD //= 10
    if(checkNguyenTo(sum)): print("YES")
    else: print("NO")
    t -= 1