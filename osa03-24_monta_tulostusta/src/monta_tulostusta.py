# tee ratkaisu tähän
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def tulosta_monesti(teksti, kerta):
    i = 1
    while i <= kerta:  
        print(teksti)
        i += 1

if __name__ == "__main__":
    tulosta_monesti("python", 5)
