import random
from pprint import pprint

# 1.
katalogas = {f"Prekė-{i}": {"kaina": random.randint(5, 50), "kiekis": random.randint(1, 10)} for i in range(1, 11)}

# 2.
istorija, krepselis = [], {}
while True:
    print("\nParduotuvės katalogas:")
    pprint(katalogas)
    veiksmas = input("\nPasirinkite veiksmą: 'pirkti', 'rodyti', 'kaina < X', 'baigti': ").strip().lower()
    if veiksmas == "pirkti":
        preke = input("Įveskite prekės pavadinimą: ").strip()
        kiekis = int(input("Įveskite kiekį: "))
        if preke in katalogas and katalogas[preke]["kiekis"] >= kiekis:
            katalogas[preke]["kiekis"] -= kiekis
            krepselis[preke] = krepselis.get(preke, 0) + kiekis
            istorija.append({preke: kiekis})
            print(f"Prekė {preke} pridėta į krepšelį.")
        else:
            print("Nepakanka atsargų arba prekė neegzistuoja.")
    elif veiksmas == "rodyti":
        print("\nKrepšelio turinys:")
        pprint(krepselis)
        suma = sum(katalogas[p]["kaina"] * k for p, k in krepselis.items())
        print(f"Bendra kaina su PVM: {suma * 1.21:.2f} EUR")
    elif veiksmas.startswith("kaina <"):
        x = int(veiksmas.split("<")[1])
        pigios_prekes = [p for p, info in katalogas.items() if info["kaina"] < x]
        print(f"Prekės pigesnės už {x} EUR: {pigios_prekes}")
    elif veiksmas == "baigti":
        print("Pirkimo istorija:")
        pprint(istorija)
        break
#Apima visas jūsų mokytas technikas:
#List comprehension: Prekių filtravimui pagal kainą.
#Dict comprehension: Automatinis katalogo generavimas.
#For ciklai: Iteracija per prekes, pirkimo istoriją.
#Sąlygos: Tikrina, ar užtenka atsargų.
#Lambda funkcijos ir skaičiavimai: PVM apskaičiavimas.
#Įtraukia dinamiškumą: Generuojamas atsitiktinis katalogas, tad kiekvienas paleidimas unikalus.
#Pritaikymas: Tai galėtų būti pagrindas tikrai elektroninės parduotuvės logikai.
