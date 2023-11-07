from game.scrabblegame import ScrabbleGame
from game.bagtile import BagTile
from game.player import Player
from game.cli import UserInterface

def main():
    bag_tiles = BagTile()
    player_count = UserInterface.get_player_count()
    players = [Player(bag_tiles, f"Jugador {i + 1}") for i in range(player_count)]
    print("About to instantiate ScrabbleGame") 
    game = ScrabbleGame(player_count)
    
    current_player_index = 0  

    while game.is_playing():
        current_player = players[current_player_index]
        UserInterface.show_board(game.get_board())
        UserInterface.show_player(current_player)
        
        accion = input("Ingresa una palabra ('P'), intercambiar fichas ('I'), saltar turno ('S'), terminar juego ('E') : ").strip().upper()

        if accion == 'E':
            print("Juego terminado por el jugador")
            break

        if accion == 'P':
            word, location, orientation = UserInterface.get_inputs()
            game.play(word, location, orientation)

        if accion == 'I':
            UserInterface.exchange_tile(current_player, bag_tiles)
        
        if accion == 'S':
            game.skip_turn()

        current_player_index = (current_player_index + 1) % player_count

if __name__ == "__main__":
    main()