class Player:

    def __init__(self, my_config):
        self.position = ()
        self.items = my_config['ITEMS']
        self.bag = set()

    def __str__(self):
        # TODO Faut-il passer ca dans la classe display? je pense que oui.
        # TODO Ameliorer l'affichage de self.bag.
        return f"You are there: {self.position}, and that's in your bag: {self.bag}"

    def move_on(self, next_position):
        """change the actual position of the player"""
        self.position = next_position

    def get_item(self, item):
        """add founded item in player bag"""
        item_name = self.items[item]['NAME']
        self.bag.add(item_name)
        print(f"You found that: {item_name}.")
