class Store:
    def __init__(self, name, address, num_employees):
        self.name = name
        self.address = address
        self.num_employees = num_employees

    def greet_customers(self):
        print("Welcome to our store! What would you like to buy?")

# Create your DonutStore class below this line
class DonutStore(Store):

    def greet_customers(self):
        print("Welcome to our store!What donut would you like to eat?")

my_donut_store = DonutStore("ABC", "XYZ", 10)
