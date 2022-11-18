# tee ratkaisu tänne
def lue_tiedosto(file :str):
    with open(file) as f:
        opiskelijat = {}
        s = f.read()
        s = s.strip().split("\n")
        header = s.pop(0)
        header = header.strip().split(";")
        for i in s:
            part = i.split(";")
            temp = []
            for j in range(1,len(part)):
                temp.append(part[j])
            opiskelijat[part[0]] = temp    
    return opiskelijat


def tulosta_piste(opiskelija,tehtava):
    for i in opiskelija:
        tulos = 0
        for j in tehtava[i]:
            tulos += int(j)
        print(opiskelija[i][0],opiskelija[i][1],tulos)
            
if True:
    opiskelija_info = input("Opiskelijatiedot: ")
    tehtava_data = input("Tehtävätiedot: ")
else:
    opiskelija_info = "opiskelijat1.csv"
    tehtava_data = "tehtavat1.csv"

opiskelija = lue_tiedosto(opiskelija_info)
tehtava = lue_tiedosto(tehtava_data)
tulosta_piste(opiskelija,tehtava)