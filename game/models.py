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
