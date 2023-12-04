import pygame as pg


class Home:
    def __init__(self, width):
        self.in_home = True
        self.join_rect = pg.Rect((width / 2) - 200, 400, 400, 150)
        self.create_rect = pg.Rect((width / 2) - 200, 600, 400, 150)
        self.join_active = False
        self.create_active = False
        self.active_color = pg.Color(255, 255, 255)
        self.passive_color = pg.Color(192, 192, 192)
