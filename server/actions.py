class Actions:
    def __init__(self, data):
        self.data = data

    # Handle a user's move
    def handle_move(self, player, id):
        if len(player.move) < 1:
            return

        if player.move[0] == "ante":
            self.data.ante = player.move[1][0]
            self.data.overhead_message = f"Ante is ${self.data.ante}"
            self.data.player_list[id].reset_move()

        elif player.move[0] == "small_blind":
            self.data.small_blind_bet = player.move[1][0]
            self.data.pot += self.data.small_blind_bet
            self.data.overhead_message = f"Small blind is ${self.data.small_blind_bet}"
            self.data.player_list[id].reset_move()

        elif player.move[0] == "big_blind":
            self.data.big_blind_bet = player.move[1][0]
            self.data.pot += self.data.big_blind_bet
            self.data.overhead_message = f"Big blind is ${self.data.big_blind_bet}"
            self.data.player_list[id].reset_move()

        elif player.move[0] == "fold":
            self.data.player_list[id].previous_action = "fold"
            self.data.overhead_message = f"{player.name} has folded"
            self.data.player_list[id].reset_move()
            self.data.turn = self.data.increament_turn(self.data.turn)

        elif player.move[0] == "deal":
            self.data.has_dealt = True
            self.data.is_dealing = True
            self.data.player_list[id].previous_action = "dealt"
            self.data.overhead_message = f"{player.name} has dealt"
            self.data.player_list[id].reset_move()
            self.data.turn = self.data.increament_turn(self.data.turn)
