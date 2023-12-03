import pygame as pg


class Ready:
    def __init__(self):
        self.ready_rect = pg.Rect(225, 425, 50, 50)
        self.selected_ready_rect = pg.Rect(230, 430, 40, 40)
        self.is_ready = False
        self.ready_color = (0, 255, 0)
        self.not_ready_color = (255, 0, 0)
