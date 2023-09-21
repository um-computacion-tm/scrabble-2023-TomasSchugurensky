import unittest
from unittest.mock import patch
from game.models import Tile, BagTile, Player, Board, Cell, ScrabbleGame

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile ('A',1)
        self.assertEqual(tile.letter,'A')
        self.assertEqual (tile.values, 1 )

class TestBagTile(unittest.TestCase):
    @patch('random.shuffle')     
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTile()
        self.assertEqual(len(bag.tiles), 5)

    def test_take(self):
        bag = BagTile()
        tiles = bag.take(2)  
        self.assertEqual(len(bag.tiles), 3)  
        self.assertEqual(len(tiles), 2) 

    def test_put(self):
        bag = BagTile()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]  
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), 7)  

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player()
        self.assertEqual(
            len(player.tiles),
            0,
        )

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)
    
    def test_validate(self):  
        board = Board()
        word = 'Facultad'
        location = (5,10)
        orientation = 4
        word_is_valid = board.validate_word(word,location,orientation)
        assert word_is_valid == True

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False


class TestCell(unittest.TestCase):
    def test_cell(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier, 2)
        self.assertEqual(cell.multiplier_type, 'letter')
        self.assertIsNone(cell.letter)
    
    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', values=3)
        cell.add_letter(letter)
        self.assertEqual(cell.letter.letter, 'p')
    
    def test_cell_value(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', values=3)
        cell.add_letter(letter)
        self.assertEqual(cell.calculate_value(), 3)
    
    def test_cell_multiplier_active(self):
        pass
    
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

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]      
if __name__ == '__main__':
    unittest.main()