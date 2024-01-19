class SinhVien:

    def __init__(self, ten, soBaiDung, soBaiSubmit):
        self.__ten = ten
        self.__soBaiDung = soBaiDung
        self.__soBaiSubmit = soBaiSubmit

    def getSoBaiDung(self):
        return self.__soBaiDung

    def getSoBaiSubmit(self):
        return self.__soBaiSubmit

    def __str__(self):
        return "{} {} {}".format(self.__ten, self.__soBaiDung, self.__soBaiSubmit)

n = int(input())
a = []
for i in range(n):
    ten = input()
    soBai = input().split()
    a.append(SinhVien(ten, int(soBai[0]), int(soBai[1])))

a = sorted(a, key=lambda x: (-x.getSoBaiDung(), x.getSoBaiSubmit()))
print(*a, sep = '\n')