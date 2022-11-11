# tee ratkaisu tänne
def pisin(lista : list):
    pisin = lista[0]
    for sana in lista:
        if len(sana) > len(pisin):
            pisin = sana
    return pisin


if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))