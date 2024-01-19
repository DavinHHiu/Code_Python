t = int(input())
while t > 0:
    s = input()
    max = 0
    n = ""
    for c in s:
        if c.isdigit(): n += c
        else:
            if n != "" and max < int(n): max = int(n)
            n = ""
    if n != "" and max < int(n): max = n
    print(max)
    t -= 1