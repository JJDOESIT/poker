import pygame as pg


class Join:
    def __init__(self):
        self.in_lobby = False
        self.type_ip_active = False
        self.type_port_active = False
        self.type_name_active = False
        self.connect_active = False
        self.exit_active = False
        self.failed_to_connect = False
        self.lobby_ip = ""
        self.port = ""
        self.name = ""
        self.input_ip_rect = pg.Rect(100, 125, 300, 75)
        self.input_port_rect = pg.Rect(100, self.input_ip_rect.bottom + 40, 150, 50)
        self.input_name_rect = pg.Rect(100, self.input_port_rect.bottom + 40, 200, 50)
        self.connect_rect = pg.Rect(175, self.input_name_rect.bottom + 30, 150, 50)
        self.exit_rect = pg.Rect(10, 10, 35, 35)
        self.active_color = pg.Color(255, 255, 255)
        self.passive_color = pg.Color(192, 192, 192)

    def reset(self):
        self.type_ip_active = False
        self.type_port_active = False
        self.type_name_active = False
        self.connect_active = False
        self.exit_active = False
        self.failed_to_connect = False
        self.lobby_ip = ""
        self.port = ""
        self.name = ""
