import pygame as pg


class Draw:
    def __init__(self, screen, home_page, join_lobby, create_lobby, options, ready):
        self.screen = screen
        self.home_page = home_page
        self.join_lobby = join_lobby
        self.create_lobby = create_lobby
        self.options = options
        self.ready = ready
        self.xs_font = pg.font.Font(None, 16)
        self.sm_font = pg.font.Font(None, 24)
        self.md_font = pg.font.Font(None, 32)
        self.lg_font = pg.font.Font(None, 64)

    def draw_overhead_message(self, message):
        overhead_message_text_surface = self.md_font.render(message, True, (0, 0, 0))
        self.screen.blit(
            overhead_message_text_surface,
            (250 - (overhead_message_text_surface.get_width() / 2), 5),
        )

    # Draw the ready up button
    def draw_ready_option(self):
        if self.ready.is_ready:
            pg.draw.rect(
                self.screen, (190, 190, 190), self.ready.ready_rect, border_radius=50
            )
            pg.draw.rect(
                self.screen,
                self.ready.ready_color,
                self.ready.selected_ready_rect,
                border_radius=50,
            )
        else:
            pg.draw.rect(
                self.screen, (190, 190, 190), self.ready.ready_rect, border_radius=50
            )
            pg.draw.rect(
                self.screen,
                self.ready.not_ready_color,
                self.ready.selected_ready_rect,
                border_radius=50,
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

    # Draw the base poker table
    def draw_table(self):
        wood_section = pg.Rect(100, 100, 300, 250)
        gold_section = pg.Rect(115, wood_section.top + 15, 270, 220)
        felt_section = pg.Rect(120, gold_section.top + 5, 260, 210)
        pg.draw.rect(self.screen, (70, 50, 5), wood_section, border_radius=15)
        pg.draw.rect(self.screen, (204, 204, 0), gold_section, border_radius=15)
        pg.draw.rect(self.screen, (0, 100, 0), felt_section, border_radius=15)

    # Draw the home page
    def draw_home(self):
        # Draw home title
        title_text_surface = self.lg_font.render("Local Poker", True, (255, 255, 255))
        self.screen.blit(title_text_surface, (120, 40))

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
        dynamic_name_text_surface = self.md_font.render(
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
        self.screen.blit(exit_text_surface, (20, 17))

        # Draw the "Failed to connect" text
        if self.join_lobby.failed_to_connect:
            failed_text_surface = self.md_font.render(
                "Failed to connect", True, (255, 0, 0)
            )
            self.screen.blit(
                failed_text_surface,
                (
                    self.join_lobby.connect_rect.centerx - 80,
                    self.join_lobby.connect_rect.centery + 30,
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
        self.screen.blit(exit_text_surface, (20, 17))

        # Draw the "Failed to create" text
        if self.create_lobby.failed_to_create:
            failed_text_surface = self.md_font.render(
                "Failed to create", True, (255, 0, 0)
            )
            self.screen.blit(
                failed_text_surface,
                (
                    self.create_lobby.create_rect.centerx - 80,
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
                    self.create_lobby.create_rect.centerx - 80,
                    self.create_lobby.create_rect.centery + 50,
                ),
            )
