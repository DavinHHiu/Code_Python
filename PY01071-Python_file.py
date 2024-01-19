def check(s):
    for c in s:
        if not c.isalpha() and c != '_' and c != '.':
            return False
    return True

s = input()
str = s.lower()
if check(str) and str[-3:] == ".py": print("yes")
else: print("no")