# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, piece: str):
    if (x < 0 or x > 2) or (y < 0 or y > 2):
        return False 

    for rivi in range(3):
        for sarake in range(3): 
            if lauta[y][x] == "":
                lauta[y][x] = piece
                return True
    return False

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)