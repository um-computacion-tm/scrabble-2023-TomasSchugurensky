import unittest
from game.player import Player
from game.bagtile import BagTile
from game.tile import Tile

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player()
        self.assertEqual(
            len(player.tiles),
            0,
        )

    def test_validate_has_letters(self):
        player= Player()
        bag_tile = BagTile()
        bag_tile.tiles=[
            Tile(letter='H', values=1),
            Tile(letter='O', values=1),
            Tile(letter='L', values=1),
            Tile(letter='A', values=1),
            Tile(letter='A', values=1),
            Tile(letter='A', values=1),
            Tile(letter='A', values=1),
        ]
        tiles = [
            Tile(letter='H', values=1),
            Tile(letter='O', values=1),
            Tile(letter='L', values=1),
            Tile(letter='A', values=1),
        ]
        is_valid = player.has_letters(tiles)

        assert is_valid

if __name__ == '__main__':
    unittest.main()