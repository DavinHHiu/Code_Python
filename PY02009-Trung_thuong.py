t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    st = set()
    val = -1
    max = 0
    for x in sorted(a):
        if x in st: continue
        else: 
            st.add(x)
            if a.count(x) > max:
                max = a.count(x)
                val = x
    print(val)
