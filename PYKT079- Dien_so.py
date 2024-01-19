t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    for j in range(min(a), max(a)):
        if j not in a: count += 1
    print(count)