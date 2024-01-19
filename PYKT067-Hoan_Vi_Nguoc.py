ok = [0] * 15
a = []
n = 0

def Try(s):
    if len(s) == n:
        a.append(s)
    for i in range(n, 0, -1):
        if ok[i] == 0:
            ok[i] = 1
            Try(s + str(i))
            ok[i] = 0

t = int(input())
for i in range(t):
    a = []
    n = int(input())
    Try('')
    print(len(a))
    print(*a, sep = ' ')