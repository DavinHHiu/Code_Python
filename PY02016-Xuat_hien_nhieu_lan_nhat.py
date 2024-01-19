"""Main"""
t = int(input())
while t > 0:
    n = int(input())
    lst = [int(x) for x in input().split()]
    danhDau = [0] * 10 ** 5
    max = 0
    phan_tu = -5
    for i in lst:
        danhDau[i] += 1
    for i in range(len(danhDau)):
        if danhDau[i] > max:
            max = danhDau[i]
            phan_tu = i
    if max > n // 2: print(phan_tu)
    else: print("NO")
    t -= 1
    