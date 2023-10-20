from game.player import Player
from game.bagtile import BagTile
from game.models import Board


class InvalidWordException(Exception):
    pass

class InvalidPlaceWordException(Exception):
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

    def calculate_words_value(self, word):
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


    def get_words_input(self):
        word_input = input("Ingrese la palabra que desea jugar: ").strip()
        location_input = input("Ingrese la ubicación de la palabra (fila, columna): ").strip()
        orientation_input = input("Ingrese la orientación (horizontal o vertical): ").strip()

        return word_input, location_input, orientation_input

    
    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation, self.get_current_player())
        total = calculate_words_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def validate_word(self, word, location, orientation):
        if not dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
        
    if not self.get_current_player().has_letters(missingletters)