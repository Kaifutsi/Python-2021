# Kirjoita ratkaisu tähän
kerta = int(input("Montako kertaa viikossa syöt Unicafessa? "))
hinta = float(input("Unicafe-lounaan hinta? "))
ruoka = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

Päivässä = (kerta * hinta + ruoka) / 7
Viikossa = kerta * hinta + ruoka

print("Kustannukset keskimäärin:")
print(f"Päivässä {Päivässä} euroa")
print(f"Viikossa {Viikossa} euroa")