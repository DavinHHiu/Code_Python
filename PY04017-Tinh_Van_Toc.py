from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

class VDV:

    def __init__(self, ten, donVi, thoiDiemVeDich):
        a = [i[0] for i in donVi.split()]
        b = [i[0] for i in ten.split()]
        self.__ma = ''.join(a) + ''.join(b)
        self.__ten = ten
        self.__donVi = donVi
        thoiGian = (datetime.strptime(thoiDiemVeDich, '%H:%M') - datetime.strptime('6:00', '%H:%M')).total_seconds() / 3600
        self.__vanToc = 120 / thoiGian

    def getVanToc(self):
        return self.__vanToc

    def __str__(self):
        return "{} {} {} {} Km/h".format(self.__ma, self.__ten, self.__donVi, Decimal(self.__vanToc).quantize(Decimal(0), ROUND_HALF_UP))

n = int(input())
a = []
for i in range(n):
    a.append(VDV(input(), input(), input()))

a = sorted(a, key = lambda x: -x.getVanToc())

for x in a:
    print(x)