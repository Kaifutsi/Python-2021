# tee ratkaisu tänne
def kaanna(sanasto: dict):
    temp = {}
    
    for key, value in sanasto.items():
        temp[value] = key

    sanasto.clear()

    for key, value in temp.items():
        sanasto[key] = value

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)