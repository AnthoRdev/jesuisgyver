from random import *

import classes.map as World


class Player:

    def __init__(self, my_config, world):
        self.X_MIN = my_config['MAP']['X_MIN']
        self.X_MAX = my_config['MAP']['X_MAX']
        self.Y_MIN = my_config['MAP']['Y_MIN']
        self.Y_MAX = my_config['MAP']['Y_MAX']
        self.items = []
        self.position = world.start_position
        self.start_position = world.start_position
        self.end_position = world.end_position
        self.items_positions = world.items_positions
        self.paths = world.paths

    def __str__(self):
        return f"You are there: {self.position}, and that's in your bag: {self.items}"

    def _define_action(self, next_position):
        if next_position[0] not in range(self.X_MIN, self.X_MAX):
            print("Out of range. A day I hope you will find the right hole, buddy.")
            self._after_death()
        elif next_position[1] not in range(self.Y_MIN, self.Y_MAX):
            print("Out of range. A day I hope you will find the right hole, buddy.")
            self._after_death()
        elif next_position in self.paths or next_position in self.items_positions:
            self._move_on(next_position)
        elif next_position == self.end_position:
            print("You got", self.items)
            self._move_on(next_position)
        elif next_position == self.start_position:
            print("No, idiot, you can't escape from there by this way. Ah ah ah!!!")
            self._move_on(next_position)
        else:
            print("Stop trying to imitate a ghost, change direction "
                  "or call Chuck Norris")
            self.move()

    def _move_on(self, next_position):
        self.position = next_position
        for coor, item in self.items_positions:
            if coor == next_position:
                self._find_item(self.position)
        if self.position == self.end_position:
            if len(self.items) == 3:  # TODO remplacer 3 par une liste
                self._is_winner()
            else:
                print("You're not enough prepared to affront Chuck.\nFind some "
                      "good items or good ideas, but find something. For now, "
                      "you're dead.\nGAME OVER")
                self._after_death()
        self.move()

    def _move_up(self, position):
        x, y = position
        next_position = x + 1, y
        self._define_action(next_position)

    def _move_down(self, position):
        x, y = position
        next_position = x - 1, y
        self._define_action(next_position)

    def _move_left(self, position):
        x, y = position
        next_position = x, y - 1
        self._define_action(next_position)

    def _move_right(self, position):
        x, y = position
        next_position = x, y + 1
        self._define_action(next_position)

    def _find_item(self, position):
        for coor, item in self.items_positions:
            if coor == position:
                if item == "N":
                    item = "needle"
                elif item == "T":
                    item = "tub"
                elif item == "E":
                    item = "ether"
                self.items.append(item)
                print(f"You found that: {item}.")

    def _is_winner(self):
        print("After discovering that the guard was Chuck Norris. You decide to "
              "prepare with all of your items, an ether based sedative for "
              "horses. You injected that potion in his neck. "
              "Congratulation Mac, you beaten Chuck, enjoy the freedom!")

    def _after_death(self):
        try_again = input("Try again? (y/n)")
        if try_again == "y":
            print("=" * 80)
            self.items = []
            self.position = self.start_position
            self.move()
        elif try_again == "n":
            print("Don't be afraid anymore, come back now!")
            exit()
        else:
            print("You definitly have no chances to win. "
                  "To shutdown, try to unplug your laptop...")
            exit()

    def move(self, direction=None):
        print(self)

        if direction is None:
            direction = input("Where do you wants to go?")

        if direction == "q":
            self._move_up(self.position)
        elif direction == "a":
            self._move_left(self.position)
        elif direction == "s":
            self._move_right(self.position)
        elif direction == "z":
            self._move_down(self.position)
        else:
            print("Are you kidding me? Dare repeat!")
            self.move()
