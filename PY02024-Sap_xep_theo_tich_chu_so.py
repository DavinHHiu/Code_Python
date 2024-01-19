def cmp(a):
    mul = 1
    for c in a:
        mul *= int(c)
    return mul, int(a)

"""Main"""
t = int(input())
while t > 0:
    n = int(input())
    daySo = [t for t in input().split()]
    daySo.sort(key = cmp)
    for i in daySo:
        print(i, end = ' ')
    print()
    t -= 1
    