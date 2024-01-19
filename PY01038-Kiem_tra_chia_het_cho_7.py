def chia(n):
    t = 1000
    while(t > 0):
        if int(n) % 7 == 0: return n
        sum = int(n) + int(n[::-1])
        n = str(sum)
        if sum % 7 == 0: return sum
        t -= 1
    return -1

"""Main"""
t = int(input())
while t > 0:
    n = input()
    print(chia(n))
    t -= 1