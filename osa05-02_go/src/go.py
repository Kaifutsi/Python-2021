# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
    pisteet1 = 0
    pisteet2 = 0
 
    for rivi in pelilauta:
        for nelio in rivi:
            if nelio == 1:
                pisteet1 += 1
            elif nelio == 2:
                pisteet2 += 1
    
    if pisteet1 > pisteet2:
        return 1
    elif pisteet2 > pisteet1:
        return 2
    else:
        return 0


if __name__ == "__main__":
    go = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(kumpi_voitti(go))