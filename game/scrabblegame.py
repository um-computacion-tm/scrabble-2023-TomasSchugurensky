from game.player import Player
from game.bagtile import BagTile
from game.models import Board, InvalidPlaceWordException
from game.tile import Tile
from game.dictionary import dict_validate_word, DictionaryConnectionError

class InvalidWordException(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.players = []
        self.bag_tile = BagTile()
        self.current_player_index = 0  
        for _ in range(players_count):
            self.players.append(Player(self.bag_tile, "nombre"))
        self.turn = 0
        self.current_players = self.players
        self.current_player = self.players[0]
        self.skipped_turns = 0 

    def string_to_tiles(self, word):
        letter_values = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
            'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3,
            'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8,
            'Y': 4, 'Z': 10, 'CH': 5, 'LL': 8, 'RR': 8, '': 0 
        }
        return [Tile(letter.upper(), letter_values[letter.upper()]) for letter in word]
        

    def is_playing(self):
        return True
    
    def get_board(self):
        return self.board
    
    def get_current_player(self):
        return self.players[self.current_player_index]
          
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]   
        if self.current_players:
            index_player = self.turn
            next_turn = (index_player + 1) % len(self.current_players)  
            next_player = self.current_players[next_turn]
            self.turn = next_turn
            self.current_player = next_player  
            if self.turn == 0:  
                self.current_players = self.players
    
    def skip_turn(self):
        self.skipped_turns += 1
        self.next_turn()  
        print(f"Turno saltado. Llevas {self.skipped_turns} turnos saltados.")

    def calculate_words_value(self, word):
        try:
            if not dict_validate_word(word):
                return 0
        except DictionaryConnectionError:
            pass

        letter_values = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
            'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3,
            'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8,
            'Y': 4, 'Z': 10, 'CH': 5, 'LL': 8, 'RR': 8, '': 0 
        }
        word = word.upper()
        total_value = 0

        for letter in word:
            if letter in letter_values:
                total_value += letter_values[letter]
            else:
                total_value += 0
        return total_value


    def play(self, word, location, orientation):
        try:
            if not dict_validate_word(word):
                print(f"La palabra '{word}' no existe en el diccionario")
                return False  

            tiles = self.string_to_tiles(word)
            print(f"Fichas para palabra '{word}': {[tile.letter for tile in tiles]}")

            if self.board.put_words(tiles, location, orientation):
                cells = self.board.get_cells(location, orientation, len(word))
                score_for_word = self.board.calculate_word_value(cells)
                self.players[self.current_player_index].score += score_for_word
                self.players[self.current_player_index].remove_tiles(tiles)
                self.players[self.current_player_index].refill_tiles(self.bag_tile)
                print(f"Palabra '{word}' puesta correctamente. Puntaje para esta palabra: {score_for_word}")
                print(f"Puntaje total para {self.players[self.current_player_index].name}: {self.players[self.current_player_index].score}")
                return True  
            else:
                print("La palabra no pudo ser colocada en el tablero.")
                return False  
        except InvalidPlaceWordException as e:
            print(e)  
            return False

    def validate_word(self, word, location, orientation):
        required_letters = list(word)
        if not dict_validate_word(word):
            raise InvalidWordException("Palabra no existe")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Palabra mal puesta")
        if not self.current_player.has_letters(required_letters):
            raise InvalidPlaceWordException("No tenes las letras requeridas")