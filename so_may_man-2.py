t = int(input())
for j in range(t):
    a = input()
    b = 5
    for i in range(len(a)):
        if(a[i] != '4' and a[i] != '7'):
            print('NO')
            b = 0
            break
    if(b == 5): print("YES")