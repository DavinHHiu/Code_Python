import math

class PhanSo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def toiGian(self):
        GCD = math.gcd(self.__x, self.__y)
        self.__x = int(self.__x / GCD)
        self.__y = int(self.__y / GCD)
    def __str__(self):
        return "{}/{}".format(self.__x, self.__y)

a, b = [int(x) for x in input().split()]
ps = PhanSo(a, b)
ps.toiGian()
print(ps)
