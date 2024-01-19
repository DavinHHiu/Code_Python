import math
"""Main"""
t = int(input())
while t > 0:
    s = input()
    s_dao = s[::-1]
    n = int(s)
    m = int(s_dao)
    if(math.gcd(m, n) == 1): print("YES")
    else: print("NO")
    t -= 1