# Kirjoita ratkaisu tähän
sana1 = input("Anna jono 1: ")
sana2 = input("Anna jono 2: ")

if len(sana1) > len(sana2):
    print(f"{sana1} on pidempi")
elif len(sana2) > len(sana1): 
    print(f"{sana2} on pidempi")
else:
    print("Jonot ovat yhtä pitkät")