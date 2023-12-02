import pygame as pg

class Home:
    def __init__(self):
        self.in_home = True
        self.join_rect = pg.Rect(150,175,200,70)
        self.create_rect = pg.Rect(150,265,200,70)
        self.join_active = False
        self.create_active = False
        self.active_color = pg.Color(255,255,255)
        self.passive_color = pg.Color(192,192,192) 