# Kirjoita ratkaisu tähän
sana = input("Anna sana: ")
toinen = sana[1]
toinenVim = sana[-2]

if toinen != toinenVim:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")
else:
    print(f"Toinen ja toiseksi viimeinen kirjain on {toinen}")