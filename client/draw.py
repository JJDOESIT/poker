import pygame as pg
import copy


class Draw:
    def __init__(
        self,
        width,
        height,
        screen,
        home_page,
        join_lobby,
        create_lobby,
        ante,
        blinds,
        cards,
        viewCards,
        animations,
        options,
    ):
        self.width = width
        self.height = height
        self.screen = screen
        self.home_page = home_page
        self.join_lobby = join_lobby
        self.create_lobby = create_lobby
        self.ante = ante
        self.blinds = blinds
        self.cards = cards
        self.viewCards = viewCards
        self.animations = animations
        self.options = options
        self.poker_table = pg.image.load("./images/poker_table.png")
        self.xs_font = pg.font.Font(None, 16)
        self.sm_font = pg.font.Font(None, 32)
        self.md_font = pg.font.Font(None, 64)
        self.lg_font = pg.font.Font(None, 128)
        self.xl_font = pg.font.Font(None, 200)

    # Draw the players personal cards
    def draw_player_cards(self, deck, all_player_cards, id):
        if self.viewCards.viewing_cards:
            if not self.viewCards.cards_initilized:
                self.viewCards.initilize_cards(
                    self.cards.fetch_card(deck[0].number, deck[0].suit),
                    self.cards.fetch_card(deck[1].number, deck[1].suit),
                    all_player_cards[id],
                )

            if self.viewCards.moving_to_hand or self.viewCards.flipping_to_front:
                left_table_card = self.cards.fetch_card(-1, -1)
                right_table_card = self.cards.fetch_card(-1, -1)
            else:
                left_table_card = self.viewCards.left_revealed_card
                right_table_card = self.viewCards.right_revealed_card

            left_table_card = pg.transform.scale(
                left_table_card, (self.viewCards.card_width, self.viewCards.card_height)
            )
            left_table_card = pg.transform.rotate(
                left_table_card, self.viewCards.left_angle
            )
            if self.viewCards.flipping_to_front or self.viewCards.stretching_out_front:
                my_rect = copy.deepcopy(self.viewCards.left_revealed_card_rect)
                my_rect.x += (
                    self.viewCards.end_card_width - self.viewCards.card_width
                ) / 2
                self.screen.blit(left_table_card, my_rect)
            else:
                self.screen.blit(
                    left_table_card,
                    (
                        self.viewCards.left_card_position.x,
                        self.viewCards.left_card_position.y,
                    ),
                )

            right_table_card = pg.transform.scale(
                right_table_card,
                (self.viewCards.card_width, self.viewCards.card_height),
            )
            right_table_card = pg.transform.rotate(
                right_table_card, self.viewCards.right_angle
            )
            right_table_card_rect = right_table_card.get_rect(
                center=self.viewCards.right_revealed_card_rect.center
            )
            if self.viewCards.flipping_to_front or self.viewCards.stretching_out_front:
                my_rect = copy.deepcopy(self.viewCards.right_revealed_card_rect)
                my_rect.x += (
                    self.viewCards.end_card_width - self.viewCards.card_width
                ) / 2
                self.screen.blit(right_table_card, my_rect)

            else:
                self.screen.blit(
                    right_table_card,
                    (
                        self.viewCards.right_card_position.x,
                        self.viewCards.right_card_position.y,
                    ),
                )

            # Lerp
            if self.viewCards.moving_to_hand:
                self.viewCards.left_card_position = self.animations.lerp_position(
                    self.viewCards.left_card_position,
                    self.viewCards.left_end_position,
                    self.viewCards.position_tick,
                )
                self.viewCards.right_card_position = self.animations.lerp_position(
                    self.viewCards.right_card_position,
                    self.viewCards.right_end_position,
                    self.viewCards.position_tick,
                )
                self.viewCards.card_width = self.animations.lerp_number(
                    self.viewCards.card_width,
                    self.viewCards.end_card_width,
                    self.viewCards.position_tick,
                )
                self.viewCards.card_height = self.animations.lerp_number(
                    self.viewCards.card_height,
                    self.viewCards.end_card_height,
                    self.viewCards.position_tick,
                )

                self.viewCards.left_angle = self.animations.lerp_number(
                    self.viewCards.left_angle,
                    self.viewCards.left_end_angle,
                    self.viewCards.position_tick,
                )
                self.viewCards.right_angle = self.animations.lerp_number(
                    self.viewCards.right_angle,
                    self.viewCards.right_end_angle,
                    self.viewCards.position_tick,
                )
                self.viewCards.position_tick += 0.005
                self.viewCards.check_if_in_position()

            elif self.viewCards.flipping_to_front:
                self.viewCards.card_width = self.animations.lerp_number(
                    self.viewCards.card_width,
                    self.viewCards.end_card_width / 10,
                    self.viewCards.flipping_tick,
                )
                self.viewCards.flipping_tick += 0.1
                self.viewCards.check_if_switch()

            elif self.viewCards.stretching_out_front:
                self.viewCards.card_width = self.animations.lerp_number(
                    self.viewCards.card_width,
                    self.viewCards.end_card_width,
                    self.viewCards.flipping_tick,
                )
                self.viewCards.flipping_tick += 0.1
                self.viewCards.check_if_switch()

    # Draw the total pot text
    def draw_pot_text(self, pot):
        if pot != 0:
            pot_text_surface = self.md_font.render(f"Pot: ${pot}", True, (0, 0, 0))
            self.screen.blit(
                pot_text_surface,
                (
                    self.options.view_cards_rect.centerx
                    - (pot_text_surface.get_width() / 2),
                    self.options.view_cards_rect.bottom + 20,
                ),
            )

    # Draw the ante options
    def draw_ante_option(self):
        self.screen.blit(self.ante.two_dollar_img, self.ante.two_dollar_rect)
        self.screen.blit(self.ante.five_dollar_img, self.ante.five_dollar_rect)
        self.screen.blit(self.ante.ten_dollar_img, self.ante.ten_dollar_rect)
        self.screen.blit(self.ante.twenty_dollar_img, self.ante.twenty_dollar_rect)

        # Draw the "Set the ante" text
        ante_text_surface = self.sm_font.render("Set the ante", True, (0, 0, 0))
        self.screen.blit(
            ante_text_surface,
            ((self.width / 2) - (ante_text_surface.get_width() / 2), 850),
        )

    # Draw the small blind options
    def draw_small_blind(self, ante):
        if ante // 2 == 1:
            self.blinds.active_blind = "one_dollar"
            self.screen.blit(self.blinds.one_dollar_img, self.blinds.one_dollar_rect)
        if ante // 2 == 2:
            self.blinds.active_blind = "two_dollar"
            self.screen.blit(self.blinds.two_dollar_img, self.blinds.two_dollar_rect)
        if ante // 2 == 5:
            self.blinds.active_blind = "five_dollar"
            self.screen.blit(self.blinds.five_dollar_img, self.blinds.five_dollar_rect)
        if ante // 2 == 10:
            self.blinds.active_blind = "ten_dollar"
            self.screen.blit(self.blinds.ten_dollar_img, self.blinds.ten_dollar_rect)

        # Draw the "Place small blind" text
        small_blind_text_surface = self.sm_font.render(
            "Place small blind", True, (0, 0, 0)
        )
        self.screen.blit(
            small_blind_text_surface,
            ((self.width / 2) - (small_blind_text_surface.get_width() / 2), 850),
        )

    # Draw the big blind options
    def draw_big_blind(self, ante):
        if ante == 2:
            self.blinds.active_blind = "two_dollar"
            self.screen.blit(self.blinds.two_dollar_img, self.blinds.two_dollar_rect)
        if ante == 5:
            self.blinds.active_blind = "five_dollar"
            self.screen.blit(self.blinds.five_dollar_img, self.blinds.five_dollar_rect)
        if ante == 10:
            self.blinds.active_blind = "ten_dollar"
            self.screen.blit(self.blinds.ten_dollar_img, self.blinds.ten_dollar_rect)
        if ante == 20:
            self.blinds.active_blind = "twenty_dollar"
            self.screen.blit(
                self.blinds.twenty_dollar_img, self.blinds.twenty_dollar_rect
            )

        # Draw the "Place big blind" text
        big_blind_text_surface = self.sm_font.render("Place big blind", True, (0, 0, 0))
        self.screen.blit(
            big_blind_text_surface,
            ((self.width / 2) - (big_blind_text_surface.get_width() / 2), 850),
        )

    # Draw the players cards
    def draw_all_player_cards(self, card_list, id):
        for key, card_set in card_list.items():
            for card in card_set:
                if self.viewCards.viewing_cards:
                    if key == id:
                        break
                card_back = self.cards.fetch_card(-1, -1)
                card_back = pg.transform.scale(card_back, (40, 60))
                card_back = pg.transform.rotate(card_back, card.angle)
                self.screen.blit(card_back, (card.position.x, card.position.y))

    # Draw the base poker table
    def draw_table(self, deck):
        poker_table = pg.transform.scale_by(self.poker_table, 1.5)
        self.screen.blit(
            poker_table,
            (
                self.width / 2 - poker_table.get_width() / 2,
                self.height / 2 - poker_table.get_height() / 2,
            ),
        )

        # Draw the deck of cards
        card_back = self.cards.fetch_card(-1, -1)
        card_back = pg.transform.scale(card_back, (40, 60))
        for card in deck.deck:
            self.screen.blit(card_back, (card.position.x, card.position.y))

    # Draw the overhead message
    def draw_overhead_message(self, message):
        overhead_message_text_surface = self.md_font.render(message, True, (0, 0, 0))
        self.screen.blit(
            overhead_message_text_surface,
            (self.width / 2 - overhead_message_text_surface.get_width() / 2, 25),
        )

    # Draw the view cards button
    def draw_view_cards(self):
        if self.options.view_cards_active:
            pg.draw.rect(
                self.screen,
                self.options.active_color,
                self.options.view_cards_rect,
                border_radius=30,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.options.passive_color,
                self.options.view_cards_rect,
                border_radius=30,
            )

        # Draw the "View Cards" text
        view_cards_text_surface = self.sm_font.render("View Cards", True, (0, 0, 0))
        self.screen.blit(
            view_cards_text_surface,
            (
                self.options.view_cards_rect.centerx
                - (view_cards_text_surface.get_width() / 2),
                self.options.view_cards_rect.centery
                - (view_cards_text_surface.get_height() / 2),
            ),
        )

    # Draw the ready up button
    def draw_ready_option(self, ready):
        if ready.is_ready:
            pg.draw.rect(
                self.screen, (190, 190, 190), ready.ready_rect, border_radius=50
            )
            pg.draw.rect(
                self.screen,
                ready.ready_color,
                ready.selected_ready_rect,
                border_radius=50,
            )
        else:
            pg.draw.rect(
                self.screen, (190, 190, 190), ready.ready_rect, border_radius=50
            )
            pg.draw.rect(
                self.screen,
                ready.not_ready_color,
                ready.selected_ready_rect,
                border_radius=50,
            )

    # Draw the deal cards option
    def draw_deal_option(self):
        if self.options.deal_active:
            pg.draw.rect(
                self.screen,
                self.options.active_color,
                self.options.deal_rect,
                border_radius=30,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.options.passive_color,
                self.options.deal_rect,
                border_radius=30,
            )

        # Draw the "Deal" text
        deal_text_surface = self.md_font.render("Deal", True, (0, 0, 0))
        self.screen.blit(
            deal_text_surface,
            (
                self.options.deal_rect.centerx - (deal_text_surface.get_width() / 2),
                self.options.deal_rect.centery - (deal_text_surface.get_height() / 2),
            ),
        )

    # Draw the options for a turn
    def draw_options(self):
        # Draw the fold option
        if self.options.fold_active:
            pg.draw.rect(
                self.screen,
                self.options.active_color,
                self.options.fold_rect,
                border_radius=30,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.options.passive_color,
                self.options.fold_rect,
                border_radius=30,
            )

        # Draw the call option
        if self.options.call_active:
            pg.draw.rect(
                self.screen,
                self.options.active_color,
                self.options.call_rect,
                border_radius=30,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.options.passive_color,
                self.options.call_rect,
                border_radius=30,
            )

        # Draw the raise option
        if self.options.raise_active:
            pg.draw.rect(
                self.screen,
                self.options.active_color,
                self.options.raise_rect,
                border_radius=30,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.options.passive_color,
                self.options.raise_rect,
                border_radius=30,
            )

        # Draw the "Raise" text
        fold_text_surface = self.md_font.render("Fold", True, (0, 0, 0))
        self.screen.blit(
            fold_text_surface,
            (
                self.options.fold_rect.centerx - (fold_text_surface.get_width() / 2),
                self.options.fold_rect.centery - (fold_text_surface.get_height() / 2),
            ),
        )

        # Draw the "Call" text
        call_text_surface = self.md_font.render("Call", True, (0, 0, 0))
        self.screen.blit(
            call_text_surface,
            (
                self.options.call_rect.centerx - (call_text_surface.get_width() / 2),
                self.options.call_rect.centery - (call_text_surface.get_height() / 2),
            ),
        )

        # Draw the "Raise" text
        raise_text_surface = self.md_font.render("Raise", True, (0, 0, 0))
        self.screen.blit(
            raise_text_surface,
            (
                self.options.raise_rect.centerx - (raise_text_surface.get_width() / 2),
                self.options.raise_rect.centery - (raise_text_surface.get_height() / 2),
            ),
        )

    # Draw the player sprites
    def draw_sprites(self, player_list, players_connected):
        for index in range(4):
            if players_connected[index] == "taken":
                pg.draw.rect(
                    self.screen,
                    (225, 225, 225),
                    player_list[index].player_border_rect,
                )
                # Display the players name
                name_text_surface = self.xs_font.render(
                    player_list[index].name, True, (0, 0, 0)
                )
                self.screen.blit(
                    name_text_surface,
                    (
                        player_list[index].player_border_rect.centerx
                        - (name_text_surface.get_width() / 2),
                        player_list[index].player_border_rect.top + 5,
                    ),
                )

                # Display the players money
                money_text_surface = self.xs_font.render(
                    "$" + str(player_list[index].money), True, (0, 0, 0)
                )
                self.screen.blit(
                    money_text_surface,
                    (
                        player_list[index].player_border_rect.centerx
                        - (money_text_surface.get_width() / 2),
                        player_list[index].player_border_rect.centery - 5,
                    ),
                )

                # Display the players previous action
                previous_action_text_surface = self.xs_font.render(
                    player_list[index].previous_action, True, (0, 0, 0)
                )
                self.screen.blit(
                    previous_action_text_surface,
                    (
                        player_list[index].player_border_rect.centerx
                        - (previous_action_text_surface.get_width() / 2),
                        player_list[index].player_border_rect.bottom
                        - (previous_action_text_surface.get_height())
                        - 5,
                    ),
                )

    # Draw the home page
    def draw_home(self):
        # Draw home title
        title_text_surface = self.xl_font.render("Local Poker", True, (255, 255, 255))
        self.screen.blit(
            title_text_surface,
            ((self.width / 2) - (title_text_surface.get_width() / 2), 150),
        )

        # Draw join button
        if self.home_page.join_active:
            pg.draw.rect(
                self.screen, self.home_page.active_color, self.home_page.join_rect
            )
        else:
            pg.draw.rect(
                self.screen, self.home_page.passive_color, self.home_page.join_rect
            )

        # Draw create button
        if self.home_page.create_active:
            pg.draw.rect(
                self.screen, self.home_page.active_color, self.home_page.create_rect
            )
        else:
            pg.draw.rect(
                self.screen, self.home_page.passive_color, self.home_page.create_rect
            )

        # Draw join text
        join_text_surface = self.md_font.render("Join Lobby", True, (0, 0, 0))
        self.screen.blit(
            join_text_surface,
            (
                self.home_page.join_rect.centerx - (join_text_surface.get_width() / 2),
                self.home_page.join_rect.centery - (join_text_surface.get_height() / 2),
            ),
        )

        # Draw create text
        create_text_surface = self.md_font.render("Create Lobby", True, (0, 0, 0))
        self.screen.blit(
            create_text_surface,
            (
                self.home_page.create_rect.centerx
                - (create_text_surface.get_width() / 2),
                self.home_page.create_rect.centery
                - (create_text_surface.get_height() / 2),
            ),
        )

    # Draw the join_lobby page
    def draw_join_lobby(self):
        # Draw the text input box
        if self.join_lobby.type_ip_active:
            pg.draw.rect(
                self.screen, self.join_lobby.active_color, self.join_lobby.input_ip_rect
            )
        else:
            pg.draw.rect(
                self.screen,
                self.join_lobby.passive_color,
                self.join_lobby.input_ip_rect,
            )

        # Draw the port input box
        if self.join_lobby.type_port_active:
            pg.draw.rect(
                self.screen,
                self.join_lobby.active_color,
                self.join_lobby.input_port_rect,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.join_lobby.passive_color,
                self.join_lobby.input_port_rect,
            )

        # Draw the name box
        if self.join_lobby.type_name_active:
            pg.draw.rect(
                self.screen,
                self.join_lobby.active_color,
                self.join_lobby.input_name_rect,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.join_lobby.passive_color,
                self.join_lobby.input_name_rect,
            )

        # Draw the connect button
        if self.join_lobby.connect_active:
            pg.draw.rect(
                self.screen,
                self.join_lobby.active_color,
                self.join_lobby.connect_rect,
                border_radius=50,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.join_lobby.passive_color,
                self.join_lobby.connect_rect,
                border_radius=50,
            )

        # Draw the exit button
        if self.join_lobby.exit_active:
            pg.draw.rect(
                self.screen,
                (160, 160, 160),
                self.join_lobby.exit_rect,
                border_radius=50,
            )
        else:
            pg.draw.rect(
                self.screen, (0, 120, 0), self.join_lobby.exit_rect, border_radius=50
            )

        # Draw the "Join Lobby" text
        join_title_text_surface = self.lg_font.render(
            "Join Lobby", True, (255, 255, 255)
        )
        self.screen.blit(
            join_title_text_surface,
            ((self.width / 2) - (join_title_text_surface.get_width() / 2), 40),
        )

        # Draw the "Connect" text
        connect_text_surface = self.md_font.render("Connect", True, (0, 0, 0))
        self.screen.blit(
            connect_text_surface,
            (
                self.join_lobby.connect_rect.centerx
                - (connect_text_surface.get_width() / 2),
                self.join_lobby.connect_rect.centery
                - (connect_text_surface.get_height() / 2),
            ),
        )

        # Draw the "Server IP:" text
        static_ip_text_surface = self.md_font.render(
            "Server IP:", True, (255, 255, 255)
        )
        self.screen.blit(
            static_ip_text_surface,
            (
                self.join_lobby.input_ip_rect.left,
                self.join_lobby.input_ip_rect.top - static_ip_text_surface.get_height(),
            ),
        )

        # Draw the "Port:" text
        port_text_surface = self.md_font.render("Port:", True, (255, 255, 255))
        self.screen.blit(
            port_text_surface,
            (
                self.join_lobby.input_port_rect.left,
                self.join_lobby.input_port_rect.top - port_text_surface.get_height(),
            ),
        )

        # Draw the "Name:" text
        name_text_surface = self.md_font.render("Username:", True, (255, 255, 255))
        self.screen.blit(
            name_text_surface,
            (
                self.join_lobby.input_name_rect.left,
                self.join_lobby.input_name_rect.top - name_text_surface.get_height(),
            ),
        )

        # Draw the ip address text
        dynamic_ip_text_surface = self.md_font.render(
            self.join_lobby.lobby_ip, True, (0, 0, 0)
        )
        self.screen.blit(
            dynamic_ip_text_surface,
            (
                self.join_lobby.input_ip_rect.left,
                self.join_lobby.input_ip_rect.centery
                - (dynamic_ip_text_surface.get_height() / 2),
            ),
        )

        # Draw the dyanmic port text
        dynamic_port_text_surface = self.md_font.render(
            self.join_lobby.port, True, (0, 0, 0)
        )
        self.screen.blit(
            dynamic_port_text_surface,
            (
                self.join_lobby.input_port_rect.left,
                self.join_lobby.input_port_rect.centery
                - (dynamic_port_text_surface.get_height() / 2),
            ),
        )

        # Draw the dyanmic name text
        dynamic_name_text_surface = self.sm_font.render(
            self.join_lobby.name, True, (0, 0, 0)
        )
        self.screen.blit(
            dynamic_name_text_surface,
            (
                self.join_lobby.input_name_rect.left,
                self.join_lobby.input_name_rect.centery
                - (dynamic_name_text_surface.get_height() / 2),
            ),
        )

        # Draw the X
        exit_text_surface = self.md_font.render("X", True, (255, 0, 0))
        self.screen.blit(
            exit_text_surface,
            (
                self.join_lobby.exit_rect.centerx - (exit_text_surface.get_width() / 2),
                self.join_lobby.exit_rect.centery
                - (exit_text_surface.get_height() / 2),
            ),
        )

        # Draw the "Failed to connect" text
        if self.join_lobby.failed_to_connect:
            failed_text_surface = self.md_font.render(
                "Failed to connect", True, (255, 0, 0)
            )
            self.screen.blit(
                failed_text_surface,
                (
                    (self.width / 2) - (failed_text_surface.get_width() / 2),
                    self.join_lobby.connect_rect.centery + 50,
                ),
            )

    # Draw the create lobby page
    def draw_create_lobby(self):
        # Draw the ip text input box
        if self.create_lobby.type_ip_active:
            pg.draw.rect(
                self.screen,
                self.create_lobby.active_color,
                self.create_lobby.input_ip_rect,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.create_lobby.passive_color,
                self.create_lobby.input_ip_rect,
            )

        # Draw the auto connect checkbox
        if self.create_lobby.auto_connect:
            pg.draw.rect(
                self.screen,
                (255, 255, 255),
                self.create_lobby.auto_connect_rect,
                border_radius=50,
            )
            pg.draw.rect(
                self.screen, (0, 0, 0), self.create_lobby.checked_box, border_radius=50
            )
        else:
            pg.draw.rect(
                self.screen,
                (255, 255, 255),
                self.create_lobby.auto_connect_rect,
                border_radius=50,
            )

        # Draw the port text input box
        if self.create_lobby.type_port_active:
            pg.draw.rect(
                self.screen,
                self.create_lobby.active_color,
                self.create_lobby.input_port_rect,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.create_lobby.passive_color,
                self.create_lobby.input_port_rect,
            )

        # Draw the create button
        if self.create_lobby.connect_active:
            pg.draw.rect(
                self.screen,
                self.create_lobby.active_color,
                self.create_lobby.create_rect,
                border_radius=50,
            )
        else:
            pg.draw.rect(
                self.screen,
                self.create_lobby.passive_color,
                self.create_lobby.create_rect,
                border_radius=50,
            )

        # Draw the exit button
        if self.create_lobby.exit_active:
            pg.draw.rect(
                self.screen,
                (160, 160, 160),
                self.create_lobby.exit_rect,
                border_radius=50,
            )
        else:
            pg.draw.rect(
                self.screen, (0, 120, 0), self.create_lobby.exit_rect, border_radius=50
            )

        # Draw the "Create Lobby" text
        create_title_text_surface = self.lg_font.render(
            "Create Lobby", True, (255, 255, 255)
        )
        self.screen.blit(
            create_title_text_surface,
            ((self.width / 2) - (create_title_text_surface.get_width() / 2), 40),
        )

        # Draw the "Create" text
        connect_text_surface = self.md_font.render("Create", True, (0, 0, 0))
        self.screen.blit(
            connect_text_surface,
            (
                self.create_lobby.create_rect.centerx
                - (connect_text_surface.get_width() / 2),
                self.create_lobby.create_rect.centery
                - (connect_text_surface.get_height() / 2),
            ),
        )

        # Draw the "External IP:" text
        static_ip_text_surface = self.md_font.render(
            "External IP:", True, (255, 255, 255)
        )
        self.screen.blit(
            static_ip_text_surface,
            (
                self.create_lobby.input_ip_rect.left,
                self.create_lobby.input_ip_rect.top
                - static_ip_text_surface.get_height(),
            ),
        )

        # Draw the "Port:" text
        static_port_text_surface = self.md_font.render("Port:", True, (255, 255, 255))
        self.screen.blit(
            static_port_text_surface,
            (
                self.create_lobby.input_port_rect.left,
                self.create_lobby.input_port_rect.top
                - static_port_text_surface.get_height(),
            ),
        )

        # Draw the "Auto-Connect:" text
        auto_connect_text_surface = self.sm_font.render(
            "Auto-Connect:", True, (255, 255, 255)
        )
        self.screen.blit(
            auto_connect_text_surface,
            (
                self.create_lobby.auto_connect_rect.centerx
                - (auto_connect_text_surface.get_width() / 2),
                self.create_lobby.input_port_rect.top
                - auto_connect_text_surface.get_height(),
            ),
        )

        # Draw the dynamic ip address text
        dynamic_ip_text_surface = self.md_font.render(
            self.create_lobby.external_ip, True, (0, 0, 0)
        )
        self.screen.blit(
            dynamic_ip_text_surface,
            (
                self.create_lobby.input_ip_rect.left,
                self.create_lobby.input_ip_rect.centery
                - (dynamic_ip_text_surface.get_height() / 2),
            ),
        )

        # Draw the port text
        dynamic_port_text_surface = self.md_font.render(
            self.create_lobby.port, True, (0, 0, 0)
        )
        self.screen.blit(
            dynamic_port_text_surface,
            (
                self.create_lobby.input_port_rect.left,
                self.create_lobby.input_port_rect.centery
                - (dynamic_port_text_surface.get_height() / 2),
            ),
        )

        # Draw the X
        exit_text_surface = self.md_font.render("X", True, (255, 0, 0))
        self.screen.blit(
            exit_text_surface,
            (
                self.create_lobby.exit_rect.centerx
                - (exit_text_surface.get_width() / 2),
                self.create_lobby.exit_rect.centery
                - (exit_text_surface.get_height() / 2),
            ),
        )

        # Draw the "Failed to create" text
        if self.create_lobby.failed_to_create:
            failed_text_surface = self.md_font.render(
                "Failed to create", True, (255, 0, 0)
            )
            self.screen.blit(
                failed_text_surface,
                (
                    (self.width / 2 - failed_text_surface.get_width() / 2),
                    self.create_lobby.create_rect.centery + 50,
                ),
            )
        elif self.create_lobby.success:
            success_text_surface = self.md_font.render(
                "Lobby Created", True, (0, 255, 0)
            )
            self.screen.blit(
                success_text_surface,
                (
                    (self.width / 2 - success_text_surface.get_width() / 2),
                    self.create_lobby.create_rect.centery + 50,
                ),
            )
