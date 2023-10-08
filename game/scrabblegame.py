from game.player import Player
from game.bagtile import BagTile
from game.models import Board


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
    
    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
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