# Kirjoita ratkaisu tähän
sana = input("Anna merkkijono: ")
i = -1
yht = ""
while i >= -len(sana):
    yht = sana[i] + yht
    print(yht)
    i -= 1