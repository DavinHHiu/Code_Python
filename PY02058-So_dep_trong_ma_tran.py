n, m = map(int, input().split())
a = [[]] * n
Max, Min, ok, t = - 10 ** 4, 10 ** 5, 0, 0

for i in range(n): 
    a[i] = [int(x) for x in input().split()]
    Max = max(Max, max(a[i]))
    Min = min(Min, min(a[i]))

for i in range(n):
    for j in range(m):
        if a[i][j] == Max - Min:
            if t == 0:
                ok = 1
                print(Max - Min)
                t = 1
            print(f'Vi tri [{i}][{j}]')
if ok == 0: print('NOT FOUND')

