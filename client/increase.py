import pygame as pg


class Raise:
    def __init__(self, width):
        self.bet = 0
        self.clicked_chip_amount = 0
        self.viewing_raise = False
        self.one_dollar_img = pg.image.load("./images/chips/one_dollar.png")
        self.two_dollar_img = pg.image.load("./images/chips/two_dollar.png")
        self.five_dollar_img = pg.image.load("./images/chips/five_dollar.png")
        self.ten_dollar_img = pg.image.load("./images/chips/ten_dollar.png")
        self.twenty_dollar_img = pg.image.load(
            "./images/chips/twenty_dollar.png")
        self.chip_diameter = 76
        self.transform_images()
        self.one_dollar_rect = self.one_dollar_img.get_rect()
        self.two_dollar_rect = self.two_dollar_img.get_rect()
        self.five_dollar_rect = self.five_dollar_img.get_rect()
        self.ten_dollar_rect = self.ten_dollar_img.get_rect()
        self.twenty_dollar_rect = self.twenty_dollar_img.get_rect()
        self.passive_y = 750
        self.active_y = 740
        self.position_rects(width)
        self.back_rect = pg.Rect(
            self.one_dollar_rect.x - 70, self.one_dollar_rect.centery - 25, 50, 50)
        self.plus_rect = pg.Rect(self.five_dollar_rect.right,
                                 self.five_dollar_rect.bottom + 10, 50, 50)
        self.minus_rect = pg.Rect(self.five_dollar_rect.left - 50,
                                  self.five_dollar_rect.bottom + 10, 50, 50)
        self.raise_rect = pg.Rect(
            self.five_dollar_rect.centerx - 50, self.five_dollar_rect.bottom + 10, 100, 50)
        self.raise_active = False
        self.back_active = False
        self.plus_active = False
        self.minus_active = False
        self.active_color = pg.Color(255, 255, 255)
        self.passive_color = pg.Color(192, 192, 192)

    # Transform the image to scale
    def transform_images(self):
        self.one_dollar_img = pg.transform.scale(
            self.one_dollar_img, (self.chip_diameter, self.chip_diameter))
        self.two_dollar_img = pg.transform.scale(
            self.two_dollar_img, (self.chip_diameter, self.chip_diameter))
        self.five_dollar_img = pg.transform.scale(
            self.five_dollar_img, (self.chip_diameter, self.chip_diameter))
        self.ten_dollar_img = pg.transform.scale(
            self.ten_dollar_img, (self.chip_diameter, self.chip_diameter))
        self.twenty_dollar_img = pg.transform.scale(
            self.twenty_dollar_img, (self.chip_diameter, self.chip_diameter))

    # Set the x, y of the chip rects
    def position_rects(self, width):
        self.five_dollar_rect.topleft = (
            width / 2 - (self.chip_diameter / 2), self.passive_y)
        self.ten_dollar_rect.topleft = (
            self.five_dollar_rect.x + (self.chip_diameter + (self.chip_diameter / 4)), self.passive_y)
        self.two_dollar_rect.topleft = (
            self.five_dollar_rect.x -
            (self.chip_diameter + (self.chip_diameter / 4)),
            self.passive_y,
        )
        self.one_dollar_rect.topleft = (
            self.two_dollar_rect.x -
            (self.chip_diameter + (self.chip_diameter / 4)),
            self.passive_y,
        )
        self.twenty_dollar_rect.topleft = (
            self.ten_dollar_rect.x +
            (self.chip_diameter + (self.chip_diameter / 4)),
            self.passive_y,
        )

    # Reset all conditions
    def reset(self):
        self.bet = 0
        self.clicked_chip_amount = 0
        self.raise_active = False
        self.back_active = False
        self.plus_active = False
        self.minus_active = False
        self.viewing_raise = False
