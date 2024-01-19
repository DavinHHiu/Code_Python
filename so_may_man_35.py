s = input()
count = 0
for c in s:
    if c == '3' or c == '5': count += 1

if count == 5 or count == 3: print("YES")
else: print("NO")