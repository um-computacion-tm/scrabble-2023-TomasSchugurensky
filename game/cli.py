class UserInterface:

    @staticmethod
    def exchange_tile(player, bag_tiles):
        print("Current tiles:", ", ".join([f"{tile.letter}" for tile in player.tiles]))
        while True:
            try:
                index_exchange = int(input(f"Enter index of tile to change (0-{len(player.tiles) - 1}): "))
                if 0 <= index_exchange < len(player.tiles):
                    break
                else:
                    print(f"Please enter a valid index between 0 and {len(player.tiles) - 1}.")
            except ValueError:
                print("Please enter a number.")

        
        tile_to_exchange = player.tiles[index_exchange]
        player.exchange_tile(bag_tiles, tile_to_exchange)
        print("Tile exchanged successfully.")

    
    @staticmethod
    def show_player(player):
        print(f"Nombre del jugador: {player.name}")
        print("Fichas del jugador:", ", ".join([tile.letter for tile in player.tiles]))
        print(f"Puntuación de {player.name}: {player.score}")

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
        word_input = input("Ingrese palabra: ").strip().upper()  
        location_input = input("Ingrese la ubicación (fila, columna): ").strip()
        orientation_input = input("Ingrese la orientación (horizontal 'H' o vertical 'V'): ").strip().upper()  
        location_parts = location_input.split(',')
        if len(location_parts) != 2:
            raise ValueError("La ubicación debe tener el formato 'fila, columna'")
        try:
            row = int(location_parts[0]) - 1
            col = int(location_parts[1]) - 1
        except ValueError:
            raise ValueError("La fila y columna deben ser números enteros")
    
        if orientation_input not in ('H', 'V'):
            raise ValueError("La orientación debe ser 'H' para horizontal o 'V' para vertical")
    
        return word_input, (row, col), orientation_input
    
    @staticmethod
    def show_score(player):
        print(f"Puntuación de {player.name}: {player.score}")
    
    @staticmethod
    def show_board(board):
        multiplier_symbols = {
            'DL': '2L',
            'TL': '3L',
            'DW': '2W',
            'TW': '3W',
            None: '  '  
        }
        print('\n  |' + ''.join([f' {str(col_index).rjust(2)} ' for col_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            row_display = ''
            for cell in row:
                if cell.value: 
                    row_display += f' {cell.value} '
                else: 
                    row_display += f' {multiplier_symbols[cell.multiplier_type]} '
            print(f'{str(row_index).rjust(2)}|{row_display}')