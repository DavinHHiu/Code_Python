f = [0] * 93
f[0] = 0
f[1] = f[2] = 1
for i in range(3, 93):
    f[i] = f[i - 1] + f[i - 2]

t = int(input())
while t > 0:
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(f[i], "", end = '')
    print("")
    t -= 1