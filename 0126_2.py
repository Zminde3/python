import pprint
from katalogas import kvepalu_katalogas

# Funkcija atvaizduoti
def spausdinti_kataloga(katalogas):
    print("\nParduotuvės katalogas:")
    print("-" * 50)
    for id, info in katalogas.items():
        print(f"{id}:")
        print(f"  Pavadinimas: {info['pavad.']}")
        print(f"  Kaina: {info['kaina']} EUR (su PVM)")
        print(f"  Likutis: {info['likutis']} vnt.")
        print("-" * 50)

# Krepšelis
def rodyti_krepseli(krepselis, katalogas):
    print("\nKrepšelio turinys:")
    print("-" * 50)
    bendra_suma_be_pvm = 0
    bendra_suma_su_pvm = 0
    bendra_pvm = 0
    for id, kiekis in krepselis.items():
        preke = katalogas[id]
        kaina_be_pvm = preke["kaina"] / 1.21
        suma_be_pvm = kaina_be_pvm * kiekis
        suma_su_pvm = preke["kaina"] * kiekis
        pvm = suma_su_pvm - suma_be_pvm
        bendra_suma_be_pvm += suma_be_pvm
        bendra_suma_su_pvm += suma_su_pvm
        bendra_pvm += pvm
        print(f"{id} - {preke['pavad.']}: {kiekis} vnt., {suma_be_pvm:.2f} EUR (be PVM), {pvm:.2f} EUR (PVM), {suma_su_pvm:.2f} EUR (su PVM)")
    print("-" * 50)
    print(f"Bendra suma (be PVM): {bendra_suma_be_pvm:.2f} EUR")
    print(f"Bendra PVM suma: {bendra_pvm:.2f} EUR")
    print(f"Bendra suma (su PVM): {bendra_suma_su_pvm:.2f} EUR")
    print("-" * 50)

# Parduotuvė
istorija, krepselis = [], {}

while True:
    print("\nKomandos: 'pirkti', 'rodyti', 'baigti'")
    veiksmas = input("Pasirinkite veiksmą: ").strip().lower()
    if veiksmas == "pirkti":
        print("\nPasirinkite prekes ir jų kiekius.")
        spausdinti_kataloga(kvepalu_katalogas)
        while True:
            preke_nr = input("Įveskite prekės numerį (arba 'stop' baigti): ").strip()
            if preke_nr == "stop":
                break
            preke = f"Prekė-{preke_nr.zfill(2)}"
            if preke not in kvepalu_katalogas:
                print("Tokios prekės nėra.")
                continue
            kiekis = int(input(f"Kiek norite įsigyti ({preke}): "))
            if kvepalu_katalogas[preke]["likutis"] < kiekis:
                print("Nepakanka likučio.")
                continue
            kvepalu_katalogas[preke]["likutis"] -= kiekis
            krepselis[preke] = krepselis.get(preke, 0) + kiekis
            print(f"Prekė {kvepalu_katalogas[preke]['pavad.']} pridėta į krepšelį.")
    elif veiksmas == "rodyti":
        rodyti_krepseli(krepselis, kvepalu_katalogas)
    elif veiksmas == "baigti":
        print("\nParduotuvės likučiai:")
        spausdinti_kataloga(kvepalu_katalogas)
        print("\nAčiū, kad apsipirkote!")
        break
