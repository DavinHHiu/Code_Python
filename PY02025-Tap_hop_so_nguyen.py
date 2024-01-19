n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
s1 = set(a)
s2 = set(b)
for x in sorted(s1.intersection(s2)):
    print(x, end = ' ')
print()
for x in sorted(s1.difference(s2)):
    print(x, end = ' ')
print()
for x in sorted(s2.difference(s1)):
    print(x, end = ' ')