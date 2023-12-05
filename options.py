import pygame as pg


class Options:
    def __init__(self, width):
        self.view_cards_rect = pg.Rect((width - 300), 50, 200, 50)
        self.deal_rect = pg.Rect((width / 2 - 100), 800, 200, 50)
        self.fold_rect = pg.Rect((width / 2 - 100) - 250, 800, 200, 50)
        self.call_rect = pg.Rect((width / 2 - 100), 800, 200, 50)
        self.raise_rect = pg.Rect((width / 2 - 100) + 250, 800, 200, 50)
        self.view_cards_active = False
        self.deal_active = False
        self.fold_active = False
        self.call_active = False
        self.raise_active = False
        self.active_color = (225, 225, 225)
        self.passive_color = (200, 200, 200)
