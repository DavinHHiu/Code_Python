file1 = open('DATA1.in', 'r')
file2 = open('DATA2.in', 'r')
set1 = []
set2 = []

for x in file1:
    for i in x.split():
        if i.lower() not in set1: set1.append(i.lower())

for x in file2:
    for i in x.split():
        if i.lower() not in set2: set2.append(i.lower())

set1.sort() 
set2.sort()

for x in set1:
    if x not in set2: print(x, end = ' ')
print()
for x in set2:
    if x not in set1: print(x, end = ' ')