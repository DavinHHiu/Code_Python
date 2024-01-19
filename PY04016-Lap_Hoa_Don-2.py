from datetime import datetime

giaTang = [0, 25, 34, 50, 80]

class KhachHang:

    def __init__(self, id, ten, maPhong, ngayDen, ngayDi, tienDVphatSinh):
        self.__id = 'KH' + "{:02d}".format(id)
        self.__ten = ten
        self.__maPhong = maPhong
        self.__ngayO = str(datetime.strptime(ngayDi, '%d/%m/%Y') - datetime.strptime(ngayDen, '%d/%m/%Y')).split()[0]
        if self.__ngayO == '0:00:00': self.__ngayO = 1
        else: self.__ngayO = int(self.__ngayO) + 1
        self.__tien = giaTang[int(self.__maPhong[0])] * self.__ngayO + tienDVphatSinh

    def getTongTien(self):
        return self.__tien

    def __str__(self):
        return "{} {} {} {} {}".format(self.__id, self.__ten, self.__maPhong, self.__ngayO, self.__tien)

n = int(input())
a = []
for i in range(n):
    a.append(KhachHang(i + 1, input(), input(), input().strip(), input().strip(), int(input())))

a = sorted(a, key = lambda x: -x.getTongTien())
for x in a:
    print(x)

        