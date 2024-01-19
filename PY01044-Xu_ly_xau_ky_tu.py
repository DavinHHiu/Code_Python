st = {x for x in input().lower().split()}
s = {x for x in input().lower().split()}
for c in sorted(st.union(s)):
    print(c.lower(), end = ' ')
print()
for c in sorted(st.intersection(s)):
    print(c.lower(), end = ' ')