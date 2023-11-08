import unittest
from game.scrabblegame import ScrabbleGame, InvalidPlaceWordException
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

    def test_skip_turn(self):
        initial_turns_skipped = self.scrabble_game.skipped_turns
        self.scrabble_game.skip_turn()
        final_turns_skipped = self.scrabble_game.skipped_turns
        self.assertEqual(final_turns_skipped, initial_turns_skipped + 1, "Turnos salteados aumenta en 1")

    def test_calculate_words_value(self):
        game = ScrabbleGame(1)  
        self.assertEqual(game.calculate_words_value('CASA'), 6, "El valor calculado para 'CASA' deberia ser 6")

    def test_calculate_word_invalid(self):
        word = 'XD'  
        calculated_value = self.scrabble_game.calculate_words_value(word)
        self.assertEqual(calculated_value, 0, "Palabras invalidas no tienen puntuacion")
  
    def test_calculate_no_word(self):
        word = ""
        valor = 0
        calculated_value = self.scrabble_game.calculate_words_value(word)
        self.assertEqual(calculated_value, valor)

    @patch('game.dictionary.dict_validate_word', return_value=True)
    def test_play_valid(self, mock_dict_validate_word):
        game = ScrabbleGame(1)
        initial_score = game.get_current_player().score

        game.get_current_player().tiles = [Tile('C', 3), Tile('A', 1), Tile('S', 1), Tile('A', 1)]

        location = (7, 7)  
        orientation = 'H'  

        game.play('CASA', location, orientation)

        expected_score_increase = game.calculate_words_value('CASA')
        final_score = game.get_current_player().score

        self.assertEqual(final_score, initial_score + expected_score_increase, "Puntaje no aumento correctamente con la palabra 'CASA'")

    def test_play_invalid_word(self):
        game = ScrabbleGame(1)
        initial_score = game.get_current_player().score

        game.get_current_player().tiles = [Tile('X', 8), Tile('D', 2)]

        location = (7, 7)
        orientation = 'H'

        game.play('XD', location, orientation)

        final_score = game.get_current_player().score

        self.assertEqual(final_score, initial_score, "Puntaje no aumenta con palabra invalida")

    def test_validate_word_exceeds_board(self):
        word = 'CASA'
        location = (14, 7)  
        orientation = 'H'

        with patch('game.dictionary.dict_validate_word', return_value=True):
            with self.assertRaises(InvalidPlaceWordException):
                self.scrabble_game.validate_word(word, location, orientation)

    def test_validate_word_bad_placed(self):
        word = 'CASA'
        location = (7, 7)
        orientation = 'V'  

        with patch('game.dictionary.dict_validate_word', return_value=True):
            with self.assertRaises(InvalidPlaceWordException):
                self.scrabble_game.validate_word(word, location, orientation)

    def test_validate_not_enough_letters(self):
        word = 'CASA'
        location = (7, 7)
        orientation = 'H'
        self.scrabble_game.current_player.tiles = [Tile('X', 8), Tile('D', 2)]

        with patch('game.dictionary.dict_validate_word', return_value=True):
            with self.assertRaises(InvalidPlaceWordException):
                self.scrabble_game.validate_word(word, location, orientation)
    
if __name__ == '__main__':
    unittest.main()