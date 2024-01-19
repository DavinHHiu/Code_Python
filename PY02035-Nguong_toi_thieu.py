s = input()
k = int(input())
s1 = set()
dic = dict()
check = 1

for i in range(0, len(s), 2):
    if i == len(s) - 1: break
    if s[i:i + 2] in dic: dic[s[i:i + 2]] += 1
    else: dic[s[i:i + 2]] = 1

for x in sorted(dic):
    if dic[x] >= k: 
        print(x, dic[x])
        check = 0
if check: print("NOT FOUND")
