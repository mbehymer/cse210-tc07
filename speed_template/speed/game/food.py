import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food(Actor):
    """This makes the food which are the points in the game"""

    def __init__(self):
        """Something goes here...?"""
        super().__init__()
        super().set_text("@")
        self.reset()


    def get_points(self):
        return self._points

    def reset(self):

        x = random.randint(1,constants.MAX_X-1)
        y = random.randint(1,constants.MAX_Y-1)
        self._position = Point(x, y)
        self._points = random.randint(1,5)