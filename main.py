from player import Player
from deck import Deck
from lobby import Lobby
from client import Client
import pygame as pg

pg.init()

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((500, 500))
        self.font = pg.font.Font(None, 32)
        self.sprite_diameter = 50
        self.player_list = [Player(), Player(),Player(), Player()]
        self.client = Client()
        self.lobby = Lobby()
        self.initilize_seats()
        self.initilize_sprites()

    # Draw the main lobby page
    def draw_lobby(self):
        # Draw the text input box 
        if (self.lobby.type_active):
            pg.draw.rect(self.screen, self.lobby.active_color, self.lobby.input_rect)
        else:
            pg.draw.rect(self.screen, self.lobby.passive_color, self.lobby.input_rect)
        #Draw the connect button
        if (self.lobby.connect_active):
            pg.draw.rect(self.screen, self.lobby.active_color, self.lobby.connect_rect, border_radius = 50)
        else:
            pg.draw.rect(self.screen, self.lobby.passive_color, self.lobby.connect_rect, border_radius = 50)
        # Draw the "Connect" text
        connect_text_surface = self.font.render("Connect", True, (0,0,0))
        self.screen.blit(connect_text_surface, (self.lobby.connect_rect.centerx - 45, self.lobby.connect_rect.center[1] - 10))
        # Draw the "Server IP:" text
        label_text_surface = self.font.render("Server IP:", True, (255,255,255))
        self.screen.blit(label_text_surface, (self.lobby.input_rect.left, self.lobby.input_rect.top - 32))
        # Draw the ip address text 
        ip_text_surface = self.font.render(self.lobby.lobby_ip, True, (0,0,0))
        self.screen.blit(ip_text_surface, (self.lobby.input_rect.midleft))

    # Attempt to connect to the server
    def connect_to_server(self):
        self.client.connect(self.lobby.lobby_ip)
        if self.client.id == -1:
            print('error')
        else:
            self.lobby.in_lobby = False
        

    def draw_table(self):
        wood_section = pg.Rect(100, 125,300,250)
        gold_section = pg.Rect(115, 140, 270, 220)
        felt_section = pg.Rect(120, 145, 260,210)
        pg.draw.rect(self.screen, (70,50,5), wood_section)
        pg.draw.rect(self.screen, (204,204,0), gold_section)
        pg.draw.rect(self.screen, (0,100,0), felt_section)

    def initilize_seats(self):
        seat_positions = [(250,437.5),(62.5,250),(250,62.5),(437.5, 250)]
        for index in range(4):
            self.player_list[index].seat = seat_positions[index]

    def initilize_sprites(self):
        for index in range(4):
            x = self.player_list[index].seat[0]
            y = self.player_list[index].seat[1]
            self.player_list[index].sprite = pg.Rect(x - (self.sprite_diameter/2),y - (self.sprite_diameter/2),self.sprite_diameter,self.sprite_diameter)

    def draw_sprites(self, players_connected):
        for index in range(4):
            if players_connected[index] == 'taken':
                pg.draw.rect(self.screen, (100,100,100), self.player_list[index].sprite, border_radius = 50)

    def check_for_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            # If user clicks mouse button
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user is in the lobby
                if self.lobby.in_lobby:
                    # If the user clicks the text input box
                    if self.lobby.input_rect.collidepoint(event.pos):
                        self.lobby.type_active = True
                    else:
                        self.lobby.type_active = False
                    # If the user clicks the connect button
                    if self.lobby.connect_rect.collidepoint(event.pos):
                        self.connect_to_server()

            # If user presses a key
            if event.type == pg.KEYDOWN:
                # If the user is in the lobby
                if self.lobby.in_lobby:
                    # If the input box has been clicked
                    if self.lobby.type_active:
                        if event.key == pg.K_BACKSPACE:
                            if len(self.lobby.lobby_ip) > 0:
                                self.lobby.lobby_ip = self.lobby.lobby_ip[:-1]
                        elif ((event.unicode.isnumeric() or event.unicode == '.') and len(self.lobby.lobby_ip) < 15):
                            self.lobby.lobby_ip += event.unicode
            # If the user moves their mouse
            if event.type == pg.MOUSEMOTION:
                # If the user is in the lobby
                if self.lobby.in_lobby:
                    # If the user hovers over the connect button
                    if self.lobby.connect_rect.collidepoint(event.pos):
                        self.lobby.connect_active = True
                    else:
                        self.lobby.connect_active = False

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            self.check_for_events()
            
           
            if self.lobby.in_lobby:
                self.screen.fill((0,120,0))
                self.draw_lobby()
            else:
                self.screen.fill((255,255,255))
                self.client.send_object(self.player_list[0])
                data = self.client.receive_object()
                self.draw_table()
                self.draw_sprites(data.players_connected)
           
            
            pg.display.flip()

game = Game()
game.run()
        
        

        


