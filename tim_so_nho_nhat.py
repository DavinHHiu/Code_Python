t = int(input())
while t > 0:
    s = input()
    min = 10 ** 18
    n = ""
    for c in s:
        if c.isdigit(): n += c
        else: 
            if n != "" and min > int(n): min = int(n)
            n = ""
    if n != "" and min > int(n): min = int(n)
    print(min)
    t -= 1