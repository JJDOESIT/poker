from player import Player
from deck import Deck


class Data:
    def __init__(self):
        self.deck = Deck()
        self.turn = 0
        self.dealer = 0
        self.has_dealt = False
        self.is_dealing = False
        self.player_receiving_cards = 0
        self.all_player_cards = {0: [[], 0], 1: [[], 0], 2: [[], 0], 3: [[], 0]}
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}

    # Handle players as they ready up
    def handle_ready_up(self, player, id):
        # If the player is not readied up
        if player.previous_action == "Not ready":
            self.players_ready[id] = False
            return
        # If the player is readied up
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

    # Deal cards to the player
    def deal_cards(self, id):
        # If the dealing is dealing cards
        if self.has_dealt and self.is_dealing:
            # If the player is receiving cards
            if self.player_receiving_cards == id:
                # If the player has no cards
                if self.all_player_cards[id][1] == 0:
                    card_one = self.deck.draw_card()
                    card_one.calculate_end_position(id, 1)
                    card_one.set_orientation(id, 1)
                    self.all_player_cards[id][0].append(card_one)
                    self.player_list[id].deck.append(card_one)
                    self.all_player_cards[id][1] += 1
                # If the player has one card
                elif self.all_player_cards[id][1] == 1:
                    # If the card is not in it's final position
                    if not self.all_player_cards[id][0][0].in_position:
                        self.all_player_cards[id][0][0].lerp()
                        self.all_player_cards[id][0][0].slerp()
                        if self.all_player_cards[id][0][0].check_if_in_position():
                            self.player_receiving_cards = self.increament_turn(
                                self.player_receiving_cards
                            )
                    else:
                        card_two = self.deck.draw_card()
                        card_two.calculate_end_position(id, 2)
                        card_two.set_orientation(id, 1)
                        self.all_player_cards[id][0].append(card_two)
                        self.player_list[id].deck.append(card_two)
                        self.all_player_cards[id][1] += 1

                # If the player has two cards
                elif self.all_player_cards[id][1] == 2:
                    # If the card is not in it's final position
                    if not self.all_player_cards[id][0][1].in_position:
                        self.all_player_cards[id][0][1].lerp()
                        self.all_player_cards[id][0][1].slerp()
                    # If the player has been dealt both cards
                    else:
                        self.all_player_cards[id][1] = -1
                        self.player_receiving_cards = self.increament_turn(
                            self.player_receiving_cards
                        )

                        for index in range(len(self.all_player_cards)):
                            if (
                                self.players_connected[index] == "taken"
                                and self.all_player_cards[index][1] != -1
                            ):
                                return
                        self.is_dealing = False

    # Handle a user's move
    def handle_move(self, player, id):
        if len(player.move) < 1:
            return

        if player.move[0] == "fold":
            self.player_list[id].previous_action = "fold"
            self.overhead_message = f"{player.name} has folded"
            self.player_list[id].move = []
            self.turn = self.increament_turn(self.turn)

        elif player.move[0] == "deal":
            self.has_dealt = True
            self.is_dealing = True
            self.player_list[id].previous_action = "dealt"
            self.overhead_message = f"{player.name} has dealt"
            self.player_list[id].move = []
            self.turn = self.increament_turn(self.turn)

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
        self.is_dealing = False
        self.player_receiving_cards = 0
        self.all_player_cards = {0: [[], 0], 1: [[], 0], 2: [[], 0], 3: [[], 0]}
        self.overhead_message = ""
        self.game_started = False
        self.players_ready = [False, False, False, False]
        self.player_list = [Player(0), Player(1), Player(2), Player(3)]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}
