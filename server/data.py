from client_server.player import Player
from server.deck import Deck


class Data:
    def __init__(self):
        self.deck = Deck()
        self.host = 0
        self.turn = 0
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
        self.ante = None
        self.dealer = 0
        self.has_dealt = False
        self.is_dealing = False
        self.player_receiving_cards = 0
        self.all_player_cards = {0: [], 1: [], 2: [], 3: []}
        self.big_blind_bet = 0
        self.small_blind_bet = 0
        self.big_blind_player = None
        self.small_blind_player = None
        self.pot = 0

    # Switch to next players turn
    def increament_turn(self, number):
        if number == 3:
            number = 0
        else:
            number += 1
        while (
            # self.player_list[self.turn].previous_action == "fold"
            self.players_connected[number]
            == "open"
        ):
            if number == 3:
                number = 0
            else:
                number += 1
        return number

    # Sync players
    def sync_players(self, player, id):
        self.player_list[id] = player

    # Check if the host left or if the player left during their turn
    def check_for_redo(self, id):
        if self.host == id:
            self.host = self.increament_turn(self.host)
        if self.turn == id:
            self.turn = self.increament_turn(self.turn)

    # Reset the server to a blank slate
    def check_for_reset(self):
        for key in self.players_connected.values():
            if key == "taken":
                return
        print("Server reset")
        self.deck = Deck()
        self.turn = 0
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
        self.ante = None
        self.dealer = 0
        self.has_dealt = False
        self.is_dealing = False
        self.player_receiving_cards = 0
        self.all_player_cards = {0: [], 1: [], 2: [], 3: []}
        self.big_blind_bet = 0
        self.small_blind_bet = 0
        self.big_blind_player = None
        self.small_blind_player = None
