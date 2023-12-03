import pygame as pg


class Options:
    def __init__(self):
        self.fold_rect = pg.Rect(50, 425, 100, 50)
        self.call_rect = pg.Rect(200, 425, 100, 50)
        self.raise_rect = pg.Rect(350, 425, 100, 50)
        self.fold_active = False
        self.call_active = False
        self.raise_active = False
        self.active_color = (225, 225, 225)
        self.passive_color = (200, 200, 200)
