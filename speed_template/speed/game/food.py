import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food():
    """This makes the word which are the points in the game"""

    def __init__(self):
        """This loads the words."""
        super().__init__()
        self.word_list = self.load_word_list()
        self.word_items = []
        for i in range(5):
            self.load_words()

    def load_word_list(self):
        """Open a file with many words."""
        with open("speed_template/speed/game/words.txt") as word_list:
            word_list = word_list.read()
            word_list = word_list.split()
        return word_list

    def get_word(self):
        """Pick a random word from the words file."""
        return random.choice(self.word_list)

    def get_points(self, index):
        """Calculates the points for the guessed word."""
        return self.word_items[index]._points

    def move_word(self):
        """Moves the word around the screen."""
        for word in self.word_items:

            if word._slower == 0:

                word.move_next()
                word._slower = word._slower_MAX
            else: 
                word._slower -= 1

    def load_words(self, index = ""):
        """Loads the words into a list."""
        self.word_items.append(Actor())
        self.word_items[-1]._velocity = Point(0, 1)
        self.word_items[-1]._slower_MAX = random.randint(5, 30)
        self.word_items[-1]._slower = self.word_items[-1]._slower_MAX
        word = random.choice(self.word_list)
        self.word_items[-1].set_text(word)
        if index == "":
            x = len(self.word_items) * 8
        else:
            
            x = (index + 1) * 8
        y = random.randint(1,5)
        self.word_items[-1]._position = Point(x, y)
        self.word_items[-1]._points = len(self.word_items[-1].get_text())