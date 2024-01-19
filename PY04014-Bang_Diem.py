from decimal import Decimal, ROUND_HALF_UP

class HocSinh:

    def __init__(self, i, ten, diem):
        self.__maHS = 'HS' + "{:02d}".format(i)
        self.__ten = ten
        x = 2 * diem[0] + 2 * diem[1]
        for i in range(2, 10):
            x += diem[i]
        x /= 12
        self.__diemTB = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
        if self.__diemTB >= 9: self.__xepHang = "XUAT SAC"
        elif self.__diemTB >= 8: self.__xepHang = "GIOI"
        elif self.__diemTB >= 7: self.__xepHang = "KHA"
        elif self.__diemTB >= 5: self.__xepHang = "TB"
        else: self.__xepHang = "YEU"

    def getDiemTB(self):
        return self.__diemTB

    def getMaHS(self):
        return self.__maHS

    def __str__(self):
        return "{} {} {} {}".format(self.__maHS, self.__ten, "{:1f}".format(self.__diemTB), self.__xepHang)

n = int(input())
a = []
for x in range(n):
    ten = input()
    diem = [Decimal(i) for i in input().split()]
    a.append(HocSinh(x + 1, ten, diem))

a = sorted(a, key = lambda x: (-x.getDiemTB(), x.getMaHS()))
for x in a:
    print(x)