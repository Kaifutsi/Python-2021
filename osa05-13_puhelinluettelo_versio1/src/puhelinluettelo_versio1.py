# tee ratkaisu tänne
def hae(puhkirja):
    nimi = input("nimi: ")
    if nimi in puhkirja:
        print(puhkirja[nimi])
    else:
        print("ei numeroa")

def lisaa(puhkirja):
    nimi = input("nimi: ")
    numero = input("numero: ")
    puhkirja[nimi] = numero
    print("ok!")

def main():
    puhkirja = {}
    while True:
        komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))

        if komento == 1:
            hae(puhkirja)
        if komento == 2:
            lisaa(puhkirja)
        if komento == 3:
            break
    print("lopetetaan...")

main()