a = input()
sum = 0
for j in range(len(a)):
    if(a[j] == '4' or a[j] == '7'): sum += 1
if(sum == 4 or sum == 7): print("YES")
else: print("NO")


