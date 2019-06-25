from random import *


class World:

    def __init__(self, my_config, mapfile):
        self.X_MIN = my_config['MAP']['X_MIN']
        self.X_MAX = my_config['MAP']['X_MAX']
        self.Y_MIN = my_config['MAP']['Y_MIN']
        self.Y_MAX = my_config['MAP']['Y_MAX']
        self.X_STEP = my_config['MAP']['X_STEP']
        self.Y_STEP = my_config['MAP']['Y_STEP']

        self.area = self._initialize_area()
        self.worldmap = World._create_map(self, self.area, mapfile)

    def __str__(self):
        return (f"{'=' * 80}\n"
                f"Map: {self.worldmap}\n"
                f"Map type: {type(self.worldmap)}\n"
                f"Tiles count: {self.size}\n"
                f"Start to end {self.start_position} ===> {self.end_position}\n"
                f"Needle ===>{self.needle_position}\n"
                f"Tub ===> {self.tub_position}\n"
                f"Ether ===> {self.ether_position}\n"
                f"{'=' * 80}")

    @property
    def size(self):
        return (self.X_MAX - self.X_MIN) * (self.Y_MAX - self.Y_MIN)

    def _initialize_area(self):
        area = []
        for x in range(self.X_MIN, self.X_MAX, self.X_STEP):
            for y in range(self.Y_MIN, self.Y_MAX, self.Y_STEP):
                zone = (x, y)
                area.append(zone)
        return area  # TODO est-ce vraiment utile?

    def _create_map(self, area, mapfile):
        worldmap = set()
        with open(mapfile, 'r', encoding='utf-8') as mapFile:
            # je scanne les lignes et cree une liste de chaques caracteres pour chaque ligne
            tile_list = []
            for line in mapFile:
                tile_list.append(list(line.strip()))
            # je parcours chaque ligne en remontant, et je fusionne les coordonnees de AREA avec le caractere de la map
            for y, line in enumerate(reversed(tile_list)):
                for x, tile in enumerate(line):
                    if y > 0:
                        x = x + (self.X_MAX * y)
                    worldmap.add((area[x], tile))
        # Add items on map in random positions
        World._randomize_items_positions(self, worldmap)
        return worldmap

    def _randomize_items_positions(self, worldmap):
        # Make a list of available positions
        available_positions = []
        for position in worldmap:
            if position[1] == ".":
                available_positions.append(position[0])
        items = ["N", "T", "E"]
        items_positions = sample(available_positions, 3)
        # Remove empty tiles in map will be used for items
        for item_position in items_positions:
            worldmap.remove((item_position, "."))
        # Create list of elements with position and item
        items_positions_list = []
        for i, item_position in enumerate(items_positions):
            items_positions_list.append((item_position, items[i]))
        self.items_positions = set(items_positions_list)
        # Update the map with items
        self.worldmap = frozenset(worldmap | self.items_positions)
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
        # Define these next variable for use in other class
        self.paths = available_positions
