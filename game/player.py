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
    

    def remove_tiles(self, tiles_to_remove):
        self.tiles = [tile for tile in self.tiles if tile not in tiles_to_remove]

    def refill_tiles(self, bag_tiles):
        while len(self.tiles) < 7:
            new_tiles = bag_tiles.take(1)  
            if new_tiles:  
                self.tiles.extend(new_tiles)  
            else:
                break
        
    def has_letters(self, required_letters):
        player_tiles = [tile.letter for tile in self.tiles]
        return all(letter in player_tiles for letter in required_letters)
    
    def exchange_tile(self, bag_tiles, tile):
        self.tiles.remove(tile)
        bag_tiles.put(tile)  
        new_tiles = bag_tiles.take(1)
        self.tiles.extend(new_tiles)
    
    def exchange(self, tiles_to_exchange, bag_tiles):
        if not all(tile in self.tiles for tile in tiles_to_exchange):
            return False  

        for tile in tiles_to_exchange:
            self.tiles.remove(tile)

        bag_tiles.put(tiles_to_exchange)
        new_tiles = bag_tiles.take(len(tiles_to_exchange))
        self.tiles.extend(new_tiles)

        if len(self.tiles) != 7:
            additional_tiles_needed = 7 - len(self.tiles)
            self.tiles.extend(bag_tiles.take(additional_tiles_needed))

        return True

    def show_player(self):
        print(f"Nombre del jugador: {self.name}")
        print("Fichas del jugador:", ", ".join([tile.letter for tile in self.tiles]))

bag_tiles = BagTile()
player = Player(bag_tiles, "nombre")