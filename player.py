import pygame as pg


class Player:
    def __init__(self, id):
        self.name = ""
        self.move = []
        self.previous_action = "Not ready"
        self.money = 150
        self.seat = self.initilize_seat(id)
        self.player_border_rect = self.initilize_sprite()
        self.deck = []

    # Add card to deck
    def add_card(self, card):
        self.deck.append(card)

    # Print deck
    def print_deck(self):
        for card in self.deck:
            print(card.number, card.suit)

    # Initilize the position where each player will be sitting
    def initilize_seat(self, id):
        seat_positions = [(200, 350), (0, 200), (200, 40), (400, 200)]
        return seat_positions[id]

    # Initilize the player sprite
    def initilize_sprite(self):
        return pg.Rect(self.seat[0], self.seat[1], 100, 60)
