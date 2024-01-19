s = input()
count = 0
res = ""
dao = s[::-1]
for i in range(0, len(dao)):
    res += dao[i]
    count += 1
    if(count == 3 and i < len(dao) - 1):
        res += ","
        count = 0
print(res[::-1])
