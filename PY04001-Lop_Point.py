import math
from decimal import Decimal

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def distance(self, o):
        X = self.__x - o.__x
        Y = self.__y - o.__y
        res = math.sqrt(X * X + Y * Y)
        return "{:.4f}".format(res)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1