def check(s1, s2):
    i = len(s1) - 1
    while i > 0:
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return False
        i -= 1
    return True

t = int(input())
for i in range(t):
    s = input() 
    if check(s, s[::-1]): print("YES")
    else: print("NO")
