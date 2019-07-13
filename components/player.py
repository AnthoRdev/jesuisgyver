class Player:

    def __init__(self, game_config):
        self.position = ()
        self.bag = set()
        self.items = game_config['ITEMS']  # Get the dict of items
        self.name = game_config['PLAYER']['NAME']

    def move_on(self, next_position):
        """change the actual position of the player"""
        self.position = next_position

    def get_item(self, item):
        """add founded item in player bag"""
        item_name = self.items[item]['NAME']
        self.bag.add(item_name)
        return item_name
