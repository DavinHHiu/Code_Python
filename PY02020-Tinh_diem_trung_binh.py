n = int(input())
a = [float(x) for x in input().split()]
max = max(a)
min = min(a)
sum = 0
count = 0
for i in a:
    if i != max and i != min:
        sum += i
        count += 1
print("{:.2f}".format(sum / count))