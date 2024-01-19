import re

n = int(input())
m = {}
regex = '[\w]+'

for i in range(n):
    for x in re.findall(regex, input()):
        if x.lower() in m: m[x.lower()] += 1
        else: m[x.lower()] = 1

m = sorted(m.items(), key = lambda x: (-x[1], x[0]))
for x in m:
    print(x[0], x[1])