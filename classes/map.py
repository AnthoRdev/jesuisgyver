from random import *


class World:

    def __init__(self, my_config):
        self.ITEMS = list(my_config['ITEMS'])
        self.worldmap = World._create_map(self, my_config['MAP']['FILE'])

    def __str__(self):
        return (f"{'=' * 80}\n"
                f"Map: {self.worldmap}\n"
                f"Tiles count: {self.size}\n"
                f"Start to End: {self.start_position} ===> {self.end_position}\n"
                f"Needle => {self.needle_position} // "
                f"Tub => {self.tub_position} // "
                f"Ether => {self.ether_position} // "
                f"Toy => {self.toy_position}\n"
                f"{'=' * 80}")

    @property
    def size(self):
        return len(self.worldmap)

    def _create_map(self, mapfile):
        worldmap = {}
        with open(mapfile, 'r', encoding='utf-8') as mapFile:
            # je scanne les lignes et cree une liste de chaques caracteres pour chaque ligne
            line_list = []
            for line in mapFile:
                line_list.append(list(line.strip()))
            # je parcours chaque ligne en remontant, et je fusionne les coordonnees de AREA avec le caractere de la map
            for y, line in enumerate(reversed(line_list)):
                for x, tile in enumerate(line):
                    worldmap[(x, y)] = tile
        # Add items on map in random positions
        worldmap = World._randomize_items_positions(self, worldmap)
        return worldmap

    def _randomize_items_positions(self, worldmap):
        # Make a list of available positions
        available_positions = []
        for position in worldmap.items():
            if position[1] == ".":
                available_positions.append(position[0])
        # Make a list of randomized positions
        len_items = len(self.ITEMS)
        randomized_positions = sample(available_positions, len_items)
        # Make a dict of randomized positions of items
        items_positions_list = dict(zip(randomized_positions, self.ITEMS))
        # Update the worlmap dict
        worldmap.update(items_positions_list)
        # convert wordmap to set with a comprehension loop
        worldmap = {(position, value) for position, value in worldmap.items()}
        # Define some variables can be used outside of this class
        for position in worldmap:
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
            elif position[1] == "J":
                self.toy_position = position[0]
        return worldmap

    def change_tile(self, next_tile):
        old_position = next_tile[0][0], next_tile[0][1]
        self.worldmap.remove(old_position)
        new_position = tuple([next_tile[0][0], "."])
        self.worldmap.add(new_position)
