# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)

def kuvio(koko1, merkki1, koko2, merkki2):
    i = 1
    while i <= koko1:
        viiva(i, merkki1)
        i += 1
    i = 1
    while i <= koko2:
        viiva(koko1, merkki2)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
