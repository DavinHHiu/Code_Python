import math

class SoPhuc:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def cong(self, o):
        X = self.__x + o.__x
        Y = self.__y + o.__y
        return SoPhuc(X, Y)

    def nhan(self, o):
        X = self.__x * o.__x - self.__y * o.__y
        Y = self.__x * o.__y + self.__y * o.__x
        return SoPhuc(X, Y)
    
    def __str__(self):
        output = ""
        output += str(self.__x) + " "
        if self.__y > 0: output += "+ " + str(abs(self.__y)) + "i"
        else: output += "- " + str(abs(self.__y)) + "i"
        return output


t = int(input())
for x in range(t):
    a, b, c, d = [int(i) for i in input().split()]
    A = SoPhuc(a, b)
    B = SoPhuc(c, d)
    C = A.cong(B).nhan(A)
    D = A.cong(B)
    D = D.nhan(D)
    print("{}, {}".format(C, D))
    
