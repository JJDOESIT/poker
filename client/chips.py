import pygame as pg


class Chips:
    def __init__(self):
        self.one_dollar_img = pg.image.load("./images/chips/one_dollar.png")
        self.two_dollar_img = pg.image.load("./images/chips/two_dollar.png")
        self.five_dollar_img = pg.image.load("./images/chips/five_dollar.png")
        self.ten_dollar_img = pg.image.load("./images/chips/ten_dollar.png")
        self.twenty_dollar_img = pg.image.load(
            "./images/chips/twenty_dollar.png")
        self.chip_diameter = 25
        self.transform_images()
        self.chips_images = {1: self.one_dollar_img, 2: self.two_dollar_img,
                             5: self.five_dollar_img, 10: self.ten_dollar_img, 20: self.twenty_dollar_img}
        self.player_one_chip_positions = {1: (725, 560), 2: (
            770, 510), 5: (800, 515), 10: (850, 540), 20: (855, 575)}
        self.player_two_chip_positions = {1: (435, 360), 2: (
            470, 365), 5: (500, 400), 10: (435, 505), 20: (470, 510)}
        self.player_three_chip_positions = {1: (725, 305), 2: (
            720, 340), 5: (780, 360), 10: (840, 355), 20: (855, 310)}
        self.player_four_chip_positions = {1: (1100, 360), 2: (
            1135, 365), 5: (1065, 400), 10: (1080, 505), 20: (1130, 510)}

    # Transform the images to the correct scale
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
