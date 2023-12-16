import pygame as pg
from server.vector import Vector


class ViewCards:
    def __init__(self, width):
        self.proccess = []
        self.current_process = None
        self.viewing_cards = False
        self.width = width
        self.end_card_width = 200
        self.end_card_height = 280
        self.card_width = 40
        self.card_height = 60
        self.card_start_height = 60
        self.card_start_width = 40
        self.left_end_angle = 20
        self.right_end_angle = -20
        self.left_end_position = Vector(width / 2 - 150, 600)
        self.right_end_position = Vector(width / 2 - 100, 600)
        self.tick = 0
        self.cards_initilized = False

    # Initilize the card positions
    def initilize_cards(self, player_cards):
        self.left_card_position = player_cards[0].position
        self.right_card_position = player_cards[1].position
        self.left_start_card_position = player_cards[0].position
        self.right_start_card_position = player_cards[1].position
        self.left_angle = player_cards[0].angle
        self.right_angle = player_cards[0].angle
        self.left_start_angle = player_cards[0].angle
        self.right_start_angle = player_cards[0].angle

        self.cards_initilized = True

    def check_if_done(self):
        if self.current_process == 1:
            if abs(self.tick - 1) <= 0.5:
                self.current_process = None
                self.tick = 0
        elif self.current_process == 2 or self.current_process == 4:
            if abs(self.card_width - self.end_card_width / 10) <= 5:
                self.current_process = None
                self.tick = 0
        elif self.current_process == 3 or self.current_process == 5:
            if abs(self.card_width - self.end_card_width) <= 0.5:
                self.current_process = None
                self.tick = 0
        elif self.current_process == 6:
            if abs(self.tick - 1) <= 0.5:
                self.current_process = None
                self.tick = 0
                self.viewing_cards = False
