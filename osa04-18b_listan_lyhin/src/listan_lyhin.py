# tee ratkaisu tänne
def lyhin(lista : list):
    lyhin = lista[0]
    for i in lista:
        if len(i) <= len(lyhin):
            lyhin = i
    return lyhin
    
if __name__ == "__main__":
    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]
    tulos = lyhin(lista)
    print(tulos)