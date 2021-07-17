class Polygon:
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle(Polygon):
    NUM_SIDE = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDE, color)
        self.base = base
        self.height = height


my_triangle = Triangle(5, 4, "Blue")
print(my_triangle.color)
print(my_triangle.num_sides)
