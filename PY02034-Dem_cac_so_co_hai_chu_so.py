s = input()
s1 = set()
dic = dict()

for i in range(0, len(s), 2):
    if i == len(s) - 1: break
    if s[i:i + 2] in dic: dic[s[i:i + 2]] += 1
    else: dic[s[i:i + 2]] = 1

for i in range(0, len(s), 2):
    if i == len(s) - 1: break
    if s[i:i + 2] in s1: continue
    else: 
        print(s[i:i + 2], dic[s[i:i + 2]])
        s1.add(s[i:i + 2])