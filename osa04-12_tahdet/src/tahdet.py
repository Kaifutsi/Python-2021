# tee ratkaisu tänne
def lista_tahtina(lista : list):
    koko = len(lista)
    i = 0
    while i < koko:
        print("*" * lista[i])
        i += 1
        
if __name__ == "__main__":
    lista_tahtina([3, 7, 1, 1, 2])