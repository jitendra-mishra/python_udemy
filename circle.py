class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return (self.radius == other.radius
                and self.color == other.color)

circleA = Circle(10, "Red")
circleB = Circle(9, "Blue")

print(circleA < circleB)


