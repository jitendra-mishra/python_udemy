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
    def add_multiple_items(self, items):
        for item in items:
            self.add_items(item)

    def remove_item(self, item):
        if item in self.items:
            self._items.remove(item)
            return 1
        else:
            print("Please enter a string")
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)



my_backpack = Backpack()
my_backpack.add_items("Water")
my_backpack.add_items("Bag")
my_backpack.add_items("Pen")
my_backpack.add_multiple_items(["z", "b"])
#print(my_backpack.items)
#my_backpack.add_items("Water bottle")
#print(my_backpack.items)
#my_backpack.add_items("Sleeping bag")
#print(my_backpack.items)

#print(my_backpack.has_item("Water bottle"))
print("Before sorting")
my_backpack.show_items()
print("After sorting")
my_backpack.show_items(True)
#my_backpack.remove_item("Water bottle")
#print(my_backpack.items)
#print(my_backpack.remove_item("Bag"))
