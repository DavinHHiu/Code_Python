t = int(input())
for i in range(t):
    n, p = [int(x) for x in input().split()]
    count = 0
    for i in range(1, n + 1):
        while i % p == 0:
            i /= p
            count += 1
    print(count)