t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    m = max(a)
    for i in range(n):
        if a[i] == m: 
            a.insert(i, k)
            break
    for x in a: 
        if x < 0: print(x, end = ' ')
    for x in a:
        if x >= 0: print(x, end = ' ')
    print()