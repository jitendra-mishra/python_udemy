import random


class Die:

    def __init__(self, value=None):
        self.value = value

    def roll_dice(self):
        random_value = random.randint(1, 6)
        self.value = random_value

my_die = Die(value=2)
print(my_die.value)
my_die.roll_dice()
print(my_die.value)
my_die.roll_dice()
print(my_die.value)