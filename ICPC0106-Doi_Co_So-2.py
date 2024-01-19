import math

d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

t = int(input())

for i in range(t):
    n = int(input())
    n = int(math.log(n) / math.log(2))
    s = input()
    while len(s) % n != 0: s = '0' + s
    for i in range(0, len(s), n):
        id = 0
        for j in range(i, i + n):
            if s[j] == '1': 
                id += pow(2, n - j + i - 1)
        print(d[id], end = '')
    print()
