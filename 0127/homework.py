# 1
# class Circle:
#     pi = 3.14

#     def __init__(self, r, x, y):
#         self.r = r
#         self.x = x
#         self.y = y

#     def area(self):
#         return Circle.pi * self.r * self.r

#     def circumference(self):
#         return 2 * Circle.pi * self.r

#     def center(self):
#         return (self.x, self.y)

# c1 = Circle(3, 2, 4)
# c1.area()
# c1.circumference()
# c1.center()

# print(c1.area())
# print(c1.circumference())
# print(c1.center())



# 2
from tkinter import N


class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')
    
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()