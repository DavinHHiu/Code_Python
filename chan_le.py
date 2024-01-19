def check(s):
    sum = 0
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2: return False
        sum += int(s[i])
    sum += int(s[len(s) - 1])
    if(sum % 10 != 0): return False
    return True

t = int(input())
while t > 0:
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")
    t -= 1