import math

def factor(n):
    sum = 0
    while n > 0:
        sum += math.factorial(n % 10)
        n //= 10
    return sum

t = int(input())
while t > 0:
    n = int(input())
    if n == factor(n): print("Yes")
    else: print("No")
    t -= 1