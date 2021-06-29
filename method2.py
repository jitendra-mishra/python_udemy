class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please enter a string")

    def remove_item(self, item):
        if item in self.items:
            self._items.remove(item)
            return 1
        else:
            print("Please enter a string")
            return 0

    def has_item(self, item):
        return item in self._items


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.add_items("Water bottle")
print(my_backpack.items)
my_backpack.add_items("Sleeping bag")
print(my_backpack.items)

print(my_backpack.has_item("Water bottle"))

my_backpack.remove_item("Water bottle")
print(my_backpack.items)
print(my_backpack.remove_item("Bag"))
