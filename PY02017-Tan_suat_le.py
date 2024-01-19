t = int(input())
for i in range(t):
    n = int(input())
    ds = [x for x in input().split()]
    dic = dict()
    for x in ds:
        if x in dic:
            dic[x] += 1
        else: dic[x] = 1
    for x in dic:
        if dic[x] % 2 == 1:
            print(x)
            break
        