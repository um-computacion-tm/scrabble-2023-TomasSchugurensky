import unittest
from game.player import Player
from game.bagtile import BagTile
from game.tile import Tile

class TestPlayer(unittest.TestCase):
    def test_player(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles)
        self.assertEqual(
            len(player.tiles),
            0,
        )

    def test_validate_has_letters(self):
        bag_tile = BagTile()
        player= Player(bag_tile)
        bag_tile.tiles=[
            Tile(letter='H', values=4),
            Tile(letter='O', values=1),
            Tile(letter='L', values=1),
            Tile(letter='A', values=1),
            Tile(letter='A', values=1),
            Tile(letter='A', values=1),
            Tile(letter='A', values=1),
        ]
        tiles = [
            Tile(letter='H', values=4),
            Tile(letter='O', values=1),
            Tile(letter='L', values=1),
            Tile(letter='A', values=1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()