from game.bagtile import BagTile
from game.tile import Tile

class Player:
    def __init__(self, bag_tiles):
        self.tiles = bag_tiles.take(7)    
    
    def rellenar(self, bag_tiles):
        tiles_needed = 7 - len(self.tiles)
        if tiles_needed > 0:
            additional_tiles = bag_tiles.take(tiles_needed)
            for tile in additional_tiles:
                if isinstance(tile, Tile):
                    self.tiles.append(tile)
            return len(additional_tiles)
        else:
            return 0
        
    def has_letters(self, tiles):
        player_tiles = [tile.letter for tile in self.tiles]
        for tile in tiles:
            if tile.letter not in player_tiles:
                return False
        return True
    
def show_player(self):
        print(f"Nombre del jugador: {self.name}")
        print("Fichas del jugador:", ", ".join([tile.letter for tile in self.tiles]))

bag_tiles = BagTile()
player = Player(bag_tiles)

def get_inputs(self):
    word_input = input("Ingrese palabra: ").strip()
    location_input = input("Ingrese la ubicación (fila, columna): ").strip()
    orientation_input = input("Ingrese la orientación (horizontal o vertical): ").strip()

    return word_input, location_input, orientation_input

