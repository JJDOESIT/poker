from player import Player
import pygame as pg


class Data:
    def __init__(self):
        self.turn = 0
        self.dealer = 0
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}

    # Handle players as they ready up
    def handle_ready_up(self, player, id):
        if player.previous_action == "Not ready":
            self.players_ready[id] = False
            return

        if player.previous_action == "Ready":
            self.players_ready[id] = True

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

        while (
            # self.player_list[self.turn].previous_action == "fold"
            self.players_connected[self.turn]
            == "open"
        ):
            if self.turn == 3:
                self.turn = 0
            else:
                self.turn += 1

    # Sync players
    def sync_players(self, player, id):
        self.player_list[id] = player

    # Handle a user's move
    def handle_move(self, player, id):
        if len(player.move) < 1:
            return

        if player.move[0] == "fold":
            self.player_list[id].previous_action = "fold"
            self.overhead_message = player.move[1]
            self.player_list[id].move = []
            self.increament_turn()

    # Reset the server to a blank slate
    def check_for_reset(self):
        for key in self.players_connected.values():
            if key == "taken":
                return
        print("Server reset")
        self.turn = 0
        self.dealer = 0
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
