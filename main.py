from player import Player
from join import Join
from client import Client
from home import Home
from create import Create
from options import Options
from draw import Draw
from ready import Ready
import pygame as pg
import os
import subprocess


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pg.init()


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((500, 500))
        self.sprite_diameter = 50
        self.turn = 0
        self.game_started = False
        self.overhead_message = ""
        self.player_list = [Player(), Player(), Player(), Player()]
        self.client = Client()
        self.home_page = Home()
        self.join_lobby = Join()
        self.create_lobby = Create()
        self.options = Options()
        self.ready = Ready()
        self.initilize_seats()
        self.initilize_sprites()
        self.draw = Draw(
            self.screen,
            self.home_page,
            self.join_lobby,
            self.create_lobby,
            self.options,
            self.ready,
        )

    # Attempt to connect to the server
    def connect_to_server(self, ip, port):
        if not len(ip) > 2 or not len(port) > 0:
            return
        self.client.connect(ip, port)
        # If user failed to connect to server
        if self.client.id == -1:
            if self.join_lobby.in_lobby:
                self.join_lobby.failed_to_connect = True
        else:
            # If joining from join menu
            if self.join_lobby.in_lobby:
                self.player_list[self.client.id].name = self.join_lobby.name
                self.join_lobby.reset()
                self.join_lobby.in_lobby = False
            # If joining from creating a server
            elif self.create_lobby.in_lobby:
                self.create_lobby.reset()
                self.create_lobby.auto_connect = False
                self.create_lobby.in_lobby = False
                self.create_lobby.external_ip = ""
                self.create_lobby.port = ""
                self.player_list[0].name = "Host"
            self.player_list[self.client.id].id = self.client.id

    # Attempt to create lobby
    def create(self):
        if not len(self.create_lobby.port) > 0:
            return
        result = subprocess.Popen(["py", "testBind.py", self.create_lobby.port])
        result.wait()
        self.create_lobby.reset()
        if result.returncode == 1:
            self.create_lobby.failed_to_create = True
            self.create_lobby.success = False
        else:
            self.create_lobby.failed_to_create = False
            self.create_lobby.success = True
            if self.create_lobby.auto_connect:
                self.connect_to_server(
                    self.create_lobby.external_ip, self.create_lobby.port
                )

    # See if the server has started the game
    def check_if_game_started(self, game_started, dealer):
        if not self.game_started:
            if game_started:
                self.game_started = game_started
                self.player_list[self.client.id].previous_action = ""

    # Initilize the position where each player will be sitting
    def initilize_seats(self):
        seat_positions = [(200, 350), (0, 200), (200, 40), (400, 200)]
        for index in range(4):
            self.player_list[index].seat = seat_positions[index]

    # Initilize the player sprite
    def initilize_sprites(self):
        for player in self.player_list:
            player.player_border_rect = pg.Rect(player.seat[0], player.seat[1], 100, 60)

    # Handle user input
    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            # If the user is in the home page
            if self.home_page.in_home:
                # If user clicks mouse button
                if event.type == pg.MOUSEBUTTONUP:
                    # If the user clicks the join button
                    if self.home_page.join_rect.collidepoint(event.pos):
                        self.home_page.in_home = False
                        self.home_page.join_active = False
                        self.join_lobby.in_lobby = True
                    # If the user clicks the create button
                    elif self.home_page.create_rect.collidepoint(event.pos):
                        self.home_page.in_home = False
                        self.home_page.create_active = False
                        self.create_lobby.in_lobby = True

                # If the user moves their mouse
                if event.type == pg.MOUSEMOTION:
                    self.home_page.join_active = self.home_page.join_rect.collidepoint(
                        event.pos
                    )
                    self.home_page.create_active = (
                        self.home_page.create_rect.collidepoint(event.pos)
                    )

            # If the user is in the join_lobby page
            elif self.join_lobby.in_lobby:
                # If user clicks mouse button
                if event.type == pg.MOUSEBUTTONUP:
                    # If the user clicks on ip text box
                    self.join_lobby.type_ip_active = (
                        self.join_lobby.input_ip_rect.collidepoint(event.pos)
                    )
                    # If the user clicks the port text box
                    self.join_lobby.type_port_active = (
                        self.join_lobby.input_port_rect.collidepoint(event.pos)
                    )
                    # If the user clicks the name text box
                    self.join_lobby.type_name_active = (
                        self.join_lobby.input_name_rect.collidepoint(event.pos)
                    )
                    # If the user clicks connect
                    if self.join_lobby.connect_rect.collidepoint(event.pos):
                        if len(self.join_lobby.name) > 0:
                            self.connect_to_server(
                                self.join_lobby.lobby_ip, self.join_lobby.port
                            )
                    # If the user clicks the exit button
                    if self.join_lobby.exit_rect.collidepoint(event.pos):
                        self.join_lobby.reset()
                        self.join_lobby.in_lobby = False
                        self.home_page.in_home = True

                # If user presses a key
                elif event.type == pg.KEYDOWN:
                    # If the input ip box has been clicked
                    if self.join_lobby.type_ip_active:
                        if event.key == pg.K_BACKSPACE:
                            if len(self.join_lobby.lobby_ip) > 0:
                                self.join_lobby.lobby_ip = self.join_lobby.lobby_ip[:-1]
                        elif (
                            event.unicode.isnumeric() or event.unicode == "."
                        ) and len(self.join_lobby.lobby_ip) < 15:
                            self.join_lobby.lobby_ip += event.unicode

                    # If the input port box has been clicked
                    if self.join_lobby.type_port_active:
                        if event.key == pg.K_BACKSPACE:
                            if len(self.join_lobby.port) > 0:
                                self.join_lobby.port = self.join_lobby.port[:-1]
                        elif (
                            event.unicode.isnumeric() or event.unicode == "."
                        ) and len(self.join_lobby.port) < 6:
                            self.join_lobby.port += event.unicode

                    # If the input name box has been clicked
                    if self.join_lobby.type_name_active:
                        if event.key == pg.K_BACKSPACE:
                            if len(self.join_lobby.name) > 0:
                                self.join_lobby.name = self.join_lobby.name[:-1]
                        elif event.unicode.isalpha() and len(self.join_lobby.name) < 10:
                            self.join_lobby.name += event.unicode

                # If the user moves their mouse
                elif event.type == pg.MOUSEMOTION:
                    self.join_lobby.connect_active = (
                        self.join_lobby.connect_rect.collidepoint(event.pos)
                    )
                    self.join_lobby.exit_active = (
                        self.join_lobby.exit_rect.collidepoint(event.pos)
                    )

            # If the user is in the create lobby page
            elif self.create_lobby.in_lobby:
                # If user clicks mouse button
                if event.type == pg.MOUSEBUTTONUP:
                    # If the user clicks the ip input box
                    self.create_lobby.type_ip_active = (
                        self.create_lobby.input_ip_rect.collidepoint(event.pos)
                    )
                    # If the user clicks the port input box
                    self.create_lobby.type_port_active = (
                        self.create_lobby.input_port_rect.collidepoint(event.pos)
                    )
                    # If the user clicks auto connect
                    if self.create_lobby.auto_connect_rect.collidepoint(event.pos):
                        self.create_lobby.auto_connect = (
                            not self.create_lobby.auto_connect
                        )

                    # If the user clicks create
                    if self.create_lobby.create_rect.collidepoint(event.pos):
                        self.create()
                    # If the user clicks the exit button
                    if self.create_lobby.exit_rect.collidepoint(event.pos):
                        self.create_lobby.reset()
                        self.create_lobby.in_lobby = False
                        self.create_lobby.auto_connect = False
                        self.home_page.in_home = True
                        self.create_lobby.external_ip = ""
                        self.create_lobby.port = ""

                # If user presses a key
                elif event.type == pg.KEYDOWN:
                    # If the ip input box has been clicked
                    if self.create_lobby.type_ip_active:
                        if event.key == pg.K_BACKSPACE:
                            if len(self.create_lobby.external_ip) > 0:
                                self.create_lobby.external_ip = (
                                    self.create_lobby.external_ip[:-1]
                                )
                        elif (
                            event.unicode.isnumeric() or event.unicode == "."
                        ) and len(self.create_lobby.external_ip) < 15:
                            self.create_lobby.external_ip += event.unicode
                    # If the port input box has been cicked
                    elif self.create_lobby.type_port_active:
                        if event.key == pg.K_BACKSPACE:
                            if len(self.create_lobby.port) > 0:
                                self.create_lobby.port = self.create_lobby.port[:-1]
                        elif (
                            event.unicode.isnumeric() or event.unicode == "."
                        ) and len(self.create_lobby.port) < 6:
                            self.create_lobby.port += event.unicode

                # If the user moves their mouse
                if event.type == pg.MOUSEMOTION:
                    self.create_lobby.connect_active = (
                        self.create_lobby.create_rect.collidepoint(event.pos)
                    )
                    self.create_lobby.exit_active = (
                        self.create_lobby.exit_rect.collidepoint(event.pos)
                    )

            # If the user is in the game
            else:
                if event.type == pg.MOUSEBUTTONUP:
                    # If the game hasn't started yet
                    if not self.game_started:
                        # If the user readys up
                        if self.ready.ready_rect.collidepoint(event.pos):
                            if self.ready.is_ready:
                                self.player_list[
                                    self.client.id
                                ].previous_action = "Not ready"
                                self.ready.is_ready = False
                            else:
                                self.player_list[
                                    self.client.id
                                ].previous_action = "Ready"
                                self.ready.is_ready = True

                    # If it is your turn
                    if self.turn == self.client.id:
                        # If the user clicks the fold option
                        if self.options.fold_rect.collidepoint(event.pos):
                            self.player_list[self.client.id].move.append("fold")
                            self.player_list[self.client.id].move.append(
                                f"{self.player_list[self.client.id].name} has folded"
                            )

                if event.type == pg.MOUSEMOTION:
                    self.options.fold_active = self.options.fold_rect.collidepoint(
                        event.pos
                    )
                    self.options.call_active = self.options.call_rect.collidepoint(
                        event.pos
                    )
                    self.options.raise_active = self.options.raise_rect.collidepoint(
                        event.pos
                    )

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            self.handle_input()

            if self.home_page.in_home:
                self.screen.fill((0, 120, 0))
                self.draw.draw_home()

            elif self.join_lobby.in_lobby:
                self.screen.fill((0, 120, 0))
                self.draw.draw_join_lobby()
            elif self.create_lobby.in_lobby:
                self.screen.fill((0, 120, 0))
                self.draw.draw_create_lobby()
            else:
                self.screen.fill((180, 160, 160))

                if self.game_started:
                    # If it's your turn, display possible options
                    if self.turn == self.client.id:
                        self.draw.draw_options()
                else:
                    self.draw.draw_ready_option()

                # Send your player data over
                self.client.send_object(self.player_list[self.client.id])

                # Receive the other player data back
                data = self.client.receive_object()

                # Sync the players data
                self.client.sync_players(self.player_list, data.player_list)

                # Check if the game is started
                self.check_if_game_started(data.game_started, data.dealer)

                self.overhead_message = data.overhead_message

                # Update turn
                self.turn = data.turn

                self.draw.draw_overhead_message(self.overhead_message)
                self.draw.draw_table()
                self.draw.draw_sprites(self.player_list, data.players_connected)

            pg.display.flip()


game = Game()
game.run()
