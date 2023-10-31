import unittest
from game.scrabblegame import ScrabbleGame, InvalidWordException
from game.tile import Tile

class TestScrabble(unittest.TestCase):
    def setUp(self):
        self.scrabble_game = ScrabbleGame(players_count=3)
    
    def test_scrabble_initialization(self):
        self.assertIsNotNone(self.scrabble_game.board)
        self.assertEqual(len(self.scrabble_game.players), 3)
    
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
        word = 'CASA'
        valor = 6
        calculated_value = self.scrabble_game.calculate_words_value(word)
        self.assertEqual(calculated_value, valor)
    
    def test_calculate_word_invalid(self):
        word = 'XD'
        with self.assertRaises(InvalidWordException):
            self.scrabble_game.calculate_words_value(word)
  
    def test_calculate_no_word(self):
        word = ""
        valor = 0
        calculated_value = self.scrabble_game.calculate_words_value(word)
        self.assertEqual(calculated_value, valor)

    #def test_play_valid(self):
        #word = "CASA"
        #location = (7, 7)
        #orientation = "H"
        #required_letters = [Tile(letter, valor) for letter, valor in [("C", 3), ("A", 1), ("S", 1), ("A", 1)]]

        #has_required_letters = self.scrabble_game.current_player.has_letters(required_letters)
        #if not has_required_letters:
            #self.fail("No tenes las letras")
        #initial_score = self.scrabble_game.current_player.score
        #self.scrabble_game.play(word, location, orientation)
        #final_score = self.scrabble_game.current_player.score
        #self.assertEqual(final_score, initial_score + self.scrabble_game.calculate_words_value(word))
        #No anda, preguntar el miercoles

if __name__ == '__main__':
    unittest.main()