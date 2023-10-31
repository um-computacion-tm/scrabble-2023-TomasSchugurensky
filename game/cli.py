def show_player(self):
        print(f"Nombre del jugador: {self.name}")
        print("Fichas del jugador:", ", ".join([tile.letter for tile in self.tiles]))

def get_player_count():
    while True:
        try:
            player_count = int(input('cantidad de jugadores (1-3): '))
            if player_count <= 3:
                break
        except Exception as e:
            print('ingrese un numero por favor')

    return player_count

def show_board(self):
    print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
    for row_index, row in enumerate(self.grid):
        print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([cell.value if cell.value else "   " for cell in row])
        )