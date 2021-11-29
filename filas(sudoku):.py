def filas(sudoku):
    longitud = len(sudoku)
    comparador = []
    for posicion in range(1, longitud + 1):
        comparador.append(posicion)
    for posicion in range(len(sudoku) - 1):
        sudoku[posicion].sort()
        if comparador == sudoku[posicion]:
            continue
        else:
            return False
    return True