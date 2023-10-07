import unittest
from game.cell import Cell
from game.tile import Tile

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

if __name__ == '__main__':
    unittest.main()