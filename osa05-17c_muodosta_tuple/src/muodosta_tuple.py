# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
    lista = [x, y, z]

    pienin = min(lista)
    suurin = max(lista)
     
    tuple = (pienin, suurin, sum(lista))

    return tuple


if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))