st = set()

def biendoi(n):
    if n == 1:
        st.add(1)
        return
    if n % 2 == 0:
        if n / 2 in st: return
        else: 
            st.add(n / 2)
            biendoi(n / 2)
    else: 
        if n * 3 + 1 in st: return
        else:
            st.add(n * 3 + 1)
            biendoi(n * 3 + 1)

"""Main"""
while(True):
    n = int(input())
    if(n == 0): break
    st.add(n)
    biendoi(n)
    print(len(st))
    st.clear()