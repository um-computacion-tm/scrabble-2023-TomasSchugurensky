import unittest
from game.cell import Cell
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
        cell.add_letter('A')
        self.assertEqual(cell.letter, 'A')
        self.assertEqual(cell.value, 'A')
    
    def test_cell_value(self):
        cell = Cell(multiplier=3, multiplier_type="word")
        cell.add_letter('Z')
        self.assertEqual(cell.calculate_value(), 3 * 'Z'.values)

    def test_repr(self):
        cell = Cell()
        cell.add_letter('B')
        self.assertEqual(repr(cell), repr('B'))

    def test_repr_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type="word")
        self.assertEqual(repr(cell), 'Wx2')
        cell = Cell(multiplier=3, multiplier_type="letter")
        self.assertEqual(repr(cell), 'Lx3')
        cell = Cell(multiplier=1, multiplier_type="letter")
        self.assertEqual(repr(cell), '   ')
    

if __name__ == '__main__':
    unittest.main()