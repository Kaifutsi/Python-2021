from math import sqrt
# Kirjoita ratkaisu tähän

while True:
    luku = int(input("Syötä luku: "))
    if luku == 0:
        break
    elif luku < 0:
        print("Epäkelpo luku")
    else:
        print(sqrt(luku))
print("Lopetetaan...")