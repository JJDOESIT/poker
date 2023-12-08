class Ready:
    def __init__(self, data):
        self.data = data

    # Handle players as they ready up
    def handle_ready_up(self, player, id):
        # If the player is not readied up
        if player.previous_action == "Not ready":
            self.data.players_ready[id] = False
            return

        # If the player is readied up
        if player.previous_action == "Ready":
            self.data.players_ready[id] = True
            for key, value in self.data.players_connected.items():
                if value == "taken":
                    if not self.data.players_ready[key]:
                        return
            self.data.game_started = True
