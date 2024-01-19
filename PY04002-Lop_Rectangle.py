class Rectangle:
    def __init__(self, w, h, color):
        self.__w = w
        self.__h = h
        self.__color = color[0].upper() + color[1:].lower() 
    def perimeter(self):
        return (self.__w + self.__h) * 2
    def area(self):
        return self.__w * self.__h;
    def color(self):
        return self.__color 
    
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else: print('INVALID')