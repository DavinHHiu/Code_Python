def check(a, b):
    if len(a) != len(b): return False
    for i in range(len(a)):
        if a[i] != b[i]: return False
    return True

t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    a = []
    b = []
    for c in s1:
        a.append(c)
    for c in s2:
        b.append(c)
    a.sort()
    b.sort()
    print(f"Test {i + 1}:", end = ' ')
    if check(a, b): print("YES")
    else: print("NO")
