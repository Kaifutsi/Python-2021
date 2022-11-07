# Kirjoita ratkaisu tähän
def koe_harj_suori(luku):
    empty = luku.find(" ")
    koe = int(luku[:empty])
    harjoitus = int(luku[empty+1:])
    return [koe, harjoitus]
 
def harjoitus_pisteet(maara):
    return maara // 10
 
def arvosana(pisteet):
    raja = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if pisteet >= raja[i]:
            return i
 
def keski(pisteet):
    return sum(pisteet) / len(pisteet)
 
def main():
    pisteet = []
    arvosanat = [0] * 6
    while True:
        luku = input("Koepisteet ja harjoitusten määrä: ")
        if len(luku) == 0:
            break
 
        koe_and_harjoi = koe_harj_suori(luku)
        harj_pisteet = harjoitus_pisteet(koe_and_harjoi[1])
        yht_pisteet = koe_and_harjoi[0] + harj_pisteet
 
        pisteet.append(yht_pisteet)
        arvo = arvosana(yht_pisteet)
        if koe_and_harjoi[0] < 10:
            arvo = 0
        arvosanat[arvo] += 1
 
    lap_pros = 100 * (len(pisteet) - arvosanat[0]) / len(pisteet)
 
    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {keski(pisteet):.1f}")
    print(f"Hyväksymisprosentti: {lap_pros:.1f}")
    print("Arvosanajakauma:")
    for i in range(5, -1, -1):
        tahdet = "*" * arvosanat[i]
        print(f"  {i}: {tahdet}")
 
main()