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

class Board:
    def __init__(self):
        self.grid = [
            [None for _ in range (15)]     
            for _ in range (15)
        ]
    def validate_word ():  
        pass

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
        
    
    def calculate_word_value(self):
        pass



class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.players = []
        self.bag_tile = BagTile()
        for _ in range(players_count):
            self.players.append(Player(self.bag_tile)) 
        self.turn = 0
        self.current_players = self.players
        self.current_player = self.players[0]
    
        
    def playing(self):  
        return True
    
    def next_turn(self):   
        if self.current_players:
            index_player = self.turn
            next_turn = (index_player + 1) % len(self.current_players)  
            next_player = self.current_players[next_turn]
            self.turn = next_turn
            self.current_player = next_player  
            if self.turn == 0:  
                self.current_players = self.players
    
def main():
    try:
        players_count = int(input('Cantidad de jugadores?: '))
        if players_count <= 1 or players_count > 4:
            raise ValueError('Cantidad de jugadores no válida')
        scrabble_game = ScrabbleGame(players_count=players_count)
        print (f'Turno del jugador {scrabble_game.current_player.id}')

        word = input('Ingrese palabra: ')
        position_X = input('Ingrese posición (X): ')
        position_Y = input('Ingrese posición (Y): ')
        location = position_X, position_Y
        orientation = input('Ingrese orientación (V/H): ')
        scrabble_game.validate_word(word, location, orientation)
        scrabble_game.next_turn()

    except ValueError as e:
        print(f'Error: {e}')
        print('Valor inválido')
    except Exception as e:
        print(f'Error: {e}')
        print('Otro error inesperado')
        


