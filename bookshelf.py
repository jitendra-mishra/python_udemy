class Bookshelf:

    def __init__(self):
        self.content = [[],
                        [],
                        []]
    def add_book(self, book, location):
        self.content[location].append(book)
    def take_book(self, book, location):
        self.content[location].remove(book)
    def __getitem__(self, location):
        return self.content[location]

my_bookshelf = Bookshelf()

my_bookshelf.add_book("Letus C", 0)
my_bookshelf.add_book("My C++", 0)
my_bookshelf.add_book("JKC", 0)

my_bookshelf.add_book("Java1", 1)
my_bookshelf.add_book("Java2", 1)
my_bookshelf.add_book("Java3", 1)

my_bookshelf.add_book("Python1", 2)
my_bookshelf.add_book("Python2", 2)
my_bookshelf.add_book("Python3", 2)

print(my_bookshelf[4])
