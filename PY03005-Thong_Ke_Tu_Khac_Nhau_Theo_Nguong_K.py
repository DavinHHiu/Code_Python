import re

n, k = [int(x) for x in input().split()]
regex = '[\w]+'
m = {}

for i in range(n):
    for x in re.findall(regex, input().lower()):
        if x in m: m[x] += 1
        else: m[x] = 1

m = sorted(m.items(), key=lambda x: (-x[1], x[0]))
for x in m:
    if x[1] >= k: print(x[0], x[1])