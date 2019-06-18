# import * from pygame
import env


class World:
    AREA = []
    X_MIN = 0
    X_MAX = env.width
    Y_MIN = 0
    Y_MAX = env.height
    X_STEP = 1
    Y_STEP = 1

    def __init__(self):
        area = [ i for i in self.X_MAX - self.X_MIN ]

    def show(self):
        print("Tiles count: ", self.size)

    @property
    def size(self):
        return (self.X_MAX - self.X_MIN) * (self.Y_MAX - self.Y_MIN)

    @classmethod
    def _initialize_zones(cls):
        cls.AREA = []
        for x in range(cls.X_MIN, cls.X_MAX, cls.X.STEP):
            for y in range(cls.Y_MIN, cls.Y_MAX, cls.Y_STEP):
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.AREA.append(zone)


def main():
    world = World()
    world.show()



if __name__ == "__main__":
    main()