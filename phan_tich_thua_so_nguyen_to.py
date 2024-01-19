import math
def thuaSoNT(n):
    print(1, '* ', end = '')
    for i in range(2, math.isqrt(n) + 1):
        count = 0
        while n % i == 0:
            n /= i
            count += 1
        if count > 0: print(str(i) + '^' + str(count), end = '')
        if n > 1 and count > 0: print(' * ', end = '')
    if(n > 1): print(str(int(n)) + '^1')
    else: print('')

t = int(input())
while t > 0:
    n = int(input())
    thuaSoNT(n)
    t -= 1