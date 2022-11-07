# tee ratkaisu tänne
def pisimman_pituus(lista : list):
    pituus = len(lista[0])
    for i in lista:
        if len(i) >= pituus:
            pituus = len(i)
    return pituus
    
if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimman_pituus(lista)
    print(tulos)