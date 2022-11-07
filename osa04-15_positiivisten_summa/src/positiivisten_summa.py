# tee ratkaisu tänne
def positiivisten_summa(lista):
    sum = 0
    for i in lista:
        if i > 0:
            sum += i     
    return sum

if __name__ == "__main__":
    print("vastaus", positiivisten_summa([1, -2, 3, -4, 5]))