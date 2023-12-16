import pygame as pg


class Player:
    def __init__(self, id):
        self.name = ""
        self.move = []
        self.previous_action = "Not ready"
        self.money = 150
        self.bet = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0}
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
        seat_positions = [(755, 670), (250, 415), (755, 160), (1250, 415)]
        return seat_positions[id]

    # Initilize the player sprite
    def initilize_sprite(self):
        return pg.Rect(self.seat[0], self.seat[1], 100, 70)

    # Add a move
    def add_move(self, type: str, data: list = None):
        self.move.append(type)
        if data is not None:
            self.move.append(data)

    # Return the total player bet
    def get_total_bet(self):
        total = 0
        for key, value in self.bet.items():
            total += (key * value)
        return total

    # Reset move
    def reset_move(self):
        self.move = []

    # Reset the deck
    def reset_deck(self):
        self.deck = []
