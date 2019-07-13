import json
import pygame
from pygame.locals import *

import components.world as world
import components.player as player
import components.message as mess
import components.display as disp


class Gameplay:

    def __init__(self):
        # Initialize Pygame library
        pygame.init()
        # Load the configuration
        with open('settings/setup.json', encoding='utf8') as setup_file:
            self.game_config = json.load(setup_file)

        self.world = world.World(self.game_config)  # Initialize the world map
        self.player = player.Player(self.game_config)  # Give birth to McGyver
        self.window = disp.Display(self.game_config)  # Initialize the display
        self.start_position = self.world.start_position
        self.end_position = self.world.end_position
        self.player.position = self.world.start_position
        self.items = self.game_config['ITEMS']
        self.clock = pygame.time.Clock()

    def start_loop(self):
        """Wait player clicking Start to begin the game"""
        starting = 1
        while starting:
            self.clock.tick(15)
            start_button = self.window.start_screen()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()  # Get mouse position
                pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()  # Get button clicked
                # Check if the click was in the button OR the return key is pressed
                if (start_button.collidepoint(pos) and pressed1) or\
                        (event.type == KEYDOWN and event.key == K_RETURN):
                    return self.game_loop()
                elif event.type == pygame.QUIT:
                    gaming = 0  # Explicit is better
                    return gaming  # this define what returned in main()

    def game_loop(self):
        """Start the game and loop until you quit, loose or win!"""
        playing = 1
        message = mess.Message.welcome(self.player)
        while playing:
            self.window.map_screen(self.world, self.player, message)
            self.clock.tick(15)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        playing = 0
                    elif event.key == K_UP:
                        playing, message = self._next_action(self.player, (0, -1))
                    elif event.key == K_RIGHT:
                        playing, message = self._next_action(self.player, (1, 0))
                    elif event.key == K_DOWN:
                        playing, message = self._next_action(self.player, (0, 1))
                    elif event.key == K_LEFT:
                        playing, message = self._next_action(self.player, (-1, 0))
                self.window.map_screen(self.world, self.player, message)  # Update the screen
                if playing == 0:
                    return self.end_loop()
                elif event.type == pygame.QUIT:
                    gaming = 0  # Explicit is better
                    return gaming  # this define what returned in main()

    def end_loop(self):
        """Ending screen offer you two options to retry or quit game."""
        ending = 1
        while ending:
            self.clock.tick(15)
            retry_button, quit_button = self.window.end_screen()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()  # Get mouse position
                pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()  # Get button clicked
                # Check if the click was in the button OR the return key is pressed
                if retry_button.collidepoint(pos) and pressed1:
                    gaming = 1  # Explicit is better
                    return gaming  # this define what returned in main()
                elif quit_button.collidepoint(pos) and pressed1:
                    return 0
                elif event.type == pygame.QUIT:
                    return 0

    def _next_action(self, player, movement):
        """Defines the next position of the player"""
        move_x, move_y = movement
        x, y = player.position
        next_position = x + move_x, y + move_y
        return self._define_action(player, next_position)

    def _define_action(self, player, next_position):
        """Check the next position to define the action will be executed"""
        tile = set((next_position, tile)
                   for (coor, tile)
                   in self.world.worldmap
                   if coor == next_position)
        next_tile = list(tile & self.world.worldmap)
        if not next_tile:  # equal next_tile == []. That check if player is moving inside range of map
            action = 0, mess.Message.out_of_range()
            return action
        elif next_tile[0][0] == self.start_position:
            action = 1, mess.Message.back_to_start()
            player.move_on(next_tile[0][0])
            return action
        elif next_tile[0][0] == self.end_position:
            player.move_on(next_tile[0][0])
            if self.required_items() <= player.bag:
                action = 0, mess.Message.you_win()
                return action
            else:
                action = 0, mess.Message.missing_items()
                return action
        elif next_tile[0][1] == '#':
            action = 1, mess.Message.hit_wall()
            return action
        elif next_tile[0][1] in self.items:
            player.move_on(next_tile[0][0])
            item = player.get_item(next_tile[0][1])
            self.world.change_tile(next_tile)
            action = 1, mess.Message.you_found(item)
            return action
        else:
            player.move_on(next_tile[0][0])
            return 1, ""

    def required_items(self):
        """Create a set of required items required if you want to win."""
        required_items = set()
        for item in self.items.items():
            code, spec = item
            if spec['REQUIRED']:
                print('Req:', spec['NAME'])
                required_items.add(spec['NAME'])
        return required_items
