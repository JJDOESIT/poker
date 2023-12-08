import pygame as pg


class Blinds:
    def __init__(self, width):
        self.active_blind = None
        self.one_dollar_img = pg.image.load("./images/chips/one_dollar.png")
        self.two_dollar_img = pg.image.load("./images/chips/two_dollar.png")
        self.five_dollar_img = pg.image.load("./images/chips/five_dollar.png")
        self.ten_dollar_img = pg.image.load("./images/chips/ten_dollar.png")
        self.twenty_dollar_img = pg.image.load("./images/chips/twenty_dollar.png")
        self.transform_images()
        self.one_dollar_rect = self.one_dollar_img.get_rect()
        self.two_dollar_rect = self.two_dollar_img.get_rect()
        self.five_dollar_rect = self.five_dollar_img.get_rect()
        self.ten_dollar_rect = self.ten_dollar_img.get_rect()
        self.twenty_dollar_rect = self.twenty_dollar_img.get_rect()
        self.active_y = 740
        self.passive_y = 750
        self.one_dollar_rect.topleft = (
            (width / 2) - (self.one_dollar_rect.width / 2),
            self.passive_y,
        )
        self.two_dollar_rect.topleft = (
            (width / 2) - (self.two_dollar_rect.width / 2),
            self.passive_y,
        )
        self.five_dollar_rect.topleft = (
            (width / 2) - (self.five_dollar_rect.width / 2),
            self.passive_y,
        )
        self.ten_dollar_rect.topleft = (
            (width / 2) - (self.ten_dollar_rect.width / 2),
            self.passive_y,
        )
        self.twenty_dollar_rect.topleft = (
            (width / 2) - (self.twenty_dollar_rect.width / 2),
            self.passive_y,
        )

    # Transform the image to scale
    def transform_images(self):
        self.one_dollar_img = pg.transform.scale(self.one_dollar_img, (76, 76))
        self.two_dollar_img = pg.transform.scale(self.two_dollar_img, (76, 76))
        self.five_dollar_img = pg.transform.scale(self.five_dollar_img, (76, 76))
        self.ten_dollar_img = pg.transform.scale(self.ten_dollar_img, (76, 76))
        self.twenty_dollar_img = pg.transform.scale(self.twenty_dollar_img, (76, 76))
