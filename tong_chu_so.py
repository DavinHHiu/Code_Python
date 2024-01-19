count = 0
def tongCS(s, count):
    if len(s) == 1: 
        print(count)
        return
    sum = 0
    for c in s:
        sum += ord(c) - ord('0')
    return tongCS(str(sum), count + 1)

tongCS(input(), count)
