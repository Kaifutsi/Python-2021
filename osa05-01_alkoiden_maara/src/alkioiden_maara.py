# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
    luku = 0
    for i in range(len(matriisi)): 
        for x in range(len(matriisi[i])):  
            if matriisi[i][x] == alkio:
                luku += 1
    return luku
    
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))