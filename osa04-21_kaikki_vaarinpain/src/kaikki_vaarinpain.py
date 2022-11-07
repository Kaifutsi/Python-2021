# tee ratkaisu tänne
def kaikki_vaarinpain(lista : list):
    lista2 = []
    i = len(lista) - 1
    while i >= 0:
        sana = lista[i]
        lista2.append(sana[::-1])
        i -= 1
    return lista2

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)