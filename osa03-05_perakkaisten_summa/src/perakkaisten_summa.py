# Kirjoita ratkaisu tähän
raja = int(input("Mihin asti:"))
luku = 1
val = 1
x = "1"
while val < raja:
    luku += 1
    val += luku
    x += f" + {luku}"
print(f"Laskettiin {x} = {val}")