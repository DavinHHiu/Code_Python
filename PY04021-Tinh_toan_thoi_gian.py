from datetime import timedelta

class GameThu:

    def __init__(self, id, ten, gioVao, gioRa):
        self.__id = id
        self.__ten = ten
        t1 = timedelta(hours = int(gioVao[0]), minutes = int(gioVao[1]))
        t2 = timedelta(hours = int(gioRa[0]), minutes = int(gioRa[1]))
        self.__thoiGian = t2 - t1

    def getTime(self):
        return self.__thoiGian

    def __str__(self):
        return "{} {} {} gio {} phut".format(self.__id, self.__ten, int(self.__thoiGian.total_seconds() / 3600), int(self.__thoiGian.total_seconds() % 3600 / 60) ) 

n = int(input())
a = []
for i in range(n):
    id = input()
    ten = input()
    gioVao = input().split(':')
    gioRa = input().split(':')
    a.append(GameThu(id, ten, gioVao, gioRa))

a = sorted(a, key = lambda x: -x.getTime())
for x in a: 
    print(x)
