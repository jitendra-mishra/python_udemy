class Pizza:
    def __init__(self):
        self.toppings = []

    def add_toppings(self, topping):
        self.toppings.append(topping.lower())
        return self

    def display_toppings(self):
        print("This Pizza has: ")
        for topping in self.toppings:
            print(topping.capitalize())

my_pizza = Pizza()
my_pizza.add_toppings("Chilli") \
    .add_toppings("Pepper") \
    .add_toppings("Souce")\
    .add_toppings("Chicken")\
    .display_toppings()
my_pizza.display_toppings()
