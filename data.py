from player import Player


class Data:
    def __init__(self):
        self.turn = 0
        self.id = 0
        self.player_list = [Player(), Player(), Player(), Player()]
        self.players_connected = {0: "open", 1: "open", 2: "open", 3: "open"}

    # Sync players
    def sync_players(self, player):
        self.player_list[player.id] = player
