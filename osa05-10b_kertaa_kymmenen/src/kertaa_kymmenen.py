# tee ratkaisu tänne
def kertaa_kymmenen(alku: int, loppu: int):
    sanasto = {}
    for i in range(alku, loppu + 1):
        sanasto[i] = i * 10
    
    return sanasto


if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)