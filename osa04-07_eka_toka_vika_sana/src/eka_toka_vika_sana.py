# tee ratkaisu tänne
def eka_sana(teksti):
    sanat = teksti.split(" ")
    return sanat[0]

def toka_sana(teksti):
    sanat = teksti.split(" ")
    return sanat[1]

def vika_sana(teksti):
    sanat = teksti.split(" ")
    return sanat[-1]
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))