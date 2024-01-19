n = int(input())
a = []
while True:
    x = [int(x) for x in input().split()]
    a += x
    if len(a) == n : break 
    
c = []
l = []

for x in a:
    if x % 2 == 0: c.append(x)
    else: l.append(x)

c.sort()
l.sort(reverse = True)
i, j = 0, 0

for x in a:
    if x % 2 == 0: 
        print(c[i], end = ' ')
        i += 1
    else: 
        print(l[j], end = ' ')
        j += 1