from game.bagtile import BagTile
from game.tile import Tile

class Player:
    def __init__(self, bag_tiles, name):
        self.tiles = bag_tiles.take(7)  
        self.score = 0 
        self.name = name
        

    def rellenar(self, bag_tiles):
        tiles_needed = 7 - len(self.tiles)
        if tiles_needed > 0:
            additional_tiles = bag_tiles.take(tiles_needed)
            for tile in additional_tiles:
                if isinstance(tile, Tile):
                    self.tiles.append(tile)
            print(f"Fichas adicionales: {additional_tiles}")
            return len(additional_tiles)
        else:
            return 0
        
    def has_letters(self, tiles):
        player_tiles = [tile.letter for tile in self.tiles]
        for tile in tiles:
            if tile in player_tiles:
                return False
        return True
    
    def exchange(self, tiles_to_exchange, bag_tiles):
        tiles_to_exchange_copy = list(tiles_to_exchange)
        player_tiles_copy = list(self.tiles)
        for tile in tiles_to_exchange_copy:
            if tile in player_tiles_copy:
                tiles_to_exchange_copy.remove(tile)
                player_tiles_copy.remove(tile)
            else:
                return False
            
        bag_tiles.put(tiles_to_exchange)
        num_new_tiles = 7 - len(self.tiles)
        new_tiles = bag_tiles.take(num_new_tiles)
        self.tiles.extend(new_tiles)

        return True


def show_player(self):
    print(f"Nombre del jugador: {self.name}")
    print("Fichas del jugador:", ", ".join([tile.letter for tile in self.tiles]))

bag_tiles = BagTile()
player = Player(bag_tiles, "nombre")
