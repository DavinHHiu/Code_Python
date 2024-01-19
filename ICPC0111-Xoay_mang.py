t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    for i in range(k, n):
        print(a[i], end = ' ')
    for i in range(k):
        print(a[i], end = ' ')
    print()
