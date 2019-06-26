import json

import classes.gameplay as gp
import classes.map as map
import classes.player as player

def main():
    # Load the configuration
    with open('setup.json', encoding='utf8') as game_config:
        my_config = json.load(game_config)
        # assert type(my_config) is dict  # convertir en dictionnaire? vu sur developpez.net
    # Initialize the world map
    world = map.World(my_config)
    print(world)  # statistic and details of the world map
    # Give birth to McGyver
    gyver = player.Player(my_config)
    # Start the game
    # disp = disp.Display()
    game = gp.Gameplay(my_config, world, gyver)
    # Start to play
    game.choose_action(gyver)
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "q")
    # game.choose_action(gyver, "q")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "q")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "q")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "a")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "z")
    # game.choose_action(gyver, "s")
    # game.choose_action(gyver, "z")


if __name__ == "__main__":
    main()
