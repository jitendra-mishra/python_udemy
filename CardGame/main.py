from Deck import Deck
from Player import Player
from war_card_game import WarCardGame

player = Player("Jitu", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)

deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_msg()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("Do you want nextx round? Press Enter to continue or X to quit")
    if answer.lower() == "x":
        break


