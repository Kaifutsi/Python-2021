# Kirjoita ratkaisu tähän
tuntipalkka = float(input("Tuntipalkka:"))
tunti = int(input("Työtunnit:"))
paiva = input("Viikonpäivä:")

palkka = tuntipalkka * tunti
if paiva == "sunnuntai":
    palkka *= 2
print(f"Palkka {palkka} euroa")