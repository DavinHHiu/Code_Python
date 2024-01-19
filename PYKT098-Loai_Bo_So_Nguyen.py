def isNotInt(n):
    if not n.isdigit(): return True
    if int(n) <= 2147483647 and int(n) >= -2147483648: 
        return False
    return True

file = open('DATA.in', 'r')
a = []

for x in file:
    for i in x.split():
        if isNotInt(i): a.append(i)

for x in sorted(a):
    print(x, end = ' ')
