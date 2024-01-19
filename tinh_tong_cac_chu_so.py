t = int(input())
while t > 0:
    s = input()
    lst = []
    sum = 0
    for c in s:
        if c.isalpha(): lst.append(c)
        if c.isdigit(): sum += int(c)
    lst.sort()
    for c in lst:
        print(c, end = '')
    print(sum)
    t -= 1