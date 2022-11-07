# Kirjoita ratkaisu tähän
koko = int(input("Kuinka monta lukua: "))
lista = []
i = 1 
while i <= koko:
    item = int(input(f"Item {i}:"))
    lista.append(item)
    i += 1
print(lista)