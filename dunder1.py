class Backpack:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item doesn't exist")
    def __len__(self):
        return len(self.items)

my_backpack = Backpack()
my_backpack.add_item("Tissue")
my_backpack.add_item("Water Bottle")
my_backpack.add_item("Sleeping bag")
print(len(my_backpack))
my_backpack.remove_item("Tissue")
print(len(my_backpack))