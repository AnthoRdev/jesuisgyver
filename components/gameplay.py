import json
import pygame
from pygame.locals import *


import components.map as map
import components.player as player
import components.display as disp


class Gameplay:

    def __init__(self):
        # Load the configuration
        with open('setup.json', encoding='utf8') as game_config:
            my_config = json.load(game_config)
            # assert type(my_config) is dict  # convertir en dictionnaire? vu sur developpez.net
        # Initialize the world map
        self.world = map.World(my_config)
        print(self.world)  # statistic and details of the world map
        # Give birth to McGyver
        self.gyver = player.Player(my_config)

        self.position = self.world.start_position
        self.start_position = self.world.start_position
        self.end_position = self.world.end_position
        self.gyver.position = self.start_position
        self.items = my_config['ITEMS']
        self.world = self.world
        self.display = disp.Display()

        # Initialize references Pygame
        self.game_title = my_config["TITLE"]
        self.image_icon = my_config["ICON"]
        self.window_width = my_config["MAP"]["X_TILES"] * my_config["MAP"]["TILE_WIDTH"]
        self.window_height = my_config["MAP"]["Y_TILES"] * my_config["MAP"]["TILE_HEIGHT"]
        self.image_wall = my_config["MAP"]["WALL"]
        self.image_path = my_config["MAP"]["PATH"]
        self.gyver_image = my_config["PLAYER"]["IMAGE"]
        self.image_guard = my_config["MAP"]["GUARD"]
        self.image_needle = my_config["ITEMS"]["N"]["IMAGE"]
        self.image_tub = my_config["ITEMS"]["T"]["IMAGE"]
        self.image_ether = my_config["ITEMS"]["E"]["IMAGE"]
        self.image_toy = my_config["ITEMS"]["E"]["IMAGE"]  # TODO Ajouter une image de canard

        # Initialize Pygame
        pygame.init()

        # Set the game title displayed on window
        pygame.display.set_caption(self.game_title)

        # Set the game icon
        self.icon = pygame.image.load(self.image_icon)
        pygame.display.set_icon(self.icon)

        # Define the window for the game
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Load visuals elements and set initial place
        self.image_path = pygame.image.load(self.image_path).convert()
        self.image_wall = pygame.image.load(self.image_wall).convert()
        self.image_guard = pygame.image.load(self.image_guard).convert()
        self.image_needle = pygame.image.load(self.image_needle).convert()
        self.image_tub = pygame.image.load(self.image_tub).convert()
        self.image_tub.set_colorkey((255, 255, 255))
        self.image_ether = pygame.image.load(self.image_ether).convert()
        self.image_ether.set_colorkey((255, 255, 255))
        self.image_toy = pygame.image.load(self.image_toy).convert()

        self.pion_gyver = pygame.image.load(self.gyver_image).convert()

        for position in self.world.worldmap:
            if position[1] != "#":
                image_tile = self.image_path
                if position[1] == "O":
                    image_tile = self.image_guard
                elif position[1] == "N":
                    image_tile = self.image_needle
                elif position[1] == "T":
                    image_tile = self.image_tub
                elif position[1] == "E":
                    image_tile = self.image_ether
                elif position[1] == "J":
                    image_tile = self.image_toy
            else:
                image_tile = self.image_wall
            x, y = position[0]
            self.window.blit(image_tile, self.world.coor_convert(x, y))
        x, y = self.gyver.position
        self.window.blit(self.pion_gyver, self.world.coor_convert(x, y))
        pygame.display.update()

    def game_loop(self):
        # Start the game
        playing = 1
        clock = pygame.time.Clock()
        while playing:
            clock.tick(15)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    x_old, y_old = self.gyver.position
                    if event.key == K_ESCAPE:
                        playing = self.choose_action(self.gyver, 'q')
                    if event.key == K_UP:
                        playing = self.choose_action(self.gyver, 'w')
                    if event.key == K_RIGHT:
                        playing = self.choose_action(self.gyver, 's')
                    if event.key == K_DOWN:
                        playing = self.choose_action(self.gyver, 'z')
                    if event.key == K_LEFT:
                        playing = self.choose_action(self.gyver, 'a')

                    self.window.blit(self.image_path, self.world.coor_convert(x_old, y_old))
                    x, y = self.gyver.position
                    self.window.blit(self.pion_gyver, self.world.coor_convert(x, y))
                    pygame.display.update()

    def choose_action(self, player, game_input=None):
        """listen the terminal to choose wich action to make"""
        print(player)

        if game_input is None:
            game_input = input(self.display.where_we_going())

        if game_input == "w":
            return self._move_up(player)
        elif game_input == "a":
            return self._move_left(player)
        elif game_input == "s":
            return self._move_right(player)
        elif game_input == "z":
            return self._move_down(player)
        elif game_input == "q":
            # serious = input(self.display.are_u_sure())
            # if serious == "yes":
            #     return self._after_death(player)
            # else:
            #     return self.choose_action(player)
            return 0
        else:
            print(self.display.kidding_me())
            self.choose_action(player)

    def _move_up(self, player):
        x, y = player.position
        next_position = x, y + 1
        return self._define_action(player, next_position)

    def _move_down(self, player):
        x, y = player.position
        next_position = x, y - 1
        return self._define_action(player, next_position)

    def _move_left(self, player):
        x, y = player.position
        next_position = x - 1, y
        return self._define_action(player, next_position)

    def _move_right(self, player):
        x, y = player.position
        next_position = x + 1, y
        return self._define_action(player, next_position)

    def _define_action(self, player, next_position):
        """Check the next position to define the action will be executed"""
        tile = set((next_position, tile) for (coor, tile) in self.world.worldmap if coor == next_position)
        # test d'appartenance pour verifier s'il fait parti du set, recupere la tuile et
        # converti en liste (pour pouvoir utiliser [0], impossible dans un set)
        next_tile = list(tile & self.world.worldmap)  # TODO voir s'il est possible de rester en set
        if not next_tile:  # equal next_tile == []
            self.display.out_of_range()
            return self._after_death(player)
        elif next_tile[0][0] == self.start_position:
            self.display.back_to_start()
            player.move_on(next_tile[0][0])
            # self.choose_action(player)
            return 1
        elif next_tile[0][0] == self.end_position:
            self.display.what_in_bag(player)
            player.move_on(next_tile[0][0])
            if {'Needle', 'Tub', 'Ether'} <= player.bag:  # TODO creer liste d'objets requis
                return self._is_winner(player)
            else:
                self.display.missing_items()
                return self._after_death(player)
        elif next_tile[0][1] == '#':
            self.display.hit_wall()
            # self.choose_action(player)
            return 1
        elif next_tile[0][1] in self.items:
            player.move_on(next_tile[0][0])
            player.get_item(next_tile[0][1])
            self.world.change_tile(next_tile)
            # self.choose_action(player)
            return 1
        else:
            player.move_on(next_tile[0][0])
            # self.choose_action(player)
            return 1

    def _is_winner(self, player):
        self.display.you_win()
        return self._after_death(player)

    def _after_death(self, player):
        try_again = input(self.display.ask_retry())
        if try_again == "y":
            self.display.retry()
            player.bag.clear()  # TODO Ne pas oublier de replacer les objets !!
            player.position = self.start_position
            # self.choose_action(player)
            return 1
        elif try_again == "n":
            return 0
        else:
            self.display.shutdown()
            return 0
