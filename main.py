from player import Player
from deck import Deck
from client import Client
import pygame as pg

class Game:
    def __init__(self, width, height):
        self.screen = pg.display.set_mode((width, height))
        self.player_list = [Player(), Player(),Player(), Player()]
        self.client = Client()
        self.initilize_seats()
        self.initilize_sprites()

    def initilize_seats(self):
        seat_positions = [(250,437.5),(62.5,250),(250,62.5),(437.5, 250)]
        for index in range(4):
            self.player_list[index].seat = seat_positions[index]

    def initilize_sprites(self):
        for index in range(4):
            x = self.player_list[index].seat[0]
            y = self.player_list[index].seat[1]
            self.player_list[index].sprite = pg.Rect(x,y,50,50)

    def draw_sprites(self, players_connected):
        for index in range(4):
            if index in players_connected:
                pg.draw.rect(self.screen, (100,100,100), self.player_list[index].sprite, border_radius = 50)

    def run(self):
        running = True
        clock = pg.time.Clock()
        while running:
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
            self.client.send_object(self.player_list[0])
            data = self.client.receive_object()
            self.screen.fill((255,255,255))
            self.draw_sprites(data.players_connected)
            pg.display.flip()

game = Game(500,500)
game.run()
        
        

        


