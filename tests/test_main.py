import unittest
from unittest.mock import patch, MagicMock
from game.main import main
from game.cli import UserInterface

class TestMain(unittest.TestCase):
    @patch('builtins.print')
    @patch('game.cli.UserInterface.show_player')
    @patch('game.cli.UserInterface.show_board')
    @patch('game.cli.UserInterface.get_inputs', return_value=('CASA', (1, 3), 'H'))
    @patch('builtins.input', side_effect=['S', 'X'])  
    @patch('game.scrabblegame.ScrabbleGame', autospec=True)
    def test_main(self, mock_scrabble_game, mock_get_inputs, mock_input, mock_show_board, mock_show_player, mock_print):
        game_instance = mock_scrabble_game.return_value
        game_instance.is_playing.side_effect = [True, False]
        main()


if __name__ == '__main__':
    unittest.main()
