n, m = map(int, input().split())
a = [int(x) for x in input().split()]
mark = [0] * (m + 1)

for x in a:
    mark[x] += 1

Max = max(mark)
res = 0
ans = 0
for i in range(0, len(mark)):
    if mark[i] < Max and mark[i] > res:
        res = mark[i]
        ans = i
if res == 0: print("NONE")
else: print(ans)

