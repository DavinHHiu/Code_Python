def tangGiam(s):
    if(len(s) < 3): return False
    index = 0
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            index = i
            break
        elif s[i] == s[i + 1]: return False 
    if index == 0: return False
    for i in range(index, len(s) - 1):
        if s[i] <= s[i + 1]: return False
    return True

t = int(input())
for i in range(t):
    if tangGiam(input()): print("YES")
    else: print("NO")