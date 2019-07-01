import json
import pygame
from pygame.locals import *


import classes.gameplay as gp
import classes.map as map
import classes.player as player


def main():
    # BOUCLE PRINCIPALE
    # continuer = 1
    # while continuer:
    #     # Chargement et affichage de l'écran d'accueil
    #     accueil = pygame.image.load(image_accueil).convert()
    #     fenetre.blit(accueil, (0, 0))
    #     # Rafraichissement
    #     pygame.display.flip()
    #     # # On remet ces variables à 1 à chaque tour de boucle
    #     # continuer_jeu = 1
    #     # continuer_accueil = 1
    #     #
    #     # # BOUCLE D'ACCUEIL
    #     # while continuer_accueil:
    #     #     # Limitation de vitesse de la boucle
    #     #     pygame.time.Clock().tick(30)

    # Load the configuration
    with open('setup.json', encoding='utf8') as game_config:
        my_config = json.load(game_config)
        # assert type(my_config) is dict  # convertir en dictionnaire? vu sur developpez.net

    # Initialize the world map
    world = map.World(my_config)
    # print(world)  # statistic and details of the world map

    # Give birth to McGyver
    gyver = player.Player(my_config)

    # Initialize references Pygame
    game_title = my_config["TITLE"]
    image_icon = my_config["ICON"]
    window_width = my_config["MAP"]["X_TILES"] * my_config["MAP"]["TILE_WIDTH"]
    window_height = my_config["MAP"]["Y_TILES"] * my_config["MAP"]["TILE_HEIGHT"]
    image_background = my_config["MAP"]["WALL"]
    image_wall = my_config["MAP"]["WALL"]
    image_path = my_config["MAP"]["PATH"]
    pion_gyver = my_config["PLAYER"]["IMAGE"]

    # Initialize Pygame
    pygame.init()

    # Set the game title displayed on window
    pygame.display.set_caption(game_title)

    # Set the game icon
    icon = pygame.image.load(image_icon)
    pygame.display.set_icon(icon)

    # Define the window for the game
    window = pygame.display.set_mode((window_width, window_height), RESIZABLE)

    # Load visuals elements and set initial place
    background = pygame.image.load(image_background).convert()
    image_wall = pygame.image.load(image_wall).convert()
    pion_gyver = pygame.image.load(pion_gyver).convert()

    window.blit(background, (0, 0))
    window.blit(pion_gyver, (60, 0))
    pygame.display.update()

    # Start the game
    playing = 1
    game = gp.Gameplay(my_config, world, gyver, playing)

    while playing:
        # Tant qu'on ne travaille pas avec les événements, appeller cette
        # fonction pour permettre à pygame de les gérer en interne.
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gp.playing = gp._after_death(player)
                if event.key == K_UP:
                    gp._move_up(gyver)
                if event.key == K_RIGHT:
                    gp._move_right(gyver)
                if event.key == K_DOWN:
                    gp._move_down(gyver)
                if event.key == K_LEFT:
                    gp._move_left(gyver)

        # Using console to play
        # playing = game.choose_action(gyver)



if __name__ == "__main__":
    main()
