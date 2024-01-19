def trans(n):
    if n > 38: return 9.0
    if n > 36: return 8.5
    if n > 34: return 8.0
    if n > 32: return 7.5
    if n > 29: return 7.0
    if n > 26: return 6.5
    if n > 22: return 6.0
    if n > 19: return 5.5
    if n > 15: return 5.0
    if n > 12: return 4.5
    if n > 9: return 4.0
    if n > 6: return 3.5
    if n > 4: return 3.0
    return 2.5

t = int(input())
for i in range(t): 
    a = [x for x in input().split()]
    r, l = trans(int(a[0])), trans(int(a[1]))
    s, w = float(a[2]), float(a[3])
    res = (r + l + s + w) / 4.0
    if res - int(res) >= 0.75: res = int(res) + 1.0
    elif res - int(res) >= 0.25: res = int(res) + 0.5
    else: res = int(res)
    print(float(res)) 
