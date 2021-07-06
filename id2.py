class Dog:

    def __init__(self, age):
        self.age = age

a = Dog(10)
b = Dog(10)

print(f"a={id(a)} and b={id(b)}")
print(a == b)