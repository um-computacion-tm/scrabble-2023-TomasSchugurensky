from game.get_player import get_player_count
from game.scrabblegame import ScrabbleGame
from game.models import show_board
from game.player import show_player, get_inputs


def main():
    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_board(game.get_board())
        show_player(*game.get_current_player())
        accion = input("Ingresa una palabra ('P'), intercambiar fichas ('I'), saltar turno ('S') : ").upper() #Hacer: Terminar juego, y shuffle (opcional)
        if accion == 'P':
            word, coords, orientation = get_inputs()
            try:
                game.play(word, coords, orientation)
            except Exception as e:
                print(e)
        if accion == 'I':
            tiles_to_exchange = input("Fichas a intercambiar?")
            tiles_to_exchange = [tile for tile in tiles_to_exchange if tile in game.get_current_player()[0].tiles]
            if game.get_current_player()[0].exchange_tiles(tiles_to_exchange):
                print("Intercambio exitoso")
            else:
                print("Intercambio erroneo")
        
        if accion == 'S':
            game.skip_turn()
