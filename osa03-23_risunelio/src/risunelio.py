# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti


def risunelio(koko):
    i = 1 
    while i <= koko:
        print("#"*koko)
        i += 1

if __name__ == "__main__":
    risunelio(5)