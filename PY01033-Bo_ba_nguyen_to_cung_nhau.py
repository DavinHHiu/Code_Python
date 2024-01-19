import math

def GCD(a, b):
    if math.gcd(a, b) == 1: return True
    return False

a, b = map(int, input().split())
b += 1

for i in range(a, b - 2):
    for j in range(i + 1, b - 1):
        for k in range(j + 1, b):
            if GCD(i, j) and GCD(i, k) and GCD(j, k):
                print(f'({i}, {j}, {k})')