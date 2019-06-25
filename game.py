import json

import classes.map as World
import classes.player as Player

def main():
    # Load the configuration
    with open('setup.json', encoding='utf8') as game_config:
        my_config = json.load(game_config)
        # assert type(my_config) is dict  # convertir en dictionnaire
    # Initialize the world map
    world = World.World(my_config, './ressources/mapfile.txt')  # TODO Comprendre pourquoi je dois doubler l'appel
    print(world)  # statistic and details of the world map
    # Give birth to Gyver
    gyver = Player.Player(my_config, world)
    # Start the game
    gyver.move()
    # gyver.move("z")
    # gyver.move("a")
    # gyver.move("a")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("q")
    # gyver.move("q")
    # gyver.move("s")
    # gyver.move("q")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("q")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("a")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("s")
    # gyver.move("s")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("a")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("s")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("a")
    # gyver.move("a")
    # gyver.move("a")
    # gyver.move("a")
    # gyver.move("z")
    # gyver.move("z")
    # gyver.move("s")
    # gyver.move("z")


if __name__ == "__main__":
    main()
