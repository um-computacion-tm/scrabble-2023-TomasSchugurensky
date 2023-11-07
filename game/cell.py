from game.tile import Tile
class Cell:
    def __init__(self, multiplier=None, multiplier_type=None, letter=None, letter_values=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = True
        self.value = self.letter.letter if self.letter else ""
        self.letter_values = letter_values or {}

    def add_letter(self, tile):
        if isinstance(tile, Tile):
            self.letter = tile
            self.value = tile.letter
        elif isinstance(tile, str) and tile.upper() in self.letter_values:
            value = self.letter_values[tile.upper()]
            self.letter = Tile(tile, value)
            self.value = tile
        else:
            raise ValueError("Invalid input for add_letter")

    def calculate_word_value(self):
        if self.letter:
            tile_value = self.letter.values
            if self.multiplier_type == "word":
                return tile_value * self.multiplier
            elif self.multiplier_type == "letter":
                return tile_value * self.multiplier
            return tile_value
        return 0

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        elif self.multiplier and self.multiplier_type:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        return '   '