class SinhVien:

    def __init__(self, ma, ten, lop):
        self.__ma = ma
        self.__ten = ten
        self.__lop = lop
        self.__diemCC = 10
        self.__ghiChu = ''

    def setDiemCC(self, s):
        for c in s:
            if c == 'v': self.__diemCC -= 2
            if c == 'm': self.__diemCC -= 1
        if self.__diemCC < 0: self.__diemCC = 0
        if self.__diemCC == 0: self.__ghiChu = 'KDDK'

    def getMa(self):
        return self.__ma

    def __str__(self):
        return "{} {} {} {} {}".format(self.__ma, self.__ten, self.__lop, self.__diemCC, self.__ghiChu)

n = int(input())
a = [] 
for i in range(n):
    a.append(SinhVien(input(), input(), input()))

for i in range(n):
    init = input().split()
    for x in a:
        if x.getMa() == init[0]: x.setDiemCC(init[1])

for x in a:
    print(x)