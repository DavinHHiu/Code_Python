n = int(input())
daySo = [int(i) for i in input().split()]
for i in range(1, 30002):
    if i not in daySo:
        print(i)
        break
