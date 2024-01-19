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

    def __init__(self, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def area(self):
        a = self.__p1.distance(self.__p2)
        b = self.__p2.distance(self.__p3)
        c = self.__p1.distance(self.__p3)
        if a + b <= c or a + c <= b or b + c <= a: print("INVALID")
        else: print("{:.2f}".format(math.sqrt((a + b + c)*(a + b - c)*(a - b + c)*(-a + b + c)) / 4))

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for x in range(t):
    triangle = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
    triangle.area()
    i += 6

    

