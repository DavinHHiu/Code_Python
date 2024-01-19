from decimal import Decimal, ROUND_HALF_UP

class KhachHang:

    def __init__(self, id, ten, chiSoCu, chiSoMoi):
        self.__id = "KH" + "{:02d}".format(id)
        self.__ten = ten
        s = chiSoMoi - chiSoCu
        if s <= 50: 
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else: 
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.__tien = Decimal(s).quantize(Decimal(0), ROUND_HALF_UP)

    def __str__(self):
        return "{} {} {}".format(self.__id, self.__ten, self.__tien)

    def getTien(self):
        return self.__tien

n = int(input())
a = []
for i in range(n):
    ten = input()
    chiSoCu = int(input())
    chiSoMoi = int(input())
    a.append(KhachHang(i + 1, ten, chiSoCu, chiSoMoi))

a = sorted(a, key = lambda x: -x.getTien())

for x in a:
    print(x)

