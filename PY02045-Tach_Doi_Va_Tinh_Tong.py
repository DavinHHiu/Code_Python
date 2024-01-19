def process(n):
    if len(n) == 1: return
    sum = int(n[:len(n) // 2]) + int(n[len(n) // 2:])
    print(sum)
    process(str(sum))

process(input())