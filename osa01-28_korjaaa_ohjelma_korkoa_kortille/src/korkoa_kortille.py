# Korjaa ohjelma
pisteet = int(input("Kuinka paljon pisteitä? "))
if pisteet < 100:
    tulo=pisteet * 1.1
    print("Sait 10 % bonusta")

if pisteet >= 100:
    tulo=pisteet * 1.15
    print("Sait 15 % bonusta")

print(f"Pisteitä on nyt", {tulo})

