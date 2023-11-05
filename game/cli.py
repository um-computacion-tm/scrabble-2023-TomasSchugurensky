class UserInterface:

    def show_player(self):
        print(f"Nombre del jugador: {self.name}")
        print("Fichas del jugador:", ", ".join([tile.letter for tile in self.tiles]))

    def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if 1 <= player_count <= 3:
                    return player_count
                else:
                    print('Por favor, ingrese un número entre 1 y 3.')
            except ValueError:
                print('Por favor, ingrese un número válido.')
    
    @staticmethod
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
    
    @staticmethod
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([cell.value if cell.value else "   " for cell in row])
            )