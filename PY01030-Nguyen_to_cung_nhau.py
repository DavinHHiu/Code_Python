import math

"""Main"""
a, b = map(int, input().split())
count = 0
for i in range(10 ** (b -1), 10 ** b):
    if(count == 10):
        count = 0
        print()
    if(math.gcd(a, i) == 1):
        print(i, '', end = '')
        count += 1