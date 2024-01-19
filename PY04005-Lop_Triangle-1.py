import math

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, o):
        X = self.__x - o.__x
        Y = self.__y - o.__y
        return math.sqrt(X * X + Y * Y)

class Triangle:

    def __init__(self, A, B, C):
        self.__A = A
        self.__B = B
        self.__C = C
    
    def perimeter(self):
        a = self.__A.distance(self.__B)
        b = self.__B.distance(self.__C)
        c = self.__C.distance(self.__A)
        if a + b <= c or a + c <= b or b + c <= a : print('INVALID')
        else : print('{:.3f}'.format(a + b + c))

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for x in range(t):
    triangle = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
    triangle.perimeter()
    i += 6
