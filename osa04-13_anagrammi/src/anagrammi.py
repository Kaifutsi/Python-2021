# Tee ratkaisu tänne
def anagrammi(sana1 : str, sana2 : str):
    sorted1 = sorted(sana1)
    sorted2 = sorted(sana2) 
    if sorted1 == sorted2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("talo", "olat")) # True
    print(anagrammi("tammi", "mitta")) # False
    print(anagrammi("python", "java")) # False