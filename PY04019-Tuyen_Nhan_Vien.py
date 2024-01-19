from decimal import Decimal, ROUND_HALF_UP

class NhanVien:

    def __init__(self, i, ten, d1, d2):
        self.__maNV = 'TS0' + str(i)
        self.__ten = ten
        if d1 > 10: d1 /= 10
        if d2 > 10: d2 /= 10
        self.__diemTB = (d1 + d2) /2
        if self.__diemTB > 9.5: self.__xepHang = "XUAT SAC"
        elif self.__diemTB >= 8: self.__xepHang = "DAT"
        elif self.__diemTB >= 5: self.__xepHang = "CAN NHAC"
        else: self.__xepHang = "TRUOT"

    def getDiemTB(self):
        return self.__diemTB

    def __str__(self): 
        return "{} {} {} {}".format(self.__maNV, self.__ten, "{:.2f}".format(self.__diemTB), self.__xepHang)

n = int(input())
a = []
for x in range(n):
    ten = input()
    d1 = Decimal(input())
    d2 = Decimal(input())
    a.append(NhanVien(x + 1, ten, d1, d2))

a = sorted(a, key = lambda x: -x.getDiemTB())
for x in a: 
    print(x)