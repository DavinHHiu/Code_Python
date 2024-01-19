n = int(input())
daySo = [int(t) for t in input().split()]

i = 0
while i < len(daySo) - 1:
    sum = daySo[i] + daySo[i + 1]
    if sum % 2 == 0:
        del daySo[i], daySo[i]
        if i > 0: i -= 2
        if i == 0: continue
    i += 1
print(len(daySo))