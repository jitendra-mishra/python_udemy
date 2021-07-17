class Character:

    def __init__(self, x, y, num_lives):
        self.x = x
        self.y = y
        self.num_lives = num_lives


class Player(Character):

    INITIAL_X = 0
    INITIAL_Y = 0
    INITIAL_LIVES = 10

    def __init__(self, score=0):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y,
                           Player.INITIAL_LIVES)
        self.score = score


class Enemy(Character):

    def __init__(self, x=15, y=15, num_lives=8, is_poisonous=False):
        Character.__init__(self, x, y, num_lives)
        self.is_poisonous = is_poisonous


my_player = Player()
print(my_player.x, my_player.y, my_player.num_lives, my_player.INITIAL_LIVES)

easy_enemy = Enemy(num_lives=1)
hard_enemy = Enemy(num_lives=54, is_poisonous=True)

print(easy_enemy.x, easy_enemy.y, easy_enemy.num_lives, easy_enemy.is_poisonous)

print(hard_enemy.x, hard_enemy.y, hard_enemy.num_lives, hard_enemy.is_poisonous)
