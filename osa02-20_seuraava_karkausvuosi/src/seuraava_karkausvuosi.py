# Kirjoita ratkaisu tähän
vuosi = int(input("Vuosi:"))
seurVuosi = vuosi + 1

while True:
    if seurVuosi % 4 == 0 and seurVuosi % 100 != 0 or seurVuosi % 400 == 0:
        break
    seurVuosi += 1
print(f"Vuotta {vuosi} seuraava karkausvuosi on {seurVuosi}") 