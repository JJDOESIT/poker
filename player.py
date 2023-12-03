class Player:
    def __init__(self):
        self.name = ""
        self.id = None
        self.move = []
        self.previous_action = "Not ready"
        self.money = 150
        self.seat = None
        self.deck = []
        self.player_border_rect = None

    # Add card to deck
    def add_card(self, card):
        self.deck.append(card)

    # Print deck
    def print_deck(self):
        for card in self.deck:
            print(card.number, card.suit)

    # Reset the move
    def reset_move(self):
        self.move = []

    def print_player_data(self):
        print(f"Player: {self.id}")
        print(f"Move: {self.move}")
        print(f"Previous Action: {self.previous_action}")
        print("")
        print("")
