# tee ratkaisu tänne
def luvuista_suurin(num1,num2,num3):
    lista1 = []
    lista1.append(num1)
    lista1.append(num2)
    lista1.append(num3)

    return max(lista1)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)