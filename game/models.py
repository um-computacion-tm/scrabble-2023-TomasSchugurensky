from game.cell import Cell
from game.dictionary import dict_validate_word, InvalidWordException

class InvalidPlaceWordException(Exception):
    pass

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
        self.is_cell_occupied = [[False] * 15 for _ in range(15)]
        self.set_multiplier('DL', [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)])
        self.set_multiplier('TL', [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)])
        self.set_multiplier('DW', [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)])
        self.set_multiplier('TW', [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)])
    
    def set_multiplier(self, multiplier, coordinates):
        for x, y in coordinates:
            self.grid[x - 1][y - 1] = multiplier

    @staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value
    
    def put_words(self, word, location, orientation):
        if not self.validate_word(word, location, orientation):
            return False
        x, y = location
        word_len = len(word)

        if orientation == "H":
            for i in range(word_len):
                if self.is_cell_occupied[x][y + i]:
                    return False
                self.grid[x][y + i].add_letter(word[i])
                self.is_cell_occupied[x][y + i] = True
        if orientation == "V":
            for i in range(word_len):
                if self.is_cell_occupied[x + i][y]:
                    return False
                self.grid[x + i][y].add_letter(word[i])
                self.is_cell_occupied[x + i][y] = True
        return True
    
    def validate_word(self, word, location, orientation):
        if not dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")

    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        if orientation == "H": 
            if x < 0 or x >= 15 or y < 0 or (y + word_length > 15 and not self.is_empty):
                return False
        elif orientation == "V": 
            if x < 0 or (x + word_length > 15 and not self.is_empty) or y < 0 or y >= 15:
                return False
        else:
            return False
        return True
    
    @property
    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.value != "":
                    return False 
        return True
    
    def validate_word_place_board(self, word, location, orientation):
        if not self.validate_word_inside_board(word, location, orientation):
            return False
        x, y = location
        word_len = len(word)

        if orientation == "H":
            for i in range(word_len):
                if x < 0 or x >= 15 or y + i < 0 or y + i >= 15 or self.grid[x][y + i].value != "":
                    return False
        if orientation == "V":
            for i in range(word_len):
                if x + i < 0 or x + i >= 15 or y < 0 or y >= 15 or self.grid[x + i][y].value != "":
                    return False
        return True

def show_board(self):
    print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
    for row_index, row in enumerate(self.grid):
        print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([cell.value if cell.value else "   " for cell in row])
        )