# Kirjoita ratkaisu tähän
lista = []
while True:
    print(f"Lista on nyt {lista}")
    valinta = input("(l)isää, (p)oista vai e(x)it:")
    if valinta == "l":
        kohde = len(lista) + 1
        lista.append(kohde)
    elif valinta == "p":
        lista.pop(len(lista) - 1)
    elif valinta == "x":
        break
    
print("Moi!")