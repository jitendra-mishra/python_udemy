class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change
    def move_down(self, change=5):
        self.y -= change
    def move_right(self, change=2):
        self.x += change
    def move_left(self, change=2):
        self.x -= change

my_player = Player(5,10)
my_player.move_up(1)
print(f"X={my_player.x} and Y={my_player.y}")