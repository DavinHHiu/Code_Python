def trans(s):
    if s == '000': return '0'
    elif s == '001': return '1'
    elif s == '010': return '2'
    elif s == '011': return '3'
    elif s == '100': return '4'
    elif s == '101': return '5'
    elif s == '110': return '6'
    elif s == '111': return '7'
s = input()
t = 3 - len(s) % 3
for i in range(t):
    s = '0' + s
ans = ''
print(s)
for i in range(0, len(s), 3):
    ans += trans(s[i:i + 3])
print(ans.lstrip('0'))