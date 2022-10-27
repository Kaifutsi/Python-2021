# Kirjoita ratkaisu tähän
res = 0
sum = 0
positiivi = 0
negatiivi = 0
print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
    luku = int(input("Luku:"))
    if luku == 0:
        break
    res += 1
    print(f"Lukuja yhteensä {res}")
    sum += luku
    print(f"Lukujen summa {sum}")
    kesk = sum / res
    print(f"Lukujen keskiarvo {kesk}")
    if luku > 0:
        positiivi += 1
    else:
        negatiivi += 1
print(f"Positiivisia {positiivi}")
print(f"Negatiivisia {negatiivi}") 