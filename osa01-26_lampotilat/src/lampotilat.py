# Kirjoita ratkaisu tähän
luku = int(input("Anna lämpötila (F):"))
celsius = (luku - 32) * 5.0/9.0
print(f"{luku} fahrenheit-astetta on {celsius} celsius-astetta")
if celsius < 0:
    print("celsius-astetta Paleltaa!")