n = int(input())
dSo = []
for i in range(n):
    s = input()
    sum = ""
    for x in s:
        if x.isdigit():
            sum += x
        else:
            if sum != "": dSo.append(int(sum))
            sum = ""
    if sum != "": dSo.append(int(sum))
for x in sorted(dSo):
    print(x)