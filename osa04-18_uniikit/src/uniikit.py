# tee ratkaisu tänne
def uniikit(lista: list):
    tulos = []
    for luku in lista:
        if luku not in tulos:
            tulos.append(luku)
 
    tulos.sort()
    return tulos

if __name__ == "__main__":

    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))