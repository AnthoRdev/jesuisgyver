class Display:
    def __init__(self):
        pass

    def where_we_going(self):
        return "Where do you wants to go? (directions:w,a,s,z or quit with 'q')"

    def out_of_range(self):
        print("Out of range. A day I hope you will find the right hole, buddy.")

    def back_to_start(self):
        print("No, idiot, you can't escape from there by this way. Ah ah ah!!!")

    def what_in_bag(self, player):
        print("You got", player.bag)

    def missing_items(self):
        print("You're not enough prepared to affront Chuck.\nFind some "
              "good items or good ideas, but find something. For now, "
              "you're dead.\nGAME OVER")

    def hit_wall(self):
        print("Stop trying to imitate a ghost, change direction "
              "or call Chuck Norris")

    def you_win(self):
        print("After discovering that the guard was Chuck Norris. You decide to "
              "prepare with all of your items, an ether based sedative for "
              "horses. You injected that potion in his neck. "
              "Congratulation Mac, you beaten Chuck, enjoy the freedom!")

    def you_loose(self):
        print()

    def ask_retry(self):
        return "Try again? (y/n)"

    def not_retry(self):
        print("Don't be afraid anymore, come back now!")

    def retry(self):
        print("Yeah! I know this game is definitly amazing!")
        print("=" * 80)

    def are_u_sure(self):
        return "Are you sure? type 'yes' if yes"

    def kidding_me(self):
        return "Are you kidding me? Dare repeat!"

    def shutdown(self):
        print("You definitly have no chances to win. "
              "To shutdown, try to unplug your laptop...")