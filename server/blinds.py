class Blinds:
    def __init__(self, data):
        self.data = data

    # Check if the bets need to be re-initilized
    def check_for_redo(self, id, dealer):
        # If the blinds havn't been established, shift them over
        if (
            (self.data.small_blind_bet == 0 and self.data.small_blind_player == id)
            or (self.data.big_blind_bet == 0 and self.data.big_blind_player == id)
            or (
                dealer == id
                and (self.data.small_blind_bet == 0 or self.data.big_blind_bet == 0)
            )
        ):
            self.reset_blinds()
            self.initilize_betting_players()

    # Reset the betting data
    def reset_blinds(self):
        self.data.pot = 0
        self.data.small_blind_bet = 0
        self.data.small_blind_player = None
        self.data.big_blind_bet = 0
        self.data.big_blind_player = None

    # Initilize who is the small and big blind
    def initilize_betting_players(self):
        if self.data.game_started:
            if (
                self.data.big_blind_player is None
                and self.data.small_blind_player is None
            ):
                connected_players = 0

                for connection in self.data.players_connected.values():
                    if connection == "taken":
                        connected_players += 1

                if connected_players == 2:
                    self.data.small_blind_player = self.data.dealer
                    self.data.big_blind_player = self.data.increament_turn(
                        self.data.dealer
                    )

                else:
                    self.data.small_blind_player = self.data.increament_turn(
                        self.data.dealer
                    )
                    self.data.big_blind_player = self.data.increament_turn(
                        self.data.small_blind_player
                    )
                self.data.overhead_message = f"{self.data.player_list[self.data.dealer].name} is the dealer | {self.data.player_list[self.data.small_blind_player].name} is the small blind"
