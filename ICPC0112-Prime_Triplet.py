isPrime = [1] * 1000001

def Prime():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 1000):
        if isPrime[i] == 1:
            for j in range(i * i, 1000001, i):
                isPrime[j] = 0

Prime()

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for i in range(1, n - 6):
        if isPrime[i] and isPrime[i + 6] and (isPrime[i + 2] or isPrime[i + 4]):
            count += 1
    print(count)
