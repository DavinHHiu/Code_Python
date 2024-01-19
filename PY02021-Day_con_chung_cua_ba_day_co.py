t = int(input())
while t > 0:
    m, n, k = map(int, input().split())
    l1, l2, l3, ok = 0, 0, 0, 0
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    while l1 < m and l2 < n and l3 < k:
        if a[l1] == b[l2] and b[l2] == c[l3]:
            print(a[l1], end = ' ')
            ok = 1
            l1 += 1
            l2 += 1
            l3 += 1
        elif a[l1] < b[l2]: l1 += 1
        elif b[l2] < c[l3]: l2 += 1
        elif c[l3] < a[l1]: l3 += 1
    if ok == 0: print('NO')
    else: print()
    t -= 1