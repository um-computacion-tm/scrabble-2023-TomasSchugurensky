from game.cell import Cell
from game.tile import Tile
from game.dictionary import dict_validate_word, InvalidWordException

class InvalidPlaceWordException(Exception):
    pass

class Board:
    def __init__(self):
        self.grid = [[Cell() for _ in range(15)] for _ in range(15)]
        self.is_cell_occupied = [[False] * 15 for _ in range(15)]
        self.set_multiplier('DL', [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)])
        self.set_multiplier('TL', [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)])
        self.set_multiplier('DW', [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)])
        self.set_multiplier('TW', [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)])

    def set_multiplier(self, multiplier_type, coordinates):
        for x, y in coordinates:
            x, y = x - 1, y - 1
            if 0 <= x < 15 and 0 <= y < 15:
                self.grid[x][y].multiplier = self.multiplier_value(multiplier_type)
                self.grid[x][y].multiplier_type = multiplier_type
    
    def multiplier_value(self, multiplier_type):
        return {
            'DL': 2,
            'TL': 3,
            'DW': 2,  
            'TW': 3,  
        }.get(multiplier_type, 1)
    
    def string_to_tiles(self, word):
        letter_values = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
            'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1,
            'P': 3, 'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 8,
            'X': 8, 'Y': 4, 'Z': 10, 'CH': 5, 'LL': 8, 'RR': 8, '': 0
        }
        return [Tile(letter.upper(), letter_values[letter.upper()]) for letter in word]
    
    def get_cells(self, location, orientation, length):
        cells = []
        x, y = location
        for i in range(length):
            if orientation == 'H':
                cells.append(self.grid[x][y + i])
            else:  
                cells.append(self.grid[x + i][y])
        return cells
    
    @staticmethod
    def calculate_word_value(cells):
        word_multiplier = 1
        word_value = 0
        for cell in cells:
            if cell.letter:  
                letter_multiplier = cell.multiplier if cell.multiplier_type == 'letter' else 1
                word_value += cell.letter.values * letter_multiplier  
                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier
        return word_value * word_multiplier
    
    def put_words(self, tiles, location, orientation):
        word = ''.join(tile.letter for tile in tiles)
        if not self.validate_word(word, location, orientation):
            return False
        x, y = location
        word_len = len(tiles)

        if orientation == "H":
            for i in range(word_len):
                if self.is_cell_occupied[x][y + i]:
                    return False
                self.grid[x][y + i].add_letter(tiles[i])
                self.is_cell_occupied[x][y + i] = True
        elif orientation == "V":
            for i in range(word_len):
                if self.is_cell_occupied[x + i][y]:
                    return False
                self.grid[x + i][y].add_letter(tiles[i])
                self.is_cell_occupied[x + i][y] = True

        return True
    
    def validate_word(self, word, location, orientation):
        if not dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
        return True

    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        if orientation == "H":
            return x >= 0 and y >= 0 and x < 15 and (y + word_length) <= 15
        elif orientation == "V":
            return y >= 0 and x >= 0 and y < 15 and (x + word_length) <= 15
        return False
    
    @property
    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.value != "":
                    return False
        return True
    
    def validate_word_place_board(self, word, location, orientation):
        x, y = location
        word_len = len(word)
   
        if orientation == "H":
            if y + word_len > 15: 
                return False
            for i in range(word_len):
                if self.grid[x][y + i].value:  
                    return False
    
        elif orientation == "V":
            if x + word_len > 15:  
                return False
            for i in range(word_len):
                if self.grid[x + i][y].value:  
                    return False
        return True