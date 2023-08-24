import unittest
from unittest.mock import patch
from game.models import Tile, BagTile
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

if __name__ == '__main__':
    unittest.main()