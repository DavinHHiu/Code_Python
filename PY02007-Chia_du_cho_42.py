l = 0
count = 0
b = [0] * 42
while True:
    a = [int(x) for x in input().split()]
    l += len(a)
    for i in a:
        b[i % 42] = 1
    if l == 10: break
for i in b:
    if i == 1: count += 1
print(count)