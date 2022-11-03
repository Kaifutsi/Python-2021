# Kirjoita ratkaisu tähän
ker = 1
while True:
    luku = int(input("Anna luku: "))
    if luku <= 0:
        break
    i = 1
    while i <= luku:
        ker *= i
        i += 1
    print(f"Luvun {luku} kertoma on {ker}")
    ker = 1
print("Kiitos ja moi!")