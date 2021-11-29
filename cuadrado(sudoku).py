def es_cuadrado(sudoku):
    longitud = len(sudoku)
    for posicion in range(len(sudoku) - 1):
        if len(sudoku[posicion]) == longitud:
            continue
        else:
            return False        
    return True