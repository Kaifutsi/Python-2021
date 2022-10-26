# Kirjoita ratkaisu tähän
print("Kerro huominen sääennuste:")
temp = int(input("Lämpötila:"))
sate = input("Sataako (kyllä/ei):")
print("Pue housut ja t-paita")

if temp < 21:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")

if temp < 11:
    print("Pue päälle takki")
    print("Ota myös pitkähihainen paita")

if temp < 6:  
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if sate == "kyllä":
    print("Muista sateenvarjo!")