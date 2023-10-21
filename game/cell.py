class Cell:
    def __init__(self, multiplier=None, multiplier_type=None, letter=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = True
        self.value = self.letter if self.letter else ""

    def add_letter(self, letter):
        self.letter = letter
        self.value = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        return self.letter.values * self.multiplier

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '