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

    def calculate_word_value(self, cells):
        word_multiplier = 1
        word_value = 0
        for cell in cells:
            if cell.multiplier_type == 'letter':
                word_value += cell.letter.value * cell.multiplier
            else:
                word_value += cell.letter.value
            if cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier
        return word_value * word_multiplier
    
    def get_word_cells(self, word, location, orientation):
        x, y = location
        cells = []
        if orientation.upper() == 'H':  
            for i in range(len(word)):
                cells.append(self.grid[x][y + i])
        elif orientation.upper() == 'V':  
            for i in range(len(word)):
                cells.append(self.grid[x + i][y])
        return cells

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        elif self.multiplier and self.multiplier_type:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        return '   '