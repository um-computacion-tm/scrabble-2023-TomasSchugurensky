import unittest
from game.models import Board
from game.tile import Tile
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)
    
    def setUp(self) -> None:
        self.board = Board()
    
    def test_validate(self):
        board = Board()
        word = "TEST"
        location = (0, 0)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid, "La palabra debería ser válida y ajustarse dentro del tablero.")

    def test_word_inside_board(self):
        word = "casa"
        location = (5, 4)
        orientation = "H"
        word_is_valid = self.board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_place_word_on_board(self):
        board = Board()  
        word = "TEST"
        tiles = board.string_to_tiles(word)  
        location = (7, 7)
        orientation = "H"
        is_placed = board.put_words(tiles, location, orientation)
        self.assertTrue(is_placed, "La palabra debe ser puesta")

    def test_word_out_of_board(self):
        board = Board()
        word = "TEST"
        location = (0, 15)  
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid, "La palabra debería ser inválida y no ajustarse dentro del tablero.")

    def test_board_is_empty(self):
        board = Board()
        self.assertTrue(board.is_empty)

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Casa"
        tiles = board.string_to_tiles(word)  
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.put_words(tiles, location, orientation)
        self.assertTrue(word_is_valid, "Palabra debió haberse puesto")

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        cell1 = Cell()
        cell2 = Cell()
        cell3 = Cell()
        cell4 = Cell()
        cell1.add_letter(Tile('F', 1))
        cell2.add_letter(Tile('a', 1))
        cell3.add_letter(Tile('c', 1))
        cell4.add_letter(Tile('u', 1))
        board.grid[2][4] = cell1
        board.grid[3][4] = cell2
        board.grid[4][4] = cell3
        board.grid[5][4] = cell4
    
        word = "Facultad"
        location = (4, 3)
        orientation = "H"
    
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertFalse(word_is_valid)

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertFalse(word_is_valid)
    
    def test_show_board(self):
        board = Board()
        cell1 = Cell()
        cell2 = Cell()
        cell3 = Cell()
        cell4 = Cell()
        cell1.add_letter(Tile('C', 1))
        cell2.add_letter(Tile('A', 1))
        cell3.add_letter(Tile('S', 1))
        cell4.add_letter(Tile('A', 1))
        board.grid[7][7] = cell1
        board.grid[8][7] = cell2
        board.grid[9][7] = cell3
        board.grid[10][7] = cell4

    def test_calculate_word_value(self):
        board = Board()
        word = "TEST"
        tiles = board.string_to_tiles(word)
        location = (7, 7)
        orientation = "H"
        board.put_words(tiles, location, orientation)
    
        cells = board.get_cells(location, orientation, len(word))
        calculated_value = board.calculate_word_value(cells)
    
        expected_value = sum(tile.values for tile in tiles)
        self.assertEqual(calculated_value, expected_value, "El calculo es igual al valor de las letras")
    