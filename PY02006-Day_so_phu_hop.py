def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]: return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if check(sorted(a), sorted(b)): print("YES")
    else: print("NO")