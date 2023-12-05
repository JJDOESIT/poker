from player import Player
from deck import Deck


class Data:
    def __init__(self):
        self.deck = Deck()
        self.turn = 0
        self.dealer = 0
        self.has_dealt = False
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
        self.received_card = {0: False, 1: False, 2: False, 3: False}

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

    # Deal cards to the player
    def deal_cards(self, player, id):
        if self.has_dealt:
            if not self.received_card[id]:
                player.add_card(self.deck.draw_card())
                player.add_card(self.deck.draw_card())
                self.received_card[id] = True

    # Handle a user's move
    def handle_move(self, player, id):
        if len(player.move) < 1:
            return

        if player.move[0] == "fold":
            self.player_list[id].previous_action = "fold"
            self.overhead_message = f"{player.name} has folded"
            self.player_list[id].move = []
            self.increament_turn()

        elif player.move[0] == "deal":
            self.has_dealt = True
            self.player_list[id].previous_action = "dealt"
            self.overhead_message = f"{player.name} has dealt"
            self.player_list[id].move = []
            self.increament_turn()

    # Reset the server to a blank slate
    def check_for_reset(self):
        for key in self.players_connected.values():
            if key == "taken":
                return
        print("Server reset")
        self.deck = Deck()
        self.turn = 0
        self.dealer = 0
        self.has_dealt = False
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
        self.received_card = {0: False, 1: False, 2: False, 3: False}
