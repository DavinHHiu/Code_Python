diemUT = [1.5, 1, 0]

class ThiSinh:

    def __init__(self, i, ten, diemThi, danToc, khuVuc):
        self.__ma = 'TS' + "{:02d}".format(i)
        self.__ten = ThiSinh.chuanHoa(self, ten)
        self.__danToc = danToc
        self.__diemUT = diemUT[khuVuc - 1]
        if self.__danToc != 'Kinh': self.__diemUT += 1.5
        self.__tong = diemThi + self.__diemUT
        if self.__tong >= 20.5: self.__tinhTrang = 'Do'
        else: self.__tinhTrang = 'Truot'

    def chuanHoa(self, ten):
        res = ''
        for s in ten.split():
            res += s.capitalize() + ' '
        return res.strip()

    def getTongDiem(self):
        return self.__tong

    def getMa(self):
        return self.__ma

    def __str__(self):
        return "{} {} {} {}".format(self.__ma, self.__ten, "{:.1f}".format(self.__tong), self.__tinhTrang)

n = int(input())
a = []
for i in range(n):
    a.append(ThiSinh(i + 1, input(), float(input()), input(), int(input())))

a = sorted(a, key = lambda x: (-x.getTongDiem(), x.getMa()))
print(*a, sep = '\n')
