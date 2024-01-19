a = []
b = ['0', '2', '4', '6', '8']

def Try(s):
    t = list(s)
    t.reverse()
    t = int(s + ''.join(t))
    global a
    a.append(t)
    if len(s) != 3:
        for i in b: Try(s + i)
for i in range(1, 5): Try(b[i])
a.sort()

t = int(input())
for i in range(t):
    n = int(input())
    for x in a:
        if x < n: print(x, end = ' ')
        else: break
    print()