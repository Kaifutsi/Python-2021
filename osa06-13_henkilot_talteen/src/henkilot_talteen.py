# tee ratkaisu tänne

def tallenna_henkilo(henkilo: tuple):
    with open('henkilot.csv', 'a') as file:
        henkilo_tiedot = []
        henkilo_tiedot.append(henkilo[0])
        henkilo_tiedot.append(str(henkilo[1]))
        henkilo_tiedot.append(str(henkilo[2]))
        line = ';'.join(henkilo_tiedot) + '\n'
        file.write(line)