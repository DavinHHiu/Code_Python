import math
def prime(n):
    if(n == 2): return 1
    if(n % 2 == 0 or n < 2): return 0
    for i in range(3, math.sqrt(n)):
        if(n % i == 0): return 0
        i += 2
    return 1
# Ham tim gcd    
# def gcd(a, b):
#     while(b):
#       a, b = b, a % b
#     return a
t = int(input())
while t > 0:
    n, k = int(input()), 1
    for i in range(2, n): 
        if(math.gcd(n, i) == 1): k += 1
    if(prime(k)): print('YES')
    else: print('NO')
    t -= 1