x = input()
n = len(x)
ok = [True] * 10

def hoanVi(i, s):
    if i == n: 
        print(s)
        return
    for j in range(n):
        if ok[j]:
            ok[j] = False
            hoanVi(i + 1, s + x[j])
            ok[j] = True
        
hoanVi(0, "")   