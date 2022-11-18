# tee ratkaisu tänne
def suurin():
    luvut = []
    with open("luvut.txt") as new_file:
        for line in new_file:
            luvut.append(int(line))
    if len(luvut) > 0:
        suurin = luvut[0]
        for num in luvut:
            if num > suurin:
                suurin = num
        return suurin

if __name__ == "__main__":
    suurin()