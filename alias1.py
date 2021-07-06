class Circle:

    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(4)
your_circle = my_circle

print(id(my_circle))
print(id(your_circle))