s1 = input()
s2 = input()
n = int(input())
ans = s1[:n - 1] + s2 + s1[n - 1:]
print(ans)