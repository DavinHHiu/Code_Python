from decimal import Decimal, ROUND_HALF_UP

class SinhVien:

    def __init__(self, i, ten, d1, d2, d3):
        self.__ma = 'SV' + "{:02d}".format(i)
        self.__ten = SinhVien.chuanHoa(ten)
        self.__diemTB = (d1 * 3 + d2 * 3 + d3 * 2) / 8
        self.__diemTB = Decimal(self.__diemTB).quantize(Decimal('0.01'), ROUND_HALF_UP)
        self.__xepHang = 0

    def chuanHoa(ten):
        res = ''
        for s in ten.split():
            res += s.capitalize() + ' '
        return res.strip()

    def xepHang(self, i):
        self.__xepHang = i

    def getXepHang(self):
        return self.__xepHang

    def getDiemTB(self):
        return self.__diemTB

    def __str__(self):
        return "{} {} {} {}".format(self.__ma, self.__ten, "{:.2f}".format(self.__diemTB), self.__xepHang)

n = int(input())
a = []
for i in range(n):
    a.append(SinhVien(i + 1, input(), float(input()), float(input()), float(input())))

a = sorted(a, key = lambda x: -x.getDiemTB())
a[0].xepHang(1)
print(a[0])
for i in range(1, len(a)):
    if a[i].getDiemTB() == a[i - 1].getDiemTB(): a[i].xepHang(a[i - 1].getXepHang())
    else: a[i].xepHang(i + 1)
    print(a[i])

