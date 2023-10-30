import unittest
from game.scrabblegame import ScrabbleGame

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble = ScrabbleGame(3)
        self.assertIsNotNone(scrabble.board)
        self.assertEqual(
            len(scrabble.players),
            3,
        )
    
    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[1])

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.turn = 2  
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]
    
if __name__ == '__main__':
    unittest.main()