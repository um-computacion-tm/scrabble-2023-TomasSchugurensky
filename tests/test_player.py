import unittest
from game.player import Player
from game.bagtile import BagTile
from game.tile import Tile

class TestPlayer(unittest.TestCase):
    def test_player(self):
        bag_tiles = BagTile()  
        player = Player(bag_tiles, "Nombre")
        self.assertEqual(len(player.tiles), 7)
        additional_tiles = player.rellenar(bag_tiles)
        self.assertEqual(additional_tiles, 0)
        self.assertEqual(len(player.tiles), 7)

    def test_rellenar(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Nombre")
        self.assertEqual(len(player.tiles), 7)  
        additional_tiles = player.rellenar(bag_tiles)  
        self.assertEqual(additional_tiles, 0)  
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

    def test_exchange(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Nombre")
        player.tiles = [
            Tile(letter='H', values=4),
            Tile(letter='O', values=1),
            Tile(letter='L', values=1),
            Tile(letter='A', values=1),
        ]

        tiles_to_exchange = player.tiles[:2]  
        exchange_successful = player.exchange(tiles_to_exchange, bag_tiles)

        self.assertTrue(exchange_successful, "Intercambio exitoso")
        self.assertEqual(len(player.tiles), 7, "Jugador debe tener 7 fichas después de intercambiar")

        for tile in tiles_to_exchange:
            self.assertIn(tile, bag_tiles.tiles, "Las fichas intercambiadas deben estar en la bolsa")

    def test_exchange_invalid(self):
        bag_tiles = BagTile()
        player = Player(bag_tiles, "Nombre")
        player.tiles = [
            Tile(letter='H', values=4),
            Tile(letter='O', values=1),
            Tile(letter='L', values=1),
            Tile(letter='A', values=1),
        ]
        bag_tiles.tiles = [
            Tile(letter='B', values=3),
            Tile(letter='E', values=1),
            Tile(letter='S', values=1),
            Tile(letter='T', values=1),
        ]

        tiles_to_exchange = [Tile(letter='X', values=8), Tile(letter='Y', values=10)]
        initial_bag_count = len(bag_tiles.tiles)
        exchange_unsuccessful = player.exchange(tiles_to_exchange, bag_tiles)

        self.assertFalse(exchange_unsuccessful, "Intercambio no debe ser exitoso")
        self.assertEqual(len(player.tiles), 4, "Jugador no deberia perder fichas")
        self.assertEqual(len(bag_tiles.tiles), initial_bag_count, "La bolsa no debería cambiar si el intercambio es inválido")

if __name__ == '__main__':
    unittest.main()