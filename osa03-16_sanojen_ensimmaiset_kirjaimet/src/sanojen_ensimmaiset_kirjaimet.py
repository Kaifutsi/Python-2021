# Kirjoita ratkaisu tähän
lause = input("Anna lause: ")
i = 0
if len(lause) != 0:
    print(lause[0])
    while i < len(lause):
        if lause[i] == " ":
            print(lause[i+1])
        i += 1