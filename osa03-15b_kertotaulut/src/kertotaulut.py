# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
i = 1

while i <= luku:
    x = 1
    while x <= luku:
        print(f"{i} x {x} = {i*x}")
        x += 1
    i += 1