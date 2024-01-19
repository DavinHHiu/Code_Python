n = int(input())
dSo, l, Max, ok = [], 0, 0, 1

while True:
    a = [int(x) for x in input().split()]
    l += len(a)
    for x in a: 
        dSo.append(x)
        Max = max(Max, x)
    if l == n: break
for i in range(1, Max):
    if i not in dSo: 
        print(i)
        ok = 0
if ok: print('Excellent!')