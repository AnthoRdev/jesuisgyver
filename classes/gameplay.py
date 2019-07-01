import classes.display as disp


class Gameplay:

    def __init__(self, my_config, world, player, playing):
        self.position = world.start_position
        self.start_position = world.start_position
        self.end_position = world.end_position
        player.position = self.start_position
        self.items = my_config['ITEMS']
        self.world = world
        self.display = disp.Display()
        self.playing = playing

    def choose_action(self, player, game_input=None):
        """listen the terminal to choose wich action to make"""
        print(player)

        if game_input is None:
            game_input = input(self.display.where_we_going())

        if game_input == "w":
            self._move_up(player)
        elif game_input == "a":
            self._move_left(player)
        elif game_input == "s":
            self._move_right(player)
        elif game_input == "z":
            self._move_down(player)
        elif game_input == "q":
            serious = input(self.display.are_u_sure())
            if serious == "yes":
                self.playing = self._after_death(player)
            else:
                self.choose_action(player)
        else:
            print(self.display.kidding_me())
            self.choose_action(player)

    def _move_up(self, player):
        x, y = player.position
        next_position = x, y + 1
        self._define_action(player, next_position)

    def _move_down(self, player):
        x, y = player.position
        next_position = x, y - 1
        self._define_action(player, next_position)

    def _move_left(self, player):
        x, y = player.position
        next_position = x - 1, y
        self._define_action(player, next_position)

    def _move_right(self, player):
        x, y = player.position
        next_position = x + 1, y
        self._define_action(player, next_position)

    def _define_action(self, player, next_position):
        """Check the next position to define the action will be executed"""
        tile = set((next_position, tile) for (coor, tile) in self.world.worldmap if coor == next_position)
        # test d'appartenance pour verifier s'il fait parti du set, recupere la tuile et
        # converti en liste (pour pouvoir utiliser [0], impossible dans un set)
        next_tile = list(tile & self.world.worldmap)  # TODO voir s'il est possible de rester en set
        if not next_tile:  # equal next_tile == []
            self.display.out_of_range()
            self._after_death(player)
        elif next_tile[0][0] == self.start_position:
            self.display.back_to_start()
            player.move_on(next_tile[0][0])
            self.choose_action(player)
        elif next_tile[0][0] == self.end_position:
            self.display.what_in_bag(player)
            player.move_on(next_tile[0][0])
            if {'Needle', 'Tub', 'Ether'} <= player.bag:  # TODO creer liste d'objets requis
                self._is_winner(player)
            else:
                self.display.missing_items()
                self._after_death(player)
        elif next_tile[0][1] == '#':
            self.display.hit_wall()
            self.choose_action(player)
        elif next_tile[0][1] in self.items:
            player.move_on(next_tile[0][0])
            player.get_item(next_tile[0][1])
            self.world.change_tile(next_tile)
            self.choose_action(player)
        else:
            player.move_on(next_tile[0][0])
            self.choose_action(player)

    def _is_winner(self, player):
        self.display.you_win()
        self._after_death(player)

    def _after_death(self, player):
        try_again = input(self.display.ask_retry())
        if try_again == "y":
            self.display.retry()
            player.bag.clear()
            player.position = self.start_position
            self.choose_action(player)
        elif try_again == "n":
            # self.display.
            return 0
        else:
            self.display.shutdown()
            return 0
