class MatHang:

    def __init__(self, ma, ten, soLuong, donGia, chietKhau):
        self.__ma = ma
        self.__ten = ten
        self.__soLuong = soLuong
        self.__donGia = donGia
        self.__chietKhau = chietKhau
        self.__tongTien = soLuong * donGia - chietKhau

    def getTongTien(self):
        return self.__tongTien

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.__ma, self.__ten, self.__soLuong, self.__donGia, self.__chietKhau, self.__tongTien)

n = int(input())
a = []
for i in range(n):
    a.append(MatHang(input(), input(), int(input()), int(input()), int(input())))

a = sorted(a, key = lambda x: -x.getTongTien())
print(*a, sep = '\n')