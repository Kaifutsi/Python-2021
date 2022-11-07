# Kirjoita ratkaisu tähän
lista = []
while True:
    sana = input("sana: ")
    if sana in lista:
        print(f"Annoit {len(lista)} eri sanaa")
        break
    lista.append(sana)