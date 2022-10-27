# Kirjoita ratkaisu tähän
tarina = ""
viime = ""
while True:
    sana = input("Anna sana: ")
    if sana == "loppu" or sana == viime:
        break
    tarina = tarina + sana + " "
    viime = sana
print(tarina)