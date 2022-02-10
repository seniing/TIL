
from turtle import width


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.sq_width = abs(self.p1.x - self.p2.x) # 사각형 가로의 길이
        self.sq_length = abs(self.p1.y - self.p2.y) # 사각형 세로의 길이

    def get_area(self):
        # 넓이 = 가로 * 세로
        return self.sq_width * self.sq_length

    def get_perimeter(self):
        # 길이 = (가로 + 세로) * 2
        return (self.sq_width + self.sq_length) * 2

    def is_square(self):
        # 정사각형 : 가로의 길이 == 세로의 길이
        if self.sq_width == self.sq_length:
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())