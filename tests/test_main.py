import unittest
from unittest.mock import patch
from game.main import main

class TestMain(unittest.TestCase):
    @patch('builtins.print')
    @patch('game.cli.UserInterface.show_player')
    @patch('game.cli.UserInterface.show_board')
    @patch('game.cli.UserInterface.get_player_count', return_value=1)
    @patch('game.cli.UserInterface.get_inputs', return_value=('CASA', (1, 3), 'H'))
    @patch('game.scrabblegame.ScrabbleGame', autospec=True)
    @patch('builtins.input', side_effect=['P', 'I', 'S', 'E'])
    def test_main(self, mock_input, mock_scrabble_game, mock_get_inputs, mock_get_player_count, 
                  mock_show_board, mock_show_player, mock_print):
        main()

        

if __name__ == '__main__':
    unittest.main()