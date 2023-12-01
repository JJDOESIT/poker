import pygame as pg


class Lobby:
    def __init__(self):
        self.in_lobby = True
        self.lobby_ip = ""
        self.input_rect = pg.Rect(100,125,300,100)
        self.connect_rect = pg.Rect(175,250,150,50)
        self.type_active = False
        self.connect_active = False
        self.active_color = pg.Color(255,255,255)
        self.passive_color = pg.Color(192,192,192) 
