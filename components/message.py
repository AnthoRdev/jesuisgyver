class Message:

    def __init__(self):
        pass

    @staticmethod
    def welcome(player):
        return f"Welcome home {player.name}!"

    @staticmethod
    def out_of_range():
        return "A day I hope you will find the right hole, buddy."

    @staticmethod
    def back_to_start():
        return "No, idiot, you can't escape from there by that way."

    @staticmethod
    def you_found(item):
        return f"You found that: {item}."

    @staticmethod
    def whats_in_bag(player):
        if player.bag == set():
            return "You got nothing"
        else:
            return f"You got " + str(player.bag).strip('{}') + "."

    @staticmethod
    def missing_items():
        return "You're not enough prepared to be free. GAME OVER"

    @staticmethod
    def hit_wall():
        return "Stop to hurt your beautiful hairstyle"

    @staticmethod
    def you_win():
        return "Congratulation, you are free!"
