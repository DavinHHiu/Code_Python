def check(s):
    for c in s:
        if c != '0' and c != '1' and c != '2':
            return False
    return True
"""Main"""
t = int(input())
while t > 0:
    if check(input()): print("YES")
    else: print("NO")
    t -= 1