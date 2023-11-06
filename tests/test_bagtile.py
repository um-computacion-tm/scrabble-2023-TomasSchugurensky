import unittest
from game.bagtile import BagTile
from game.tile import Tile
from unittest.mock import patch

class TestBagTile(unittest.TestCase):
    @patch('random.shuffle')     
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTile()
        self.assertEqual(len(bag.tiles), 101)

    def test_take(self):
        bag = BagTile()
        tiles = bag.take(2)  
        self.assertEqual(len(bag.tiles), 99)  
        self.assertEqual(len(tiles), 2) 

    def test_put(self):
        bag = BagTile()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]  
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), 103)  

if __name__ == '__main__':
    unittest.main()