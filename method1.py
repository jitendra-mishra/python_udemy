class Circle:
    def __init__(self, radius):
        self._radius = radius

    def find_diameter(self):
        print(f"Diameter: {self._radius * 2}")

my_circle = Circle(10)
my_circle.find_diameter()
Circle.find_diameter(my_circle)