from random import *


class World:

    def __init__(self, game_config):
        self.items = game_config['ITEMS']
        self.worldmap = World._create_map(self, game_config['MAP']['FILE'])
        # Define some variables can be used outside of this class
        for position in self.worldmap:
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
        self.game_config = game_config['MAP']

    def _create_map(self, mapfile):
        """Make a set of positions associated with their content"""
        worldmap = {}
        with open(mapfile, 'r', encoding='utf-8') as mapFile:
            line_list = []
            for line in mapFile:
                line_list.append(list(line.strip()))
            for y, line in enumerate(line_list):
                for x, tile in enumerate(line):
                    worldmap[(x, y)] = tile
        # Add items on map in random positions
        worldmap = self._randomize_items_positions(worldmap)
        return worldmap

    def _randomize_items_positions(self, worldmap):
        # Make a list of available positions
        available_positions = []
        for position in worldmap.items():
            if position[1] == ".":
                available_positions.append(position[0])
        # Make a list of randomized positions
        randomized_positions = sample(available_positions, len(self.items))
        # Make a dict of randomized positions of items
        items_positions_list = dict(zip(randomized_positions, self.items))
        # Update the worlmap dict
        worldmap.update(items_positions_list)
        # convert wordmap to set with a comprehension loop
        worldmap = {(position, value) for position, value in worldmap.items()}
        return worldmap

    def change_tile(self, next_tile):
        """Replace the tile by a path. Used to replace an item tile after taken it."""
        old_position = next_tile[0][0], next_tile[0][1]
        self.worldmap.remove(old_position)
        new_position = tuple([next_tile[0][0], "."])
        self.worldmap.add(new_position)

    def coor_convert(self, x, y):
        """Convert position coordonates to pixel positions on screen for Pygame
        and add margins around the map"""
        (x, y) = x * self.game_config['TILE_WIDTH'] + self.game_config['MARGIN'], \
                 y * self.game_config['TILE_HEIGHT'] + self.game_config['MARGIN']
        return x, y
