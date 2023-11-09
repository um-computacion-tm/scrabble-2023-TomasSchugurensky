import unittest
from game.cli import UserInterface  
from game.bagtile import BagTile
from game.player import Player
from game.models import Board
from unittest.mock import patch

class TestCLI(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(
            UserInterface.get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(
            UserInterface.get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        self.assertEqual(
            UserInterface.get_player_count(),
            1,
        )

    @patch('builtins.input', return_value='1')
    def test_exchange_tile(self, input_patched):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Player1")
        player.tiles = bag_tiles.take(7)  # Utiliza el método take para obtener las fichas

        with patch('builtins.input', side_effect=['0']):
            UserInterface.exchange_tile(player, bag_tiles)

        self.assertEqual(len(player.tiles), 7)

    def test_show_score(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Player1")
        player.score = 30

        with patch('builtins.print') as print_patched:
            UserInterface.show_score(player)

        print_patched.assert_called_with(f"Puntuación de {player.name}: {player.score}")
    
    def test_show_board(self):
        board = Board()  
        with patch('builtins.print') as print_patched:
            UserInterface.show_board(board)

    def test_get_inputs(self):
        with patch('builtins.input', side_effect=['WORD', '2,3', 'H']):
            word_input, location, orientation = UserInterface.get_inputs()

        self.assertEqual(word_input, 'WORD')
        self.assertEqual(location, (1, 2))
        self.assertEqual(orientation, 'H')

if __name__ == '__main__':
    unittest.main()