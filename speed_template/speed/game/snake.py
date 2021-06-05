from game import constants
from game.actor import Actor
from game.point import Point

class Snake:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._buffer = Actor()
        self._buffer.set_text("-Buffer: ")
        self._text = ["-Buffer: ",""]
        self._buffer._position = Point(0, 20)
        # self._prepare_body()
    
    def update_text(self, text):
        """
        """
        if text != "*":

            self._text[1] += text
            self._buffer.set_text(self._text[0]+self._text[1])

    def get_buffer(self):

        return self._buffer

    def check_word(self, word):
        if word == self._text[1]:
            return True
        else:
            return False
    def clear_buffer(self):
        self._text[1] = ""
        self._buffer.set_text(self._text[0])
