mon = ['TOAN', 'LY', 'HOA']
diemUT = [2.0, 1.5, 1.0, 0.0]

class GiaoVien:

    def __init__(self, id, ten, ma, d1, d2):
        self.__ma = 'GV' + "{:02d}".format(id)
        self.__ten = ten
        self.__mon = mon[ord(ma[0]) - ord('A')]
        self.__diemUT = diemUT[int(ma[1]) - 1]
        self.__tong = d1 * 2 + d2 + self.__diemUT
        if self.__tong >= 18: self.__tinhTrang = 'TRUNG TUYEN'
        else: self.__tinhTrang = 'LOAI'
    def getTongDiem(self):
        return self.__tong

    def __str__(self):
        return "{} {} {} {} {}".format(self.__ma, self.__ten, self.__mon, "{:.1f}".format(self.__tong), self.__tinhTrang)

n = int(input())
a = []
for i in range(n):
    a.append(GiaoVien(i + 1, input(), input(), float(input()), float(input())))

a = sorted(a, key = lambda x: -x.getTongDiem())
print(*a, sep = '\n')

