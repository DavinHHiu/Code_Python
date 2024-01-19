t = int(input())
while t > 0:
    s = input()
    count = 1
    for i in range(1,len(s)):
        if(s[i] != s[i - 1]):
            print(str(count) + s[i - 1], end = '')
            count = 1
        else: count += 1
    print(str(count) + s[len(s) - 1])
    t -= 1