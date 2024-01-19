t = int(input())
vanBan = ''
for i in range(t):
    s = input().lower()
    for c in s:
        if c == ',' or c == '.' or c == '?' or c == '!' or c == ':' or c == ';' or c == "-" or c == '/':
            vanBan += ' '
        else: vanBan += c
tS = [str(x) for x in vanBan.split()]
for x in sorted(tS):
    print(f'{x} {tS.count(x)}')