class Tile:
    def __init__(self, letter, values):
        self.letter = letter
        self.values = values 
    
    def calculate_word_value(self):
        total_value = 0
        total_value += self.values
        return total_value
    
    def __repr__(self):
        return f"{self.letter}:{self.value}"