import components.gameplay as gp


def main():
    gaming = 1
    while gaming:
        game = gp.Gameplay()
        gaming = game.start_loop()


if __name__ == "__main__":
    main()
