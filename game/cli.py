def show_player(self):
        print(f"Nombre del jugador: {self.name}")
        print("Fichas del jugador:", ", ".join([tile.letter for tile in self.tiles]))

def get_player_count():
    while True:
        try:
            import pdb; pdb.set_trace()
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

def get_inputs():
    word_input = input("Ingrese palabra: ").strip()
    location_input = input("Ingrese la ubicación (fila, columna): ").strip()
    orientation_input = input("Ingrese la orientación (horizontal o vertical): ").strip()
    location_parts = location_input.split(',')
    if len(location_parts) != 2:
        raise ValueError("La ubicación debe tener el formato 'fila, columna'")
    try:
        row = int(location_parts[0])
        col = int(location_parts[1])
    except ValueError:
        raise ValueError("La fila y columna deben ser números enteros")
    return word_input, (row, col), orientation_input  