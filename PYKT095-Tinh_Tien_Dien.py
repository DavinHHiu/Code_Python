dinhMuc = [100, 500, 200]

class KhachHang:

    def __init__(self, i, ten, info):
        self.__ma = 'KH' + "{:02d}".format(i)
        self.__ten = KhachHang.chuanHoa(ten)
        self.__loai = info[0]
        self.__chiSoDau = int(info[1])
        self.__chiSoSau = int(info[2])
        self.__soDien = self.__chiSoSau - self.__chiSoDau 
        self.__dinhMuc = dinhMuc[ord(self.__loai) - ord('A')]
        if self.__soDien < self.__dinhMuc: self.__tienTrongDM = self.__soDien * 450
        else: self.__tienTrongDM = self.__dinhMuc * 450
        if self.__soDien > self.__dinhMuc: self.__tienVuotDM = (self.__soDien - self.__dinhMuc) * 1000
        else: self.__tienVuotDM = 0
        self.__thueVAT = 0.05 * self.__tienVuotDM
        self.__tongTien = self.__tienTrongDM + self.__tienVuotDM + self.__thueVAT

    def chuanHoa(ten):
        res = ''
        for s in ten.split():
            res += s.capitalize() + ' '
        return res.strip()

    def getTongTien(self):
        return self.__tongTien

    def __str__(self): 
        return "{} {} {} {} {} {}".format(self.__ma, self.__ten, self.__tienTrongDM, self.__tienVuotDM, int(self.__thueVAT), int(self.__tongTien))

n = int(input())
a = []
for i in range(n):
    ten = input()
    info = input().split()
    a.append(KhachHang(i + 1, ten, info))

a = sorted(a, key = lambda x: -x.getTongTien())
print(*a, sep = '\n')
    
        
