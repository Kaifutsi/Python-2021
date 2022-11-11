# tee ratkaisu tänne
def tulosta(sudoku: list):
    uusiRivi=0
    uusiSarake=0

    for r in range(9):
        for s in range(9):
            if sudoku[s][r] == 0:
                sudoku[s][r] = "_"

    pelilauta = sudoku[:]

    for uusiRivi in range(9):
        if uusiRivi > 0 and uusiRivi % 3 == 0:
            print()

        for uusiSarake in range (0,9):
            print(pelilauta[uusiRivi][uusiSarake], end=" ")
            if (uusiSarake + 1) % 3 == 0:
                print(end=" ")
        print()
              
def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    outSudoku = []

    for rivi in sudoku:
        temp = []
        for i in rivi:
            temp.append(i)
        outSudoku.append(temp)
    outSudoku[rivi_nro][sarake_nro] = luku
    return outSudoku 
    
if __name__ == "__main__":
    
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)