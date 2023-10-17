class Player:
    def __init__(self, bag_tiles):
        self.tiles = bag_tiles.take(7)
    
    def rellenar(self, bag_tiles):
        tiles_needed = 7 - len(self.tiles)
        if tiles_needed > 0:
            additional_tiles = bag_tiles.take(tiles_needed)
            self.tiles += additional_tiles
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