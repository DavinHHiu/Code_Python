import math

class PhanSo:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def toiGian(self):
        GCD = math.gcd(self.__x, self.__y)
        self.__x = int(self.__x / GCD)
        self.__y = int(self.__y / GCD) 

    def cong(self, o):
        X = self.__x * o.__y + o.__x * self.__y
        Y = self.__y * o.__y
        psTong = PhanSo(X, Y)
        psTong.toiGian()
        return psTong

    def __str__(self):
        return "{}/{}".format(self.__x, self.__y)

a, b, c, d = [int(x) for x in input().split()]

ps1 = PhanSo(a, b)
ps2 = PhanSo(c, d)
print(ps1.cong(ps2))
