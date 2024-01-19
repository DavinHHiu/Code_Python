"""Main"""
t = int(input())
while t > 0:
    s = input()
    sum = 0
    multi = 1
    check = False
    for i in range(len(s)):
        if i % 2 == 0: sum += int(s[i])
        else:
            if s[i] == '0': continue
            else: 
                multi *= int(s[i])
                check = True
    if(check): print(sum, multi)
    else: print(sum, 0)
    t -= 1