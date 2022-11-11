# tee ratkaisu tänne
def histogrammi(sana : str):
    kirjaimet = {}
    for i in sana:
        if i not in kirjaimet:
            kirjaimet[i] = 0
        kirjaimet[i] += 1
    
    for key, value in kirjaimet.items():
        print(f"{key} {value*'*'}")

if __name__ == "__main__":
    histogrammi("statistically")