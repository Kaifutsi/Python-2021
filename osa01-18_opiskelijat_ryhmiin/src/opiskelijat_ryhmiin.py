# Kirjoita ratkaisu tähän
opiskelijat = int(input("Montako opiskelijaa? "))
koko = int(input("Mikä on ryhmän koko? "))

ryhmat = (opiskelijat + koko -1) // koko

print("Ryhmien määrä: ", ryhmat)