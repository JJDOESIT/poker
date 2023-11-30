

class Player:
    def __init__(self):
        self.money = 150
        self.seat = None
        self.deck = []
        self.sprite = None

    # Add card to deck     
    def add_card(self, card):
        self.deck.append(card)

    # Print deck
    def print_deck(self):
        for card in self.deck:
            print(card.number, card.suit)

    