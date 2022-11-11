# tee ratkaisu tänne
def transponoi(matriisi: list):
    for x in range(len(matriisi)):
        for y in range(x, len(matriisi)):
            temp = matriisi[x][y]
            matriisi[x][y] = matriisi[y][x]
            matriisi[y][x] = temp

if __name__ == "__main__":
    matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matriisi)
    transponoi(matriisi)
    print(matriisi)