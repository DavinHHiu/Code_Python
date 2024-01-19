n = int(input())
a = [[]] * n
for i in range(n):  
    a[i] = [int(x) for x in input().split()]
k = int(input())
j = n - 1
h = n - 1
s1 = 0
s2 = 0

for i in range(n - 1):
    for l in range(j):
        s1 += a[i][l]
    j -= 1

for i in range(1, n):
    for l in range(h, n):
        s2 += a[i][l]
    h -= 1

if abs(s1 - s2) <= k: print("YES")
else: print("NO")
print(abs(s1 - s2))