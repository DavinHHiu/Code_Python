import math

class Point:
    def __init__(self, s):
        self.toaDo = [int(x) for x in s.split()]
    def tinhKhoangCach(self, o):
        res = 0
        for i in range(len(self.toaDo)):
            res += (self.toaDo[i] - o.toaDo[i]) * (self.toaDo[i] - o.toaDo[i])
        return math.sqrt(res)
    def tinhTichVoHuong(self, o):
        res = 0
        for i in range(len(self.toaDo)):
            res += (self.toaDo[i] * o.toaDo[i]) 
        return res

t = int(input())
for i in range(t):
    x = Point(input())
    y = Point(input())
    ans = str(round(x.tinhKhoangCach(y), 2))
    for i in range(len(ans)):
        if ans[i] == '.' and  i + 1 == len(ans) - 1: 
           ans += '0'
    print(ans, end = ' ')
    print((x.tinhTichVoHuong(y)))
