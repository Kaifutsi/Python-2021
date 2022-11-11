# tee ratkaisu tänne
def rivi_oikein(sudoku: list, rivi_nro: int):
    uusi_lista = []
    for i in range(0, 9):
        sudoku[rivi_nro][i]
        if sudoku[rivi_nro][i] > 0 and  sudoku[rivi_nro][i] in uusi_lista:
            return False
        else:
            uusi_lista.append(sudoku[rivi_nro][i])
        
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

    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))