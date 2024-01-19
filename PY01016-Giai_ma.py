t = int(input())
while t > 0:
    s = input()
    i = 0
    while i in range(len(s)):
        c = int(s[i + 1])
        while(c > 0):
            print(s[i], end = '')
            c -= 1
        i += 2
    print('')
    t -= 1