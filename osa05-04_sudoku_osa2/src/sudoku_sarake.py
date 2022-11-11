# tee ratkaisu tänne
def sarake_oikein(sudoku: list, sarake_nro: int):
    uusi_lista = []
    for i in range(len(sudoku)): 
        for j in range(len(sudoku[i])): 
            if sudoku[i][sarake_nro] > 0 and sudoku[i][sarake_nro] in uusi_lista:
                return False
        else:
            uusi_lista.append(sudoku[i][sarake_nro])

    return True

if __name__ == "__main__":

    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sarake_oikein(sudoku, 0))
    print(sarake_oikein(sudoku, 1))