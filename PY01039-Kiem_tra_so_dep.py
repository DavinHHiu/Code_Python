def check(s):
    if s[0] == s[1]: return False
    for i in range(2, len(s)):
        if s[i] != s[0] and s[i] != s[1]: return False
        if i % 2 == 0 and s[i] != s[0]: return False
        if i % 2 != 0 and s[i] != s[1]: return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t -= 1