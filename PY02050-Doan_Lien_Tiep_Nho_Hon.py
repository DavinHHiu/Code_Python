t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    st = [-1]
    for i in range(n):
        while st[-1] != -1 and a[st[-1]] <= a[i]: st.pop()
        print(i - st[-1], end = ' ')
        st.append(i)
    print()
