t = int(input())

for i in range(t):
    d, id = [], 1
    for c in input():
        if c == '(': 
            d.append(id)
            print(id, end = ' ')
            id += 1
        if c == ')': 
            print(d[-1], end = ' ')
            d.pop()
    print()
