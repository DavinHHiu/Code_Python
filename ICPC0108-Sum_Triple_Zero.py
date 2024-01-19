t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    a.sort()
    for i in range(n - 1):
        for j in range(n):
            if -(a[i] + a[j]) in a: count += 1
    print(count // 3)