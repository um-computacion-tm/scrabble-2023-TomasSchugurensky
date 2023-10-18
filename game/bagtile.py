import random
from game.tile import Tile

class BagTile:
    def __init__(self): 
        self.tiles =[
            Tile('A',1), Tile('A',1), Tile('A',1), Tile('A',1), Tile('A',1), Tile('A',1), 
            Tile('A',1), Tile('A',1), Tile('A',1), Tile('A',1), Tile('A',1), Tile('A',1),

            Tile('B',5), Tile('B',5),

            Tile('C',3), Tile('C',3), Tile('C',3), Tile('C',3),  

            Tile('D',2), Tile('D',2), Tile('D',2), Tile('D',2), Tile('D',2),

            Tile('E',1), Tile('E',1), Tile('E',1), Tile('E',1), Tile('E',1), Tile('E',1),
            Tile('E',1), Tile('E',1), Tile('E',1), Tile('E',1), Tile('E',1), Tile('E',1),

            Tile('F',4),

            Tile('G',2), Tile('G',2),

            Tile('H',4), Tile('H',4),

            Tile('I',1), Tile('I',1), Tile('I',1), Tile('I',1),Tile('I',1), Tile('I',1),

            Tile('J',8),

            Tile('K',8),

            Tile('L',1), Tile('L',1), Tile('L',1), Tile('L',1),

            Tile('M',3), Tile('M',3),

            Tile('N',1), Tile('N',1), Tile('N',1), Tile('N',1), Tile('N',1),

            Tile('Ñ',8),

            Tile('O',1), Tile('O',1), Tile('O',1), Tile('O',1), Tile('O',1), Tile('O',1), 
            Tile('O',1), Tile('O',1), Tile('O',1),

            Tile('P',3), Tile('P',3),

            Tile('Q',5),

            Tile('R',1), Tile('R',1), Tile('R',1), Tile('R',1), Tile('R',1),

            Tile('S',1), Tile('S',1), Tile('S',1), Tile('S',1), Tile('S',1), Tile('S',1),

            Tile('T',1), Tile('T',1), Tile('T',1), Tile('T',1),

            Tile('U',1), Tile('U',1), Tile('U',1), Tile('U',1), Tile('U',1),

            Tile('V',4),

            Tile('W',8),

            Tile('X',8),

            Tile('Y',4),

            Tile('Z',10),

            #Letras especiales

            Tile('CH',5),

            Tile('LL',8),

            Tile('RR',8),

            Tile('',0),

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