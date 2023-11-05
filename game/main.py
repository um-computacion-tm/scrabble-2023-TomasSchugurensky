from game.scrabblegame import ScrabbleGame
from game.bagtile import BagTile
from game.player import Player
from game.cli import UserInterface

def main():
    bag_tiles = BagTile()
    current_player_index = 0
    player_count = UserInterface.get_player_count()  
    players = [Player(bag_tiles, f"Jugador {i + 1}") for i in range(player_count)]
    game = ScrabbleGame(player_count)

    while game.is_playing():
        current_player = players[current_player_index]
        UserInterface.show_board(game.get_board())  
        UserInterface.show_player(current_player)    
        accion = input("Ingresa una palabra ('P'), intercambiar fichas ('I'), saltar turno ('S') : ").upper()

        if accion == 'P':
            word, coords, orientation = UserInterface.get_inputs()  
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
                        print("Intercambio erróneo")
                except Exception as e:
                    print(e)
        
        if accion == 'S':
            game.skip_turn()

        current_player_index = (current_player_index + 1) % player_count

if __name__ == "__main__":
    main()