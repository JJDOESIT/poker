from card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.generate_deck()
        self.shuffle_deck()

    # Generate a deck of 52 cards
    def generate_deck(self):
        for number in range(13):
            for suit in range(4):
                self.deck.append(Card(number, suit))

    # Shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.deck)

    # Draw a card from the deck
    def draw_card(self):
        return self.deck.pop(random.randrange(0, len(self.deck)))

    # Print the deck
    def print_deck(self):
        for card in self.deck:
            print(card.number, card.suit)
