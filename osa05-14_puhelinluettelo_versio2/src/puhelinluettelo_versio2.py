# tee ratkaisu tänne
def hae(puhkirja):
    nimi = input("nimi: ")
    if nimi not in puhkirja:
        print("ei numeroa")
    else:
        for num in puhkirja[nimi]:
            print(num)

def lisaa(puhkirja):
    nimi = input("nimi: ")
    numero = input("nimi: ")

    if nimi not in puhkirja:
        puhkirja[nimi] = []
    puhkirja[nimi].append(numero)

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