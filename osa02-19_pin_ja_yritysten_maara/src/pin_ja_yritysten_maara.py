# Kirjoita ratkaisu tähän
yri = 0
while True:
    pin = int(input("PIN-koodi: "))
    yri += 1
    if pin == 4321:
        break
    print("Väärin")
if yri == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yri} yritystä")