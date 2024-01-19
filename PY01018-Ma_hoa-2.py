p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    ip = input()
    if ip == '0': break
    m, s = map(str, ip.split())
    k = int(m)
    ans = ""
    for i in range(len(s)):
        id = p.index(s[i])
        ans += p[(id + k) % 28]
    print(ans[::-1])
