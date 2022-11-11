# tee ratkaisu tänne
def vanhin(henkilot: list):
    vanhin = henkilot[0][1]
    for henkilo in henkilot:
        vuosi = henkilo[1]
        if vanhin < vuosi:
            vanhin = vuosi

    return vanhin
    
def vanhin(henkilot: list):

    vanhinNimi = henkilot[0][0]
    vanhuus = henkilot[0][1]
    
    for i in henkilot:
        if i[1] < vanhuus:
            vanhuus = i[1]
            vanhinNimi = i[0]

    return (vanhinNimi)

if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))