# tee ratkaisu tänne
def samat(teksti, luku1, luku2):
    if luku1 >= len(teksti) or luku2 >= len(teksti):
        return False
    return teksti[luku1] == teksti[luku2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(samat("abc", 1, 3))

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 