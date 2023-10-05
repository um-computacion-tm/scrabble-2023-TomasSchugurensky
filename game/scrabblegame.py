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