import unittest
from game.player import Player
from game.bagtile import BagTile
from game.tile import Tile

class TestPlayer(unittest.TestCase):
    def test_player(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Nombre")
        self.assertEqual(
            len(player.tiles),
            7,
        )

    def test_rellenar(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Player 1")
        self.assertEqual(len(player.tiles), 7)
        additional_tiles = player.rellenar(bag_tiles)
        self.assertGreater(additional_tiles, 0)
        self.assertEqual(len(player.tiles), 7 + additional_tiles)

    def test_validate_has_letters(self):
        bag_tile = BagTile()
        player = Player(bag_tile, "Nombre")
        bag_tile.tiles = [
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
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()