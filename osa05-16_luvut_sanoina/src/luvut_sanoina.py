# tee ratkaisu tänne
def lukukirja():

    sanasto = {}
    numerot = []
    for initialise in range(100):
        numerot.append(initialise)

    sana0 = ['nolla']
    sana1 = ['yksi', 'kaksi', 'kolme','neljä', 'viisi', 'kuusi','seitsemän', 'kahdeksan', 'yhdeksän']
    sana2 = ['kymmenen', 'yksitoista', 'kaksitoista', 'kolmetoista', 'neljätoista',
    'viisitoista', 'kuusitoista', 'seitsemäntoista', 'kahdeksantoista', 'yhdeksäntoista']
    sana3 = ['kaksikymmentä', 'kolmekymmentä', 'neljäkymmentä', 'viisikymmentä', 'kuusikymmentä', 'seitsemänkymmentä', 'kahdeksankymmentä', 'yhdeksänkymmentä']
    rest = []
    
    for i in range(len(sana3)):
        rest.append(sana3[i])
        for j in range(len(sana1)):
            rest.append(sana3[i] + sana1[j])
    
    sanaLista = []
    sanaLista.append(sana0[0])
    for i in sana1:
        sanaLista.append(i)
    for i in sana2:
        sanaLista.append(i)
    for i in rest:
        sanaLista.append(i)
    #print(wordListFinal)

    sanasto = {numerot[i] : sanaLista[i] for i in range(len(numerot))}

    return sanasto

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])