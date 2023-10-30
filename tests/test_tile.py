import unittest
from game.tile import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile ('A',1)
        self.assertEqual(tile.letter,'A')
        self.assertEqual (tile.values, 1 )

    def test_calculate_word_value(self):
        tile = Tile('A',1)
        result = tile.calculate_word_value()
        self.assertEqual(result, 1)

    def test_calculate_word_value_multiplier(self):
        tile = Tile ('B',5)
        result = tile.calculate_word_value(2)
        self.assertEqual(result,10)
    
    def test_repr(self):
        tile = Tile('C', 3)
        result = repr(tile)
        self.assertEqual(result, 'C:3')


if __name__ == '__main__':
    unittest.main()