class MonThi:

    def __init__(self, ma, ten, hinhThuc):
        self.__ma = ma
        self.__ten = ten
        self.__hinhThuc = hinhThuc

    def getMa(self):
        return self.__ma

    def __str__(self):
        return "{} {} {}".format(self.__ma, self.__ten, self.__hinhThuc)

n = int(input())
a = []
for i in range(n):
    a.append(MonThi(input(), input(), input()))

a = sorted(a, key=lambda x: x.getMa())
print(*a, sep = '\n')