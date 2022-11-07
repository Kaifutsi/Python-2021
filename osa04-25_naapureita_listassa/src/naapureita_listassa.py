# tee ratkaisu tänne
def pisin_naapurijono(lista: list):
    pituus = 1
    tulos = 1
    for i in range(1, len(lista)):
        if abs(lista[i-1]-lista[i]) == 1:
            tulos += 1
        else:
            tulos = 1
        pituus = max(pituus, tulos)
    return pituus

if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))