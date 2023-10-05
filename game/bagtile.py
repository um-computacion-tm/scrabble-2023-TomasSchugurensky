import random
from game.tile import Tile
class BagTile:
    def __init__(self): 
        self.tiles =[
            Tile('A',1),
            Tile('B',2),
            Tile('C',3),  
            Tile('D',4),
            Tile('E',5), 
            Tile('F',6),
            Tile('G',7),
            Tile('H',8),
            Tile('I',9),
            Tile('J',10),
            Tile('K',11),
            Tile('L',12),
            Tile('M',13),
            Tile('N',14),
            Tile('Ñ',15),
            Tile('O',16),
            Tile('P',17),
            Tile('Q',18),
            Tile('R',19),
            Tile('S',20),
            Tile('T',21),
            Tile('U',22),
            Tile('V',23),
            Tile('W',24),
            Tile('X',25),
            Tile('Y',26),
            Tile('Z',27),
            ]
        
        random.shuffle(self.tiles)

    def take(self, num_tiles):
        tiles_taken = []
        for _ in range(num_tiles):
            if self.tiles:
                tiles_taken.append(self.tiles.pop(0))
            else:
                break  
        return tiles_taken

    def put(self,tiles):
        for tile in tiles:
            self.tiles.append(tile)