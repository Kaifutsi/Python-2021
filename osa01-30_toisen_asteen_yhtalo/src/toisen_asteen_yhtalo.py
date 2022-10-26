# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

a = int(input("Anna a: 1"))
b = int(input("Anna b: 2"))
c = int(input("Anna c: -8"))


# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

x1 = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
x2 = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)
print(f"Juuret ovat {x1} ja {x2}")