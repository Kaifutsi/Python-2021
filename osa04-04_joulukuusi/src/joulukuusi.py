# tee ratkaisu tänne
def joulukuusi(korkeus):
    print("joulukuusi!")
    i = 1
    while i <= korkeus:
        tyhja = korkeus - i
        tahdet = 2 * i - 1
        print(" " * tyhja + "*" * tahdet)
        i += 1
    print(" " * (korkeus - 1) + "*")
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)