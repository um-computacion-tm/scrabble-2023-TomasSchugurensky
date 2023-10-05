class Tile:
    def __init__(self, letter, values):
        self.letter = letter
        self.values = values 
    
    def calculate_word_value(word):
        total_value = 0
        for cell in word:
            for value in cell.letter.values:
                total_value += value
        return total_value