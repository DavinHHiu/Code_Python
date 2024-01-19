s = input()
thuong = 0
hoa = 0
for i in range(len(s)):
    if(s[i].islower()): thuong += 1
    elif(s[i].isupper()): hoa += 1 
    else: pass
if(thuong >= hoa): print(s.lower())
else: print(s.upper())