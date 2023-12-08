from server.card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.generate_deck()
        self.shuffle_deck()
        self.initilize_positions()

    # Generate a deck of 52 cards
    def generate_deck(self):
        for number in range(13):
            for suit in range(4):
                self.deck.append(Card(number, suit))

    # Shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.deck)

    # Initilize card positions
    def initilize_positions(self):
        for index in range(len(self.deck)):
            self.deck[index].position.x = 935 + index / 10
            self.deck[index].position.y = 420 - index / 10

    # Draw a card from the deck
    def draw_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()

    # Print the deck
    def print_deck(self):
        for card in self.deck:
            print(card.number, card.suit)
