# tee ratkaisu tänne
def muotoile(lista):
    lista2 = []
    for i in lista:
        luku = "{:.2f}".format(i)
        lista2.append(luku)
    return lista2

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)