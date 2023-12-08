import pygame as pg


class Ante:
    def __init__(self, width):
        self.two_dollar_img = pg.image.load("./images/chips/two_dollar.png")
        self.five_dollar_img = pg.image.load("./images/chips/five_dollar.png")
        self.ten_dollar_img = pg.image.load("./images/chips/ten_dollar.png")
        self.twenty_dollar_img = pg.image.load("./images/chips/twenty_dollar.png")
        self.transform_images()
        self.two_dollar_rect = self.two_dollar_img.get_rect()
        self.five_dollar_rect = self.five_dollar_img.get_rect()
        self.ten_dollar_rect = self.ten_dollar_img.get_rect()
        self.twenty_dollar_rect = self.twenty_dollar_img.get_rect()
        self.active_y = 740
        self.passive_y = 750
        self.five_dollar_rect.topleft = (width / 2 - 95, self.passive_y)
        self.ten_dollar_rect.topleft = (width / 2 + 19, self.passive_y)
        self.two_dollar_rect.topleft = (
            self.five_dollar_rect.x - 114,
            self.passive_y,
        )
        self.twenty_dollar_rect.topleft = (
            self.ten_dollar_rect.x + 114,
            self.passive_y,
        )

    # Transform the image to scale
    def transform_images(self):
        self.two_dollar_img = pg.transform.scale(self.two_dollar_img, (76, 76))
        self.five_dollar_img = pg.transform.scale(self.five_dollar_img, (76, 76))
        self.ten_dollar_img = pg.transform.scale(self.ten_dollar_img, (76, 76))
        self.twenty_dollar_img = pg.transform.scale(self.twenty_dollar_img, (76, 76))
