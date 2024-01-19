P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = "abcdefghijklmnopqrstuvwxyz"

t = int(input())
for i in range(t): 
    s, k = [t for t in input().split()]
    k = int(k)
    ans = ''
    if s.isupper():
        for j in range(len(s)):
            ans += P[((P.find(s[j])) + k) % 26] 
        print(ans)
    else: 
        for j in range(len(s)):
            ans += p[((p.find(s[j])) + k) % 26] 
        print(ans)
        
    