while True:
    a = [int(x) for x in input().split()]
    if a == [0, 0, 0, 0]: break
    count = 0
    while not (a[0] == a[1] and a[1] == a[2] and a[2] == a[3]):
        tmp = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - tmp)
        count += 1
    print(count)