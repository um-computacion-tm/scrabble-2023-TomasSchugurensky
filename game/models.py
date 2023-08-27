import random
class Tile:
    def __init__(self, letter, values):
        self.letter = letter
        self.values = values 

class BagTile:
    def __init__(self): 
        self.tiles =[
            Tile('A',1),
            Tile('B',2),
            Tile('C',3),  
            Tile('D',4),
            Tile('E',5), 
            ]
        
        random.shuffle(self.tiles)
    def take(self, count):
        tiles = []
        for _ in range (count):
            tiles.append(self.tiles.pop(0))
        return tiles
    
    def put(self,tiles):
        for tile in tiles:
            self.tiles.append(tile)

class Player:
    def __init__(self):
        self.tiles = []

class Board:
    def __init__(self):
        self.grid = [
            [None for _ in range (15)]     
            for _ in range (15)
        ]

class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter):
        self.letter = letter   

    def calculate_value(self):
        if self.letter is None:
            return 0
        return self.letter.values * self.multiplier

