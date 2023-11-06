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

    def calculate_word_value(self):
        if self.letter:
            tile_value = self.letter.values
        if self.multiplier_type == "word":
            return tile_value * self.multiplier
        elif self.multiplier_type == "letter":
            return tile_value * self.multiplier
        return 0

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier and self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '