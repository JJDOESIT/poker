import pygame as pg
from server.vector import Vector


class ViewCards:
    def __init__(self, width):
        self.width = width
        self.viewing_cards = False
        self.moving_to_hand = False
        self.flipping_to_front = False
        self.stretching_out_front = False
        self.end_card_width = 200
        self.end_card_height = 280
        self.card_width = 40
        self.card_height = 60
        self.left_end_angle = 20
        self.right_end_angle = -20
        self.left_end_position = Vector(width / 2 - 150, 600)
        self.right_end_position = Vector(width / 2 - 100, 600)
        self.position_tick = 0
        self.flipping_tick = 0
        self.cards_initilized = False

    # Initilize the card positions
    def initilize_cards(self, left_card_image, right_card_image, player_cards):
        self.left_card_position = player_cards[0].position
        self.right_card_position = player_cards[1].position
        self.left_angle = player_cards[0].angle
        self.right_angle = player_cards[0].angle

        self.left_revealed_card = left_card_image
        self.right_revealed_card = right_card_image
        self.left_revealed_card = pg.transform.scale(
            self.left_revealed_card, (self.end_card_width, self.end_card_height)
        )
        self.right_revealed_card = pg.transform.scale(
            self.right_revealed_card, (self.end_card_width, self.end_card_height)
        )

        self.cards_initilized = True

    # Check if the cards are in position
    def check_if_in_position(self):
        if self.moving_to_hand:
            left_difference = self.left_card_position - self.left_end_position
            right_difference = self.right_card_position - self.right_end_position
            if (
                abs(left_difference.x) <= 0.05
                and abs(right_difference.x) <= 0.05
                and abs(left_difference.y) <= 0.05
                and abs(right_difference.y) <= 0.05
            ):
                self.moving_to_hand = False
                self.flipping_to_front = True

    def check_if_switch(self):
        if self.flipping_to_front:
            if abs(self.card_width - self.end_card_width / 10) <= 0.05:
                self.flipping_to_front = False
                self.stretching_out_front = True
                self.flipping_tick = 0
        elif self.stretching_out_front:
            if abs(self.card_width - self.end_card_width) <= 0.05:
                self.stretching_out_front = False
                self.flipping_tick = 0
