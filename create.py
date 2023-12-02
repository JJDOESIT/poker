import pygame as pg


class Create:
    def __init__(self):
        self.in_lobby = False
        self.type_ip_active = False
        self.type_port_active = False
        self.connect_active = False
        self.exit_active = False
        self.failed_to_create = False
        self.success = False
        self.auto_connect = False
        self.external_ip = ""
        self.port = ""
        self.input_ip_rect = pg.Rect(100, 125, 300, 75)
        self.input_port_rect = pg.Rect(100, self.input_ip_rect.bottom + 50, 150, 50)
        self.auto_connect_rect = pg.Rect(
            self.input_port_rect.right + 70, self.input_port_rect.top + 10, 26, 26
        )
        self.checked_box = pg.Rect(
            self.auto_connect_rect.left + 3, self.auto_connect_rect.top + 3, 20, 20
        )
        self.create_rect = pg.Rect(175, self.input_port_rect.bottom + 50, 150, 50)
        self.exit_rect = pg.Rect(10, 10, 35, 35)
        self.active_color = pg.Color(255, 255, 255)
        self.passive_color = pg.Color(192, 192, 192)

    def reset(self):
        self.type_ip_active = False
        self.type_port_active = False
        self.connect_active = False
        self.failed_to_create = False
        self.success = False
        self.exit_active = False
