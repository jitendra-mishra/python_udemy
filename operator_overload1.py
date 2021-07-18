class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point2D(new_x, new_y)

    def __str__(self):
        return f"({self.x}, {self.y})"
pointA = Point2D(5, 6)
pointB = Point2D(2, 3)

pointC = pointA + pointB
print(pointA)
print(pointB)
print(pointC)