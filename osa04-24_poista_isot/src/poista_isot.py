# tee ratkaisu tänne
def poista_isot(lista : list):
    lista2 = []
    for i in lista:
        if i.isupper():
            continue
        else:
            lista2.append(i)
    return lista2

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)