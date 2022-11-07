# tee ratkaisu tänne
def eniten_kirjainta(merkkijono: str):
    en_kir = merkkijono[0]
    for merkki in merkkijono:
        if merkkijono.count(merkki) > merkkijono.count(en_kir):
            en_kir = merkki
 
    return en_kir
    

if __name__ == "__main__":
    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))