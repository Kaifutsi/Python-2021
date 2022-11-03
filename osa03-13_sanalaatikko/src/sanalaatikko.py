# Kirjoita ratkaisu tähän
sana = input("Sana: ")

alku = (28 - len(sana)) // 2
if len(sana) % 2 == 0:
    loppu = alku
else:
    loppu = alku+1


print('*' * 30)
print(f"*{(alku * ' ')}{sana}{(loppu * ' ')}*")
print('*' * 30)