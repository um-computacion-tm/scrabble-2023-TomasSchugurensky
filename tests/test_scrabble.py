import unittest
from game.scrabblegame import ScrabbleGame, InvalidWordException
from unittest.mock import patch
from game.tile import Tile

class TestScrabble(unittest.TestCase):
    def setUp(self):
        self.scrabble_game = ScrabbleGame(players_count=3)
    
    def test_scrabble_initialization(self):
        game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(game.board)
        self.assertEqual(len(game.players), 3)
        self.assertIsNotNone(game.bag_tile)
        self.assertEqual(game.current_player_index, 0)
        self.assertEqual(game.turn, 0)
        self.assertEqual(game.current_players, game.players)
        self.assertIsNotNone(game.current_player)
        self.assertEqual(game.skipped_turns, 0)

    def test_current_player(self):
        game = ScrabbleGame(players_count=3)
        current_player = game.get_current_player()
        self.assertIs(current_player, game.players[0])

    def test_next_turn(self):
        game = ScrabbleGame(players_count=3)
        game.current_players = game.players
        game.turn = 0
        game.current_player = game.players[0]
        game.next_turn()
        self.assertEqual(game.turn, 1)
        self.assertIs(game.current_player, game.players[1])

    def test_next_turn_at_game_start(self):
        self.scrabble_game.next_turn()
        self.assertEqual(self.scrabble_game.current_player, self.scrabble_game.players[1])

    def test_next_turn_when_player_is_not_the_first(self):
        self.scrabble_game.current_player = self.scrabble_game.players[0]
        self.scrabble_game.next_turn()
        self.assertEqual(self.scrabble_game.current_player, self.scrabble_game.players[1])

    def test_next_turn_when_player_is_last(self):
        self.scrabble_game.turn = 2  
        self.scrabble_game.next_turn()
        self.assertEqual(self.scrabble_game.current_player, self.scrabble_game.players[0])

    def test_calculate_word_valid(self):
        game = ScrabbleGame(2)
        word = "CASA"
        calculated_score = game.calculate_words_value(word)
        expected_score = 6
        self.assertEqual(calculated_score, expected_score)

    def test_calculate_word_invalid(self):
        word = 'XD'
        with self.assertRaises(InvalidWordException):
            self.scrabble_game.calculate_words_value(word)
  
    def test_calculate_no_word(self):
        word = ""
        valor = 0
        calculated_value = self.scrabble_game.calculate_words_value(word)
        self.assertEqual(calculated_value, valor)

    @patch('game.dictionary.dict_validate_word', return_value=True)
    def test_play_valid(self, mock_dict_validate_word): 
        player = self.scrabble_game.current_player
        for letter, value in [("C", 3), ("A", 1), ("S", 1), ("A", 1)]:
            player.tiles.append(Tile(letter, value))

        initial_score = player.score
        self.scrabble_game.play("CASA", (7, 7), "H")
        final_score = player.score
        expected_score_increase = 6  

    
        self.assertEqual(final_score, initial_score + expected_score_increase, "Score did not increase correctly after playing 'CASA'")

if __name__ == '__main__':
    unittest.main()