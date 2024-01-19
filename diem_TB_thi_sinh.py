class ThiSinh:
    def __init__(self, name, dob, t1, t2, t3):
        self.__name = name
        self.__dob = dob
        self.__t1 = t1
        self.__t2 = t2
        self.__t3 = t3
        self.TB = 0
        Min = min(self.__t1, self.__t2, self.__t3)
        if self.__t1 != Min: self.TB += self.__t1
        if self.__t2 != Min: self.TB += self.__t2
        if self.__t3 != Min: self.TB += self.__t3
        self.TB += Min * 2
        self.TB /= 4
    def __str__(self):
        return '{} {} {}'.format(self.__name, self.__dob, "%.1f"%(self.TB))

t = int(input())
a = []
for i in range(t):
    ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    a.append(ts)
a.sort(key = lambda x: -x.TB)
for x in a:
    print(x)

