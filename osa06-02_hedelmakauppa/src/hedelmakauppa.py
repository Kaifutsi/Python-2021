# tee ratkaisu tänne
def lue_hedelmat():
    sanasto = {}
    with open("hedelmat.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            sanasto[parts[0]] = float(parts[1])
            
    return sanasto

if __name__ == "__main__":
    print(lue_hedelmat())