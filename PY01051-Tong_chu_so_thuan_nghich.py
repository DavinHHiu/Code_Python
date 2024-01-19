def checkThuanNghich(s):
    if(len(s) < 2): return False
    for i in range(len(s)//2):
        if(s[i] != s[len(s) - 1 - i]): return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    sum = 0
    for c in s:
        sum += int(c)
    if checkThuanNghich(str(sum)): print("YES")
    else: print("NO")
    t -= 1