from game import constants
from game.actor import Actor
from game.point import Point

class Snake:
    """Updates the text and the buffer.

    Stereotype:
        Structurer, Information Holder
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
        Updates the text.
        """
        if text != "*":

            self._text[1] += text
            self._buffer.set_text(self._text[0]+self._text[1])

    def get_buffer(self):
        """Returns whatever you typed."""
        return self._buffer

    def check_word(self, word):
        """Check if the word you typed is on the screen."""
        if word == self._text[1]:
            return True
        else:
            return False
    def clear_buffer(self):
        """Resets the buffer."""
        self._text[1] = ""
        self._buffer.set_text(self._text[0])
