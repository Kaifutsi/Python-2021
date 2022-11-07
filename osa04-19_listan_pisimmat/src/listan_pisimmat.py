# tee ratkaisu tänne
def pisimmat(lista):

    pituus = 0
    uusiLista = []

    for i in lista:
        if len(i) > pituus:
            pituus = len(i)

    for i in lista:
        if len(i) == pituus:
            uusiLista.append(i)

    return uusiLista

if __name__ == "__main__":

    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos)