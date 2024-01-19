import re

n = int(input())
regex = '[a-z]+'
m = {}

for i in range(n):
    for x in re.findall(regex, input().lower()):
        if x in m: m[x] += 1
        else: m[x] = 1

m = sorted(m.items(), key=lambda x: (-x[1], x[0]))
for x in m: 
    print(x[0], x[1])