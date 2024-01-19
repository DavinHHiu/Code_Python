def trans_a_to_b(s1, s2, a, b):
    new_s1 = ""
    new_s2 = ""
    for c in s1:
        if c == chr(a + 48): new_s1 += chr(b + 48)
        else: new_s1 += c
    for c in s2:
        if c == chr(a + 48): new_s2 += chr(b + 48)
        else: new_s2 += c
    return int(new_s1) + int(new_s2)
"""Main"""
t = int(input())
while(t > 0):
    p, q = map(int, input().split())
    try:
        s1 = input()
        s2 = input()
        if(p < q): print(trans_a_to_b(s1, s2, q, p), trans_a_to_b(s1, s2, p, q))
        else: print(trans_a_to_b(s1, s2, p, q), trans_a_to_b(s1, s2, q, p))
    except:
        s1, s2 = map(str, input().split())
        if(p < q): print(trans_a_to_b(s1, s2, q, p), trans_a_to_b(s1, s2, p, q))
        else: print(trans_a_to_b(s1, s2, p, q), trans_a_to_b(s1, s2, q, p))
    t -= 1