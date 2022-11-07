# tee ratkaisu tänne
def vaihteluvali(lista : list):
    mini = min(lista)
    maxi = max(lista)
    return maxi - mini
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)