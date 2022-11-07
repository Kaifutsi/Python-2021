# tee ratkaisu tänne
def palindromi(string):
    return string == string[::-1]

def main():
    while True:
        sana = input("Anna palindromi: ")
        if palindromi(sana):
            print(f"{sana} on palindromi!")
            break
        print("ei ollut palindromi")
main()
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
