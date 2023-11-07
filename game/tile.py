class Tile:
    def __init__(self, letter, values):
        self.letter = letter
        self.values = values 
    
    def calculate_word_value(self, multiplier=1):
        total_value = self.values * multiplier
        return total_value
    
    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented
        return self.letter == other.letter and self.values == other.values

    def __hash__(self):
        return hash((self.letter, self.values))
    
    def __repr__(self):
        return f"{self.letter}:{self.values}" 