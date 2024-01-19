class ThiSinh:

    def __init__(self, ten, ngaySinh, d1, d2, d3):
        self.__ten = ten
        self.__ngaySinh = ngaySinh
        self.__d1 = d1
        self.__d2 = d2
        self.__d3 = d3
        self.__tong = d1 + d2 + d3
    
    def __str__(self):
        return "{} {} {}".format(self.__ten, self.__ngaySinh, "{:.1f}".format(self.__tong))

thisinh = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
print(thisinh)
