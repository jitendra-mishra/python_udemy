class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("\n== Let's start the battle ==\n")
        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f"Your card:")
        player_card.show()

        print(f"Computer card:")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou Won this round")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nCopmuter won this game")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("It's a Tie, This is war!")
            self.start_war(cards_won)
        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, previous_card):
        if previous_card:
            return [player_card, computer_card] + previous_card
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_card = self._player.draw_card()
            player_cards.append(player_card)

            computer_card = self._computer.draw_card()
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("Game Over")
            return True
        elif self._computer.has_empty_deck():
            print(f"You won {self._player_name}")
            return True
        else:
            return False

    def print_stats(self):
        print(f"You have {self._player.deck.size}")
        print(f"Computer has {self._computer.deck.size}")

    def print_welcome_msg(self):
        print("Welcome to WarCardGame")





