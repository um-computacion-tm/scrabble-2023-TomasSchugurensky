class Tile:
    def __init__(self, letter, values):
        self.letter = letter
        self.values = values 
    
    def calculate_word_value(self, multiplier=1):
        total_value = self.values * multiplier
        return total_value
    
    def __repr__(self):
        return f"{self.letter}:{self.values}"