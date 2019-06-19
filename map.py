# import * from pygame
import env
from random import *


class World:
    X_MIN = 0
    X_MAX = env.MAP_WIDTH
    Y_MIN = 0
    Y_MAX = env.MAP_HEIGHT
    X_STEP = 1
    Y_STEP = 1

    def __init__(self, mapfile):
        self.area = World.__initialize_area()
        self.map = World.__create_map(self, self.area, mapfile)

    def show(self):
        print("Map: ", self.map)
        print("Tiles count: ", self.size)
        print("Start to end", self.start_position, "===>", self.end_position)
        print("Available positions: ", self.available_positions)
        print("Needle ===>", self.needle_position)
        print("Tub ===>", self.tub_position)
        print("Ether ===>", self.ether_position)

    @property
    def size(self):
        return (self.X_MAX - self.X_MIN) * (self.Y_MAX - self.Y_MIN)

    @classmethod
    def __initialize_area(cls):
        cls.AREA = []
        for x in range(cls.X_MIN, cls.X_MAX, cls.X_STEP):
            for y in range(cls.Y_MIN, cls.Y_MAX, cls.Y_STEP):
                zone = (x, y)
                cls.AREA.append(zone)
        return cls.AREA  # est-ce vraiment utile?

    def __create_map(self, area, mapfile):
        map = set()
        with open(mapfile, 'r', encoding='utf-8') as mapFile:
            # je scanne les lignes et cree une liste de chaques caracteres pour chaque ligne
            tileList = []
            for line in mapFile:
                tileList.append(list(line.strip()))
            # je parcours chaque ligne en remontant, et je fusionne les coordonnees de AREA avec le caractere de la map
            for y, line in enumerate(reversed(tileList)):
                for x, tile in enumerate(line):
                    if y > 0:
                        x = x + self.X_MAX * y
                    map.add((area[x],tile))
        # Add items on map in random positions
        World.__randomize_items_positions(self, map)
        return map

    def __randomize_items_positions(self, map):
        # Make a list of available positions
        available_positions = []
        for position in map:
            if position[1] == ".":
                available_positions.append(position[0])
        items = ["N", "T", "E"]
        # Remove empty tiles in map will be used for items
        items_positions = sample(available_positions, 3)
        for item_position in items_positions:
            map.remove((item_position, "."))
        # Create list of elements with position and item
        i = 0
        items_positions_list = []
        for item_position in items_positions:
            items_positions_list.append((item_position, items[i]))
            i = i + 1
        items_positions = set(items_positions_list)
        # Update the map with items
        self.map = frozenset(map | items_positions)
        # Define some variables can be used outside of this class
        for position in self.map:
            if position[1] == "I":
                self.start_position = position[0]
            elif position[1] == "O":
                self.end_position = position[0]
            elif position[1] == "N":
                self.needle_position = position[0]
            elif position[1] == "T":
                self.tub_position = position[0]
            elif position[1] == "E":
                self.ether_position = position[0]


def main():
    world = World('mapfile.txt')
    # world.show()
    print("=" * 80)
    print("Map: ", world.map)
    print("Map type: ", type(world.map))
    print("Tiles count: ", world.size)
    print("Start to end", world.start_position, "===>", world.end_position)
    print("Needle ===>", world.needle_position)
    print("Tub ===>", world.tub_position)
    print("Ether ===>", world.ether_position)
    print("=" * 80)

if __name__ == "__main__":
    main()