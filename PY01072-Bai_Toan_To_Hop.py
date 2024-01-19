n, k = [int(x) for x in input().split()]
a = []
c = [0] * (k + 1)

for x in input().split():
    if int(x) not in a: a.append(int(x))
n = len(a)
a.sort()

def ToHop(i):
    for j in range(c[i - 1] + 1, n - k + i + 1):
        c[i] = j
        if i == k: 
            for m in range(1, k + 1):
                print(a[c[m] - 1], end = ' ')
            print()
        else: ToHop(i + 1)

ToHop(1)
    