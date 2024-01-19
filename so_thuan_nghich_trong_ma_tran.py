n, m = map(int, input().split())
a = [[]] * n
maxTN, ok, t = - 10 ** 4, 1, 0

def checkTN(n):
    s = str(n)
  
    if len(s) < 2: return False
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]: return False
    return True

for i in range(n):
    a[i] = [int(x) for x in input().split()]
    for x in a[i]:
        if checkTN(x):
            maxTN = max(maxTN, x)

for i in range(n):
    for j in range(m):
        if a[i][j] == maxTN:
            if t == 0:
                ok = 0
                print(a[i][j])
                t = 1
            print(f'Vi tri [{i}][{j}]')
if ok: print("NOT FOUND")


