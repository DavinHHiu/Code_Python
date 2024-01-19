file = open('VANBAN.in', 'r')
a = []
b = {}
Max = 0

def checkTN(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]: return False
    return True

for x in file:
    for i in x.split():
        if checkTN(i):
            if i not in a: a.append(i)
            if i in b: b[i] += 1
            else: 
                b[i] = 1
                Max = max(Max, len(i))

for x in a:
    if len(x) == Max: 
        print(x, b[x])
        break