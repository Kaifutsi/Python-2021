# tee ratkaisu tänne

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
def shakkilauta(length):
    numerot = ["0", "1"]

    for x in range(length):
        for y in range(length):
            i = numerot[(x + y + 1) % 2]
            print(i, end=(''))
        print()

if __name__ == "__main__":
    shakkilauta(3)
