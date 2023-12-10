import pygame as pg


class ViewCards:
    def __init__(self, width):
        self.width = width
        self.viewing_cards = False
        self.card_width = 200
        self.card_height = 280
        self.tick = 0
        self.cards_initilized = False

    # Initilize the card positions
    def initilize_cards(self, left_card_image, right_card_image):
        left_card_image = pg.transform.scale(
            left_card_image, (self.card_width, self.card_height)
        )
        left_card_image = pg.transform.rotate(left_card_image, 20)
        self.left_card_image = left_card_image
        self.left_card_rect = left_card_image.get_rect()
        self.left_card_rect.center = (
            (self.width / 2) - (self.card_width / 2) + 25,
            800,
        )

        right_card_image = pg.transform.scale(
            right_card_image, (self.card_width, self.card_height)
        )
        right_card_image = pg.transform.rotate(right_card_image, -20)
        self.right_card_image = right_card_image
        self.right_card_rect = right_card_image.get_rect()
        self.right_card_rect.center = ((self.width / 2) + 25, 800)

        self.cards_initilized = True
