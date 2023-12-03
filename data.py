from player import Player
import pygame as pg


class Data:
    def __init__(self):
        self.turn = 0
        self.id = 0
        self.dealer = 0
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(), Player(), Player(), Player()]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}

    # Initilize the position where each player will be sitting
    def initilize_seats(self):
        seat_positions = [(200, 350), (0, 200), (200, 40), (400, 200)]
        for index in range(4):
            self.player_list[index].seat = seat_positions[index]

    # Initilize the player sprite
    def initilize_sprites(self):
        for player in self.player_list:
            player.player_border_rect = pg.Rect(player.seat[0], player.seat[1], 100, 60)

    # Handle players as they ready up
    def handle_ready_up(self, player):
        if player.previous_action == "Not ready":
            self.players_ready[player.id] = False
            return

        if player.previous_action == "Ready":
            self.players_ready[player.id] = True

            for key, value in self.players_connected.items():
                if value == "taken":
                    if not self.players_ready[key]:
                        return
            self.overhead_message = (
                f"{self.player_list[self.dealer].name} is the dealer"
            )
            self.game_started = True

    # Switch to next players turn
    def increament_turn(self):
        if self.turn == 3:
            self.turn = 0
        else:
            self.turn += 1

        while self.player_list[self.turn].previous_action == "fold":
            if self.turn == 3:
                self.turn = 0
            else:
                self.turn += 1

    # Sync players
    def sync_players(self, player):
        self.player_list[player.id] = player

    # Handle a user's move
    def handle_move(self, player):
        if len(player.move) < 1:
            return

        if player.move[0] == "fold":
            self.player_list[player.id].previous_action = "fold"
            self.overhead_message = player.move[1]
            self.player_list[player.id].move = []
            self.increament_turn()

    # Reset the server to a blank slate
    def check_for_reset(self):
        for key in self.players_connected.values():
            if key == "taken":
                return
        print("Server reset")
        self.turn = 0
        self.id = 0
        self.dealer = 0
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(), Player(), Player(), Player()]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
