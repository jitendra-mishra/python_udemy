from math import pi
from random import randint as randomsix

class Circle:
    """Doc for class"""
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        """Find the area of a Circle"""
        print(randomsix(1, 10))
        return pi * (self.radius ** 2)

my_circle = Circle(10)
my_circle.find_area()

print(Circle.__doc__)

print(len.__doc__)