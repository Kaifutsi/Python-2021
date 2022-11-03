# tee ratkaisu tänne

def nelio(teksti, numero):
    numerot = []
    a = 0
    for i in teksti:
        numerot += i

    for x in range(numero):
        for y in range(numero):
            i = numerot[a]
            print(i, end=(''))
            a += 1
            if a == len(numerot):
                a = 0
        print()

if __name__ == "__main__":
    nelio("teksti", 3)