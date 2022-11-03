# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")
i = 0

while i < len(sana)-2:
    if sana[i] == merkki:
        print(sana[i:i+3])
        break
    i += 1