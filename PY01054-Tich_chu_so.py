"""Main"""
t = int(input())
while t > 0:
    s = input()
    mul = 1
    for c in s:
        if(c != '0'): mul *= int(c)
    print(mul)
    t -= 1