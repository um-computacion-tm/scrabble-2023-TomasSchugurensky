from game.scrabblegame import ScrabbleGame
from game.cli import show_board, show_player, get_player_count, get_inputs
from game.bagtile import BagTile
from game.player import Player


def main():
    bag_tiles = BagTile()  
    current_player_index = 0
    player_count = get_player_count()
    players = [Player(bag_tiles, f"Jugador {i + 1}") for i in range(player_count)]
    game = ScrabbleGame(player_count)

    while game.is_playing():
        current_player = players[current_player_index]
        show_board(game.get_board())
        show_player(current_player)
        accion = input("Ingresa una palabra ('P'), intercambiar fichas ('I'), saltar turno ('S') : ").upper()

        if accion == 'P':
            word, coords, orientation = get_inputs()
            try:
                game.play(word, coords, orientation)
            except Exception as e:
                print(e)

        if accion == 'I':
            tiles_to_exchange_input = input("Fichas a intercambiar (separadas por espacios): ")
            tiles_to_exchange = tiles_to_exchange_input.split()
            if all(tile in current_player.tiles for tile in tiles_to_exchange):
                try:
                    if current_player.exchange(tiles_to_exchange, bag_tiles):
                        print("Intercambio exitoso")
                    else:
                        print("Intercambio erroneo")
                except Exception as e:
                    print(e)
            
        if accion == 'S':
            game.skip_turn()

        current_player_index = (current_player_index + 1) % player_count