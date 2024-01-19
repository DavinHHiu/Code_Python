isNT = [0] * (10**6 + 5)

def sangNT():
    for i in range(2, 1000):
        if isNT[i] == 0:
            for j in range(i * i, 10 ** 6 + 1, i):
                isNT[j] = 1
            
sangNT()
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(1, n):
        if isNT[i] == 0:
            k = int(str(i)[::-1])
            if k > i and k < n and isNT[k] == 0:
                print(i, k, end = ' ')
    print()
