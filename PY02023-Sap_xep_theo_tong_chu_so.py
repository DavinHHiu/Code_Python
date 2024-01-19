#import functools

# def cmp(a, b):
#     sum1 = 0
#     sum2 = 0
#     for c in a:
#         sum1 += int(c)
#     for c in b:
#         sum2 += int(c)
#     if sum1 == sum2:
#         if int(a) > int(b): return 1
#         else: return -1
#     elif sum1 > sum2: return 1  
#     else: return -1

def cmp(a):
    sum = 0
    for c in a:
        sum += int(c)
    return sum, int(a)
"""Main"""
t = int(input())
while t > 0:
    n = int(input())
    dSo = [t for t in input().split()]
    dSo.sort(key = cmp)
    for i in dSo:
        print(i, "", end = '')
    print()
    t -= 1
