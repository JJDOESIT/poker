import os
import platform
import subprocess
import pygame as pg

from client_server.player import Player
from client.join import Join
from client.client import Client
from client.home import Home
from client.create import Create
from client.options import Options
from client.draw import Draw
from client.ante import Ante
from client.blinds import Blinds
from client.chips import Chips
from client.cards import Cards
from client.viewCards import ViewCards
from client.increase import Raise
from client.animations import Animations
from client.ready import Ready


WIDTH = 1600
HEIGHT = 900

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pg.init()


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.sprite_diameter = 50
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.client = Client()
        self.home_page = Home(WIDTH)
        self.join_lobby = Join(WIDTH)
        self.create_lobby = Create(WIDTH)
        self.ante = Ante(WIDTH)
        self.blinds = Blinds(WIDTH)
        self.chips = Chips()
        self.cards = Cards()
        self.viewCards = ViewCards(WIDTH)
        self.raise_option = Raise(WIDTH)
        self.animations = Animations()
        self.options = Options(WIDTH)
        self.draw = Draw(
            WIDTH,
            HEIGHT,
            self.screen,
            self.home_page,
            self.join_lobby,
            self.create_lobby,
            self.ante,
            self.blinds,
            self.chips,
            self.cards,
            self.viewCards,
            self.raise_option,
            self.animations,
            self.options,
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
            self.ready = Ready(self.player_list, self.client.id)

    # Attempt to create lobby
    def create(self):
        if not len(self.create_lobby.port) > 0:
            return
        if platform.system() == "Linux":
            result = subprocess.Popen(
                ["python3", "server/testBind.py", self.create_lobby.port],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        elif platform.system() == "Windows":
            result = subprocess.Popen(
                ["py", "server/testBind.py", self.create_lobby.port],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
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

    # Handle user input
    def handle_input(self, data=None):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
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
                        self.create_lobby.input_port_rect.collidepoint(
                            event.pos)
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
            elif not data.game_started:
                # If the ante has not been set
                if data.ante is None:
                    # If you are the host
                    if self.client.id == data.host:
                        if event.type == pg.MOUSEMOTION:
                            # If the user hovers over the poker chips
                            if self.ante.two_dollar_rect.collidepoint(event.pos):
                                self.ante.two_dollar_rect.y = self.ante.active_y
                            else:
                                self.ante.two_dollar_rect.y = self.ante.passive_y
                            if self.ante.five_dollar_rect.collidepoint(event.pos):
                                self.ante.five_dollar_rect.y = self.ante.active_y
                            else:
                                self.ante.five_dollar_rect.y = self.ante.passive_y
                            if self.ante.ten_dollar_rect.collidepoint(event.pos):
                                self.ante.ten_dollar_rect.y = self.ante.active_y
                            else:
                                self.ante.ten_dollar_rect.y = self.ante.passive_y
                            if self.ante.twenty_dollar_rect.collidepoint(event.pos):
                                self.ante.twenty_dollar_rect.y = self.ante.active_y
                            else:
                                self.ante.twenty_dollar_rect.y = self.ante.passive_y

                        if event.type == pg.MOUSEBUTTONUP:
                            # If the user selects an ante
                            if self.ante.two_dollar_rect.collidepoint(event.pos):
                                self.player_list[self.client.id].add_move(
                                    "ante", [2])
                            if self.ante.five_dollar_rect.collidepoint(event.pos):
                                self.player_list[self.client.id].add_move(
                                    "ante", [5])
                            if self.ante.ten_dollar_rect.collidepoint(event.pos):
                                self.player_list[self.client.id].add_move(
                                    "ante", [10])
                            if self.ante.twenty_dollar_rect.collidepoint(event.pos):
                                self.player_list[self.client.id].add_move(
                                    "ante", [20])

                # If the ante has been set
                else:
                    if event.type == pg.MOUSEBUTTONUP:
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

            # If the game has started
            elif data.game_started:
                # If you are the small blind
                if (
                    data.small_blind_bet == 0
                    and data.small_blind_player == self.client.id
                ):
                    if event.type == pg.MOUSEBUTTONUP:
                        if (
                            self.blinds.one_dollar_rect.collidepoint(event.pos)
                            and self.blinds.active_blind == "one_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "small_blind", [1]
                            )
                        elif (
                            self.blinds.two_dollar_rect.collidepoint(event.pos)
                            and self.blinds.active_blind == "two_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "small_blind", [2]
                            )
                        elif (
                            self.blinds.five_dollar_rect.collidepoint(
                                event.pos)
                            and self.blinds.active_blind == "five_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "small_blind", [5]
                            )
                        elif (
                            self.blinds.ten_dollar_rect.collidepoint(event.pos)
                            and self.blinds.active_blind == "ten_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "small_blind", [10]
                            )

                    elif event.type == pg.MOUSEMOTION:
                        # If the user hovers over the poker chips
                        if self.blinds.one_dollar_rect.collidepoint(event.pos):
                            self.blinds.one_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.one_dollar_rect.y = self.blinds.passive_y
                        if self.blinds.two_dollar_rect.collidepoint(event.pos):
                            self.blinds.two_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.two_dollar_rect.y = self.blinds.passive_y
                        if self.blinds.five_dollar_rect.collidepoint(event.pos):
                            self.blinds.five_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.five_dollar_rect.y = self.blinds.passive_y
                        if self.blinds.ten_dollar_rect.collidepoint(event.pos):
                            self.blinds.ten_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.ten_dollar_rect.y = self.blinds.passive_y

                # Else if you're the big blind
                elif (
                    data.small_blind_bet != 0
                    and data.big_blind_bet == 0
                    and data.big_blind_player == self.client.id
                ):
                    if event.type == pg.MOUSEBUTTONUP:
                        if (
                            self.blinds.two_dollar_rect.collidepoint(event.pos)
                            and self.blinds.active_blind == "two_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "big_blind", [2])
                        elif (
                            self.blinds.five_dollar_rect.collidepoint(
                                event.pos)
                            and self.blinds.active_blind == "five_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "big_blind", [5])
                        elif (
                            self.blinds.ten_dollar_rect.collidepoint(event.pos)
                            and self.blinds.active_blind == "ten_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "big_blind", [10])
                        elif (
                            self.blinds.twenty_dollar_rect.collidepoint(
                                event.pos)
                            and self.blinds.active_blind == "twenty_dollar"
                        ):
                            self.player_list[self.client.id].add_move(
                                "big_blind", [20])

                    elif event.type == pg.MOUSEMOTION:
                        # If the user hovers over the poker chips
                        if self.blinds.twenty_dollar_rect.collidepoint(event.pos):
                            self.blinds.twenty_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.twenty_dollar_rect.y = self.blinds.passive_y
                        if self.blinds.two_dollar_rect.collidepoint(event.pos):
                            self.blinds.two_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.two_dollar_rect.y = self.blinds.passive_y
                        if self.blinds.five_dollar_rect.collidepoint(event.pos):
                            self.blinds.five_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.five_dollar_rect.y = self.blinds.passive_y
                        if self.blinds.ten_dollar_rect.collidepoint(event.pos):
                            self.blinds.ten_dollar_rect.y = self.blinds.active_y
                        else:
                            self.blinds.ten_dollar_rect.y = self.blinds.passive_y

                # If your the dealer and havn't dealt
                elif data.dealer == self.client.id and not data.has_dealt:
                    # If the blinds have been initilized and the dealer hasn't dealt
                    if data.small_blind_bet != 0 and data.big_blind_bet != 0:
                        # Clicks the deal button
                        if event.type == pg.MOUSEBUTTONUP:
                            if self.options.deal_rect.collidepoint(event.pos):
                                self.player_list[self.client.id].add_move(
                                    "deal")

                        # Hovers over deal button
                        if event.type == pg.MOUSEMOTION:
                            self.options.deal_active = (
                                self.options.deal_rect.collidepoint(event.pos)
                            )

                # If the dealer has dealt and the dealing animation isn't occuring
                if data.has_dealt and not data.is_dealing:
                    # If it's your turn
                    if self.client.id == data.turn:
                        # If you are not viewing your cards
                        if not self.viewCards.viewing_cards:
                            # If you are raising
                            if self.raise_option.viewing_raise:
                                if event.type == pg.MOUSEBUTTONUP:
                                    # If the user clicks the back button
                                    if self.raise_option.back_rect.collidepoint(event.pos):
                                        self.raise_option.reset()
                                    # If the user clicks a poker chip
                                    elif self.raise_option.one_dollar_rect.collidepoint(event.pos):
                                        if self.raise_option.clicked_chip_amount == 0:
                                            self.raise_option.clicked_chip_amount = 1
                                        else:
                                            self.raise_option.clicked_chip_amount = 0
                                    elif self.raise_option.two_dollar_rect.collidepoint(event.pos):
                                        if self.raise_option.clicked_chip_amount == 0:
                                            self.raise_option.clicked_chip_amount = 2
                                        else:
                                            self.raise_option.clicked_chip_amount = 0
                                    elif self.raise_option.five_dollar_rect.collidepoint(event.pos):
                                        if self.raise_option.clicked_chip_amount == 0:
                                            self.raise_option.clicked_chip_amount = 5
                                        else:
                                            self.raise_option.clicked_chip_amount = 0
                                    elif self.raise_option.ten_dollar_rect.collidepoint(event.pos):
                                        if self.raise_option.clicked_chip_amount == 0:
                                            self.raise_option.clicked_chip_amount = 10
                                        else:
                                            self.raise_option.clicked_chip_amount = 0
                                    elif self.raise_option.twenty_dollar_rect.collidepoint(event.pos):
                                        if self.raise_option.clicked_chip_amount == 0:
                                            self.raise_option.clicked_chip_amount = 20
                                        else:
                                            self.raise_option.clicked_chip_amount = 0
                                    self.raise_option.position_rects(WIDTH)
                                    if self.raise_option.clicked_chip_amount == 1:
                                        self.raise_option.one_dollar_rect.y = self.raise_option.active_y
                                    elif self.raise_option.clicked_chip_amount == 2:
                                        self.raise_option.two_dollar_rect.y = self.raise_option.active_y
                                    elif self.raise_option.clicked_chip_amount == 5:
                                        self.raise_option.five_dollar_rect.y = self.raise_option.active_y
                                    elif self.raise_option.clicked_chip_amount == 10:
                                        self.raise_option.ten_dollar_rect.y = self.raise_option.active_y
                                    elif self.raise_option.clicked_chip_amount == 20:
                                        self.raise_option.twenty_dollar_rect.y = self.raise_option.active_y

                                    # If a chip is selected
                                    if self.raise_option.clicked_chip_amount > 0:
                                        # If the user has enough money to add a chip
                                        if self.player_list[self.client.id].money - (self.raise_option.bet + self.raise_option.clicked_chip_amount) >= 0:
                                            # If the user clicks the plus button
                                            if self.raise_option.plus_rect.collidepoint(event.pos):
                                                self.raise_option.bet += self.raise_option.clicked_chip_amount
                                        # If the user has enough to subtract a chip
                                        if self.raise_option.bet - self.raise_option.clicked_chip_amount >= 0:
                                            # If the user clicks the minus button
                                            if self.raise_option.minus_rect.collidepoint(event.pos):
                                                self.raise_option.bet -= self.raise_option.clicked_chip_amount

                                elif event.type == pg.MOUSEMOTION:
                                    # If you hover over the back button
                                    self.raise_option.back_active = self.raise_option.back_rect.collidepoint(
                                        event.pos)
                                    # If no chip is clicked
                                    if self.raise_option.clicked_chip_amount == 0:
                                        # If the user hovers over the poker chips
                                        if self.raise_option.one_dollar_rect.collidepoint(event.pos):
                                            self.raise_option.one_dollar_rect.y = self.raise_option.active_y
                                        else:
                                            self.raise_option.one_dollar_rect.y = self.raise_option.passive_y
                                        if self.raise_option.two_dollar_rect.collidepoint(event.pos):
                                            self.raise_option.two_dollar_rect.y = self.raise_option.active_y
                                        else:
                                            self.raise_option.two_dollar_rect.y = self.raise_option.passive_y
                                        if self.raise_option.five_dollar_rect.collidepoint(event.pos):
                                            self.raise_option.five_dollar_rect.y = self.raise_option.active_y
                                        else:
                                            self.raise_option.five_dollar_rect.y = self.raise_option.passive_y
                                        if self.raise_option.ten_dollar_rect.collidepoint(event.pos):
                                            self.raise_option.ten_dollar_rect.y = self.raise_option.active_y
                                        else:
                                            self.raise_option.ten_dollar_rect.y = self.raise_option.passive_y
                                        if self.raise_option.twenty_dollar_rect.collidepoint(event.pos):
                                            self.raise_option.twenty_dollar_rect.y = self.raise_option.active_y
                                        else:
                                            self.raise_option.twenty_dollar_rect.y = self.raise_option.passive_y

                                    # If the chip is clicked and the user has enough money
                                    elif self.player_list[self.client.id].money - (self.raise_option.bet + self.raise_option.clicked_chip_amount) >= 0:
                                        self.raise_option.plus_active = self.raise_option.plus_rect.collidepoint(
                                            event.pos)
                                        self.raise_option.minus_active = self.raise_option.minus_rect.collidepoint(
                                            event.pos)
                            # If you are not raising
                            else:
                                if event.type == pg.MOUSEBUTTONUP:
                                    # If the user clicks the fold option
                                    if self.options.fold_rect.collidepoint(event.pos):
                                        self.player_list[self.client.id].add_move(
                                            "fold")
                                    # If the user clicks the call option
                                    elif self.options.call_rect.collidepoint(event.pos):
                                        self.player_list[self.client.id].add_move(
                                            "call")
                                    # If the user clicks the raise option
                                    elif self.options.raise_rect.collidepoint(event.pos):
                                        self.raise_option.viewing_raise = True
                                        self.options.reset()

                                elif event.type == pg.MOUSEMOTION:
                                    self.options.fold_active = (
                                        self.options.fold_rect.collidepoint(
                                            event.pos)
                                    )
                                    self.options.call_active = (
                                        self.options.call_rect.collidepoint(
                                            event.pos)
                                    )
                                    self.options.raise_active = (
                                        self.options.raise_rect.collidepoint(
                                            event.pos)
                                    )

                    # As long as the cards have been dealt
                    if event.type == pg.MOUSEBUTTONUP:
                        # If the user clicks the view cards button
                        if self.options.view_cards_rect.collidepoint(event.pos):
                            if self.viewCards.current_process is None:
                                if not self.viewCards.viewing_cards:
                                    self.viewCards.proccess = [1, 2, 3]
                                    self.viewCards.viewing_cards = True
                                else:
                                    self.viewCards.proccess = [4, 5, 6]
                    elif event.type == pg.MOUSEMOTION:
                        self.options.view_cards_active = (
                            self.options.view_cards_rect.collidepoint(
                                event.pos)
                        )

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(60)

            if self.home_page.in_home:
                self.handle_input()
                self.screen.fill((0, 120, 0))
                self.draw.draw_home()

            elif self.join_lobby.in_lobby:
                self.handle_input()
                self.screen.fill((0, 120, 0))
                self.draw.draw_join_lobby()
            elif self.create_lobby.in_lobby:
                self.handle_input()
                self.screen.fill((0, 120, 0))
                self.draw.draw_create_lobby()
            else:
                # Send your player data over
                self.client.send_object(self.player_list[self.client.id])

                # Receive the other player data back
                data = self.client.receive_object()

                # Sync the players data
                self.client.sync_players(self.player_list, data.player_list)

                self.handle_input(data)

                self.screen.fill((180, 160, 160))

                # If the game hasn't started
                if not data.game_started:
                    if data.ante is None:
                        if self.client.id == data.host:
                            self.draw.draw_ante_option()
                    else:
                        self.draw.draw_ready_option(self.ready)

                # If the game has started
                if data.game_started:
                    # If you are the small blind and havn't bet
                    if (
                        data.small_blind_bet == 0
                        and data.small_blind_player == self.client.id
                    ):
                        self.draw.draw_small_blind(data.ante)
                    # If you are the big blind and havn't bet
                    elif (
                        data.small_blind_bet != 0
                        and data.big_blind_bet == 0
                        and data.big_blind_player == self.client.id
                    ):
                        self.draw.draw_big_blind(data.ante)

                    # If you are the dealer
                    elif data.dealer == self.client.id and not data.has_dealt:
                        # If the blinds have been set
                        if data.small_blind_bet != 0 and data.big_blind_bet != 0:
                            self.draw.draw_deal_option()
                    # If the dealer has dealt and the animation isn't occuring
                    elif self.client.id == data.turn and not data.is_dealing:
                        if not self.viewCards.viewing_cards:
                            if self.raise_option.viewing_raise:
                                self.draw.draw_raise_options(
                                    self.player_list[self.client.id])
                            else:
                                self.draw.draw_options()

                    if data.has_dealt and not data.is_dealing:
                        self.draw.draw_view_cards()

                self.draw.draw_sprites(
                    self.player_list, data.players_connected)
                self.draw.draw_overhead_message(data.overhead_message)
                self.draw.draw_table(data.deck)
                self.draw.draw_pot_text(data.pot)
                self.draw.draw_chips(data.player_list)
                self.draw.draw_all_player_cards(
                    data.all_player_cards, self.client.id)
                self.draw.draw_player_cards(
                    self.player_list[self.client.id].deck,
                    data.all_player_cards,
                    self.client.id,
                )

            pg.display.flip()


game = Game()
game.run()
