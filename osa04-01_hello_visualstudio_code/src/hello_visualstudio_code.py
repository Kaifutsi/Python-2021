# Kirjoita ratkaisu tähän
while True:
    mjono = input("Editori: ")

    if mjono.lower() == "NOTEPAD" or mjono.lower() == "word":
        print("surkea")
    elif mjono.lower() == "visual studio code":
        print("loistava valinta!")
        break
    else:
        print("ei ole hyvä")