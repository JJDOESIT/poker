import pygame as pg


class Ready:
    def __init__(self, player_list, id):
        self.initilize_ready_rects(player_list, id)
        self.is_ready = False
        self.ready_color = (0, 255, 0)
        self.not_ready_color = (255, 0, 0)

    # Initilize the positions of the ready up rects
    def initilize_ready_rects(self, player_list, id):
        if id == 0:
            self.ready_rect = pg.Rect(
                player_list[id].player_border_rect.centerx - 25,
                player_list[id].player_border_rect.bottom + 25,
                50,
                50,
            )
            self.selected_ready_rect = pg.Rect(
                self.ready_rect.centerx - 20, self.ready_rect.centery - 20, 40, 40
            )
        elif id == 1:
            self.ready_rect = pg.Rect(
                player_list[id].player_border_rect.left - 75,
                player_list[id].player_border_rect.centery - 25,
                50,
                50,
            )
            self.selected_ready_rect = pg.Rect(
                self.ready_rect.centerx - 20, self.ready_rect.centery - 20, 40, 40
            )

        elif id == 2:
            self.ready_rect = pg.Rect(
                player_list[id].player_border_rect.centerx - 25,
                player_list[id].player_border_rect.top - 75,
                50,
                50,
            )
            self.selected_ready_rect = pg.Rect(
                self.ready_rect.centerx - 20, self.ready_rect.centery - 20, 40, 40
            )

        else:
            self.ready_rect = pg.Rect(
                player_list[id].player_border_rect.right + 25,
                player_list[id].player_border_rect.centery - 25,
                50,
                50,
            )
            self.selected_ready_rect = pg.Rect(
                self.ready_rect.centerx - 20, self.ready_rect.centery - 20, 40, 40
            )
