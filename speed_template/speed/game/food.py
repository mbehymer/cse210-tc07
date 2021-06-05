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
        self.wordlist = ["apple", "orange", "banana", "wheat", "watermelon"]
        self._velocity = Point(0, 1)
        self._slower = 10
        self.reset()



    def get_points(self):
        return self._points

    def move_word(self):
        if self._slower == 0:

            self.move_next()
            self._slower = 10
        else: 
            self._slower -= 1

    def reset(self):

        word = random.choice(self.wordlist)
        super().set_text(word)
        x = random.randint(1,constants.MAX_X-1)
        y = random.randint(1,constants.MAX_Y-1)
        self._position = Point(x, y)
        self._points = random.randint(1,5)

food = Food()

print(food.get_text())