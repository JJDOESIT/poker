class Deal:
    def __init__(self, data, animations):
        self.data = data
        self.animations = animations

    # Check if the dealer left
    def check_for_redo(self, id):
        if self.data.dealer == id:
            self.data.dealer = self.data.increament_turn(self.data.dealer)
            self.data.player_receiving_cards = self.data.dealer

    # Deal cards to the player
    def deal_cards(self, id):
        # If the dealing is dealing cards
        if self.data.has_dealt and self.data.is_dealing:
            # If the player is receiving cards
            if self.data.player_receiving_cards == id:
                # If the player has no cards
                if len(self.data.all_player_cards[id]) == 0:
                    card_one = self.data.deck.draw_card()
                    card_one.calculate_end_position(id, 0)
                    card_one.set_orientation(id, 1)
                    self.data.all_player_cards[id].append(card_one)
                    self.data.player_list[id].deck.append(card_one)
                # If the player has one card
                elif len(self.data.all_player_cards[id]) == 1:
                    # If the card is not in it's final position
                    if not self.data.all_player_cards[id][0].in_position:
                        self.data.all_player_cards[id][
                            0
                        ].position = self.animations.lerp_position(
                            self.data.all_player_cards[id][0].position,
                            self.data.all_player_cards[id][0].end_position,
                            self.data.all_player_cards[id][0].tick,
                        )
                        self.data.all_player_cards[id][0].tick += 0.01
                        self.data.all_player_cards[id][0].check_if_in_position(
                        )
                        self.data.all_player_cards[id][
                            0
                        ].angle = self.animations.lerp_number(
                            self.data.all_player_cards[id][0].angle,
                            self.data.all_player_cards[id][0].end_angle,
                            self.data.all_player_cards[id][0].tick,
                        )

                    else:
                        self.data.player_receiving_cards = self.data.increament_turn(
                            self.data.player_receiving_cards
                        )
                        self.data.all_player_cards[id][0].angle -= 360
                        card_two = self.data.deck.draw_card()
                        card_two.calculate_end_position(id, 1)
                        card_two.set_orientation(id, 1)
                        self.data.all_player_cards[id].append(card_two)
                        self.data.player_list[id].deck.append(card_two)

                # If the player has two cards
                elif len(self.data.all_player_cards[id]) == 2:
                    # If the card is not in it's final position
                    if not self.data.all_player_cards[id][1].in_position:
                        self.data.all_player_cards[id][
                            1
                        ].position = self.animations.lerp_position(
                            self.data.all_player_cards[id][1].position,
                            self.data.all_player_cards[id][1].end_position,
                            self.data.all_player_cards[id][1].tick,
                        )
                        self.data.all_player_cards[id][1].tick += 0.01
                        self.data.all_player_cards[id][1].check_if_in_position(
                        )
                        self.data.all_player_cards[id][
                            1
                        ].angle = self.animations.lerp_number(
                            self.data.all_player_cards[id][1].angle,
                            self.data.all_player_cards[id][1].end_angle,
                            self.data.all_player_cards[id][1].tick,
                        )
                    # If the player has been dealt both cards
                    else:
                        self.data.all_player_cards[id][1].angle -= 360
                        self.data.player_receiving_cards = self.data.increament_turn(
                            self.data.player_receiving_cards
                        )

                        # Check if all players have been dealt cards
                        for index in range(len(self.data.all_player_cards)):
                            if self.data.players_connected[index] == "taken":
                                if len(self.data.all_player_cards[index]) < 2:
                                    return
                                elif not self.data.all_player_cards[index][
                                    1
                                ].in_position:
                                    return
                        self.data.turn = self.data.increament_turn(
                            self.data.big_blind_player
                        )
                        self.data.is_dealing = False
