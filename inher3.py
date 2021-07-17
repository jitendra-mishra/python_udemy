class Polygon:
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

    def describe_polygon(self):
        print(f"This polygon has {self.num_sides} sides and it's {self.color}")


class Triangle(Polygon):
    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height)/2

class Square(Polygon):
    NUM_SIDES = 4
    def __init__(self, side_length, color):
        Polygon.__init__(self, Square.NUM_SIDES, color)
        self.side_length = side_length
    def area(self):
       return (self.side_length**2)

my_triangle = Triangle(5,4, "red")
my_triangle.describe_polygon()
print(my_triangle.area())

my_square = Square(4, "blue")
my_square.describe_polygon()
print(my_square.area())