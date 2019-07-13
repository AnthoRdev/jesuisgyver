import pygame
import components.message as mess


class Display:
    def __init__(self, game_config):
        # Initialize references Pygame
        self.game_title = game_config["TITLE"]
        self.image_icon = game_config["ICON"]
        self.window_width = game_config["MAP"]["X_TILES"] * game_config["MAP"]["TILE_WIDTH"] + 20
        self.window_height = game_config["MAP"]["Y_TILES"] * game_config["MAP"]["TILE_HEIGHT"] + 80
        self.image_wall = game_config["MAP"]["WALL"]
        self.image_path = game_config["MAP"]["PATH"]
        self.image_player = game_config["PLAYER"]["IMAGE"]
        self.image_guard = game_config["MAP"]["GUARD"]
        self.image_needle = game_config["ITEMS"]["N"]["IMAGE"]
        self.image_tub = game_config["ITEMS"]["T"]["IMAGE"]
        self.image_ether = game_config["ITEMS"]["E"]["IMAGE"]
        self.image_toy = game_config["ITEMS"]["J"]["IMAGE"]

        # Set the game title displayed on window
        pygame.display.set_caption(self.game_title)

        # Set the game icon
        self.icon = pygame.image.load(self.image_icon)
        pygame.display.set_icon(self.icon)

        # Define the window for the game
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.ground_color = (82, 66, 39)
        self.window.fill(self.ground_color)

        # Load visuals elements and set initial place
        self.image_path = pygame.image.load(self.image_path).convert()
        self.image_wall = pygame.image.load(self.image_wall).convert()
        self.image_guard = pygame.image.load(self.image_guard).convert_alpha()
        self.image_needle = pygame.image.load(self.image_needle).convert_alpha()
        self.image_tub = pygame.image.load(self.image_tub).convert_alpha()
        self.image_ether = pygame.image.load(self.image_ether).convert_alpha()
        self.image_toy = pygame.image.load(self.image_toy).convert_alpha()
        self.image_player = pygame.image.load(self.image_player).convert_alpha()

    def start_screen(self):
        button_color = (102, 155, 65)
        self.window.fill(self.ground_color)
        start_button = pygame.draw.rect(self.window, button_color, (100, 150, 270, 150))
        self.display_message("START", [165, 205], "button")
        pygame.display.update()
        return start_button

    def map_screen(self, world, player, message):
        """Defines where and what's have to be displayed on screen"""
        self.window.fill(self.ground_color)
        for position in world.worldmap:
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
            x, y = position[0]  # unpack coordonates
            self.window.blit(image_tile, world.coor_convert(x, y))  # Affect tile image to the converted position
        x, y = player.position
        self.window.blit(self.image_player, world.coor_convert(x, y))
        self.display_message(message, [20, 480], "info")  # First line displayed on screen
        self.display_message(mess.Message.whats_in_bag(player), [20, 500], "info")  # Second line displayed on screen
        pygame.display.update()  # Refresh the screen

    def end_screen(self):
        retry_button_color = (200, 131, 47)
        retry_button = pygame.draw.rect(self.window, retry_button_color, (35, 150, 170, 70))
        quit_button_color = (138, 9, 0)
        quit_button = pygame.draw.rect(self.window, quit_button_color, (265, 150, 170, 70))
        self.display_message("RETRY", [52, 167], "button")
        self.display_message("QUIT", [300, 167], "button")
        pygame.display.update()
        return retry_button, quit_button

    def display_message(self, message, pos, type):
        """Defines where is displayed and how the message look like"""
        if type == "button":
            text_font = pygame.font.Font("fonts/Mario-Kart-DS.ttf", 40)
            font_color = (0, 0, 0)
        else:
            text_font = pygame.font.Font("fonts/RetroGaming.ttf", 13)
            font_color = (255, 255, 255)
        message_text_surface = text_font.render(message, True, font_color)
        self.window.blit(message_text_surface, pos)
