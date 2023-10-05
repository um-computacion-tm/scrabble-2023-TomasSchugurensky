from game.scrabblegame import ScrabbleGame
def main():
    try:
        players_count = int(input('Cantidad de jugadores?: '))
        if players_count <= 1 or players_count > 4:
            raise ValueError('Cantidad de jugadores no válida')
        scrabble_game = ScrabbleGame(players_count=players_count)
        print (f'Turno del jugador {scrabble_game.current_player.id}')

        word = input('Ingrese palabra: ')
        position_X = input('Ingrese posición (X): ')
        position_Y = input('Ingrese posición (Y): ')
        location = position_X, position_Y
        orientation = input('Ingrese orientación (V/H): ')
        scrabble_game.validate_word(word, location, orientation)
        scrabble_game.next_turn()

    except ValueError as e:
        print(f'Error: {e}')
        print('Valor inválido')
    except Exception as e:
        print(f'Error: {e}')
        print('Error inesperado')