class Cell:
    def __init__(self, multiplier=None, multiplier_type=None, letter=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = True
        
    def add_letter(self, letter):
        self.letter = letter   

    def calculate_value(self):
        if self.letter is None:
            return 0
        return self.letter.values * self.multiplier