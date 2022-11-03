# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
 
vase = 1
oike = luku
 
while vase < oike:
    print(vase)
    print(oike)
    vase += 1
    oike -= 1
 
if vase == oike:
    print(vase)