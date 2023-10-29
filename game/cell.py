from game.tile import Tile
class Cell:
    def __init__(self, multiplier=None, multiplier_type=None, letter=""):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter if letter else None  
        self.active = True
        self.value = self.letter if self.letter else ""

    def add_letter(self, letter):
        if letter:
            if isinstance(letter, Tile):
                self.letter = letter
                self.value = letter
            else:
                self.letter = letter
                self.value = letter
        else:
            self.letter = None
            self.value = ""

    def calculate_word_value(self, word_multiplier=1):
        if self.letter is None:
            return 0
        return self.letter.calculate_word_value(self.multiplier) * word_multiplier

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier and self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '