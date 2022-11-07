# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)

def risulaatikko(korkeus):
    # You should call function line here with proper parameters
    i = 1
    while i <= korkeus:
        viiva(10, "#")
        i += 1    

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
