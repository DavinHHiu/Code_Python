def thuanNghich(s):
    if len(s) < 2: return False
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]: return False
    return True

n, m = map(int, input().split())
a = [[]] * n
for i in range(n): a[i] = [int(x) for x in input().split()]
Max = 0

for i in range(n):
    for j in range(m):
        if thuanNghich(str(a[i][j])) and a[i][j] > Max:
            Max = a[i][j]

if Max == 0: print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max: print(f'Vi tri [{i}][{j}]')


