import unittest
from game.cell import Cell
from game.tile import Tile
from game.models import Board
letter_values = {'A':1, 'B':5, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1, 'J':8, 'K':8, 
                 'L':1, 'M':3, 'N':1, 'Ñ':8, 'O':1, 'P':3, 'Q':5, 'R':1, 'S':1, 'T':1, 'U':1,
                  'V':4, 'W':8, 'X':8, 'Y':4, 'Z':10, 'CH':5, 'LL':8, 'RR':8 }

class TestCell(unittest.TestCase):
    def test_cell(self):
        cell = Cell()
        self.assertIsNone(cell.multiplier)
        self.assertIsNone(cell.multiplier_type)
        self.assertIsNone(cell.letter)
        self.assertTrue(cell.active)
        self.assertEqual(cell.value, "")

    def test_add_letter(self):
        cell = Cell()
        letter = Tile("A", 1)
        cell.add_letter(letter)
        self.assertEqual(cell.letter, letter)
        self.assertEqual(cell.value, letter.letter)

    def test_add_letter_with_string(self):
        cell = Cell(letter_values=letter_values)
        cell.add_letter("B")
        expected_tile = Tile("B", letter_values['B'])
        self.assertEqual(cell.letter.letter, expected_tile.letter)
        self.assertEqual(cell.value, expected_tile.letter)

    def test_add_no_letter(self):
        cell = Cell()
        with self.assertRaises(ValueError):
            cell.add_letter('')
    
    def test_add_tile(self):
        cell = Cell()
        tile = Tile('B', 5)
        cell.add_letter(tile)
        self.assertEqual(cell.letter, tile)
        self.assertEqual(cell.value, tile.letter)
    
    def test_cell_value(self):
        board = Board()  
        cell = Cell(multiplier=3, multiplier_type="word")
        cell.add_letter(Tile('Z', 10))
        cells = [cell]  

        calculated_value = board.calculate_word_value(cells)  

        expected_value = 3 * Tile('Z', 10).values
        self.assertEqual(calculated_value, expected_value)

    

    def test_repr(self):
        cell = Cell()
        tile = Tile('B', letter_values['B'])
        cell.add_letter(tile)
        self.assertEqual(repr(cell), repr(tile))

    def test_repr_letters(self):
        cell = Cell()
        tile = Tile("A", 1)
        cell.add_letter(tile)
        self.assertEqual(repr(cell), repr(tile))

    def test_repr_word_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type="word")
        self.assertEqual(repr(cell), 'Wx2')

    def test_repr_letter_multiplier(self):
        cell = Cell(multiplier=3, multiplier_type="letter")
        self.assertEqual(repr(cell), 'Lx3')

    def test_repr_without_letter_or_multiplier(self):
        cell = Cell()
        self.assertEqual(repr(cell), '   ')

if __name__ == '__main__':
    unittest.main()