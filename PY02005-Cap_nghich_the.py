"""Main"""
t = int(input())
a = [int(t) for t in input().split()]
count = 0
for i in range(t - 1):
    for j in range(i + 1, t):
        if a[i] > a[j]: count += 1
print(count)