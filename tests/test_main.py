import unittest
from unittest.mock import patch
from game.main import main
from game.cli import show_player, get_player_count, show_board

class TestMain(unittest.TestCase):
    @patch('builtins.print')
    @patch('game.player.show_player')
    @patch('game.models.show_board')
    @patch('game.player.get_inputs', return_value=(1, 3, 'H', 'CASA'))
    @patch('builtins.input', side_effect=['S'])
    @patch('game.scrabblegame.ScrabbleGame', autospec=True)
    def test_main(self, mock_scrabble_game, mock_get_inputs, mock_input, mock_show_board, mock_show_player, mock_print):
        game_instance = mock_scrabble_game.return_value
        game_instance.is_playing.side_effect = [True, False]
    main()

if __name__ == '__main__':
    unittest.main()
