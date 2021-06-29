class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("Calling getter")
        return self._items

    @items.setter
    def items(self, new_items):
        print("Calling setter")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Enter a list")

my_back = Backpack()
print(my_back.items)
my_back.items = ["Water bottle", "sleeping bag"]
print(my_back.items)

