# Kirjoita ratkaisu tähän
merkki = input("Anna merkkijono: ")
osajono = input("Anna osajono: ")

i1 = merkki.find(osajono)
i2 = -1
if i1 != -1:
    i2 = merkki.find(osajono, i1 + len(osajono))

if i2 == -1:
    print('Osajono ei esiinny merkkijonossa kahdesti.')
else:
    print(f"Osajonon toinen esiintymä on kohdassa {i2}.")