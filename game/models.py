from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]

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
                self.grid[x][y + i] = word[i]
        if orientation == "V":
            for i in range(word_len):
                self.grid[x + i][y] = word[i]
        return True
    
    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        if orientation == "H": 
            if x < 0 or x >= 15 or y < 0 or y + word_length > 15:
                return False
        elif orientation == "V": 
            if x < 0 or x + word_length > 15 or y < 0 or y >= 15:
                return False
        else:
            return False
        return True
    
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
    
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([repr(cell) for cell in row])
        )