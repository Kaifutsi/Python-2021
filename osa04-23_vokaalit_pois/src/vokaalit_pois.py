# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
    vokaalit = ["a","e","i","o","u","ö","ä","å","y"]
    sana = ""
    for i in mjono:
        if i in vokaalit:
            i = ""
        sana += i
    return sana



if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))