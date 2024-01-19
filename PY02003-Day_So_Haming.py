a = [1] * (10 ** 9)

for i in range(2, 10**18 + 1):
    if a[i] == 1:
        for i in range(i * i, 10 ** 18, i):
            a[i] == i

t = int(input())
for i in range(t):
    n = int(input())
    if a[n] == n: uocMAX = n
    else: uocMAX = n / a[n]
    if uocMAX <= 5: print(n)
    else: print('Not in sequence')
 