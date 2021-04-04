class Shape:
    def Area(self):
        area = 0
        print('Area of Shape is:', area)

class Square(Shape):
    def __init__(self,length):
        self.length = length
        print('Length of Square is:',self.length)

    def area(self):
        a = self.length * self.length
        print('Area is:',a)

a = Shape()
a.Area()

b = Square(4)
b.area()
