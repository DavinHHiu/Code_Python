n = int(input())
ok, a, ans = 0, [], []

for i in range(n):
    s = input().split()
    if len(a) == 0 and len(s) == 6: ans.append(1)
    a.append(s)
    if len(a) > 1 and len(s) == 6 and len(a[-2]) == 7: ans.append(1)
    if len(s) == 7: ok += 1
    if ok == 4: 
        ans.append(2)
        ok = 0
    
print(len(ans))
for x in ans: 
    print(x)
