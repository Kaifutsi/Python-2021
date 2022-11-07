# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= koko:
        viiva(koko, merkki)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
