t = int(input())

for i in range(t):
    tich = 1
    ok = 1
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == '0': continue
        tich *= int(s[i])
    print(tich)