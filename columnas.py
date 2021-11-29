
def columnas(sudoku):
    longitud = len(sudoku)
    comparador = []
    for posicion in range(1, longitud + 1):
        comparador.append(posicion)
    for posicion in range(len(sudoku)):
        columna = []
        for fila in sudoku:
            columna.append(fila[posicion])
        columna.sort()
        if columna == comparador:
            continue
        else:
            return False
    return True