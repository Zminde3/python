# 2. Patikrinti sezoną
#metu_laikas = input("Įveskite metų laiką (žiema, pavasaris, vasara, ruduo): ").lower()

#if metu_laikas == "žiema":
 #   print("Žiemos mėnesiai: Gruodis, Sausis, Vasaris")
#elif metu_laikas == "pavasaris":
 #   print("Pavasario mėnesiai: Kovas, Balandis, Gegužė")
#elif metu_laikas == "vasara":
 #   print("Vasaros mėnesiai: Birželis, Liepa, Rugpjūtis")
#elif metu_laikas == "ruduo":
 #   print("Rudens mėnesiai: Rugsėjis, Spalis, Lapkritis")
#else:
 #   print("Klaida: Įveskite vieną iš šių metų laikų – žiema, pavasaris, vasara, ruduo.")

# Skaičių tikrinimas
skaicius1 = float(input("Įveskite pirmą skaičių: "))
skaicius2 = float(input("Įveskite antrą skaičių: "))

if skaicius1 > 0 and skaicius2 > 0:
    print("Abu skaičiai yra teigiami.")
else:
    print("Ne abu skaičiai yra teigiami.")

if skaicius1 < 0 or skaicius2 < 0:
    print("Bent vienas iš skaičių yra neigiamas.")
else:
    print("Nei vienas skaičius nėra neigiamas.")

    # Automobilio tikrinimas
    vokiskos_markes = ["bmw", "audi", "mercedes-benz", "volkswagen"]
    sportiniai_modeliai = ["m3", "rs6", "amg gt", "golf r"]

    # Vartotojo įvedimas
    marke = input("Įveskite automobilio markę: ").strip().lower()
    modelis = input("Įveskite automobilio modelį: ").strip().lower()

    # 1. Tikrina, ar markė yra vok.
    if marke in vokiskos_markes:
        print(f"Markė {marke.upper()} yra vokiška.")
    else:
        print(f"Markė {marke.upper()} nėra vokiška.")

    # 2. Tikrina, ar model. yra sport.
    if modelis in sportiniai_modeliai:
        print(f"Modelis {modelis.upper()} yra sportinis.")
    else:
        print(f"Modelis {modelis.upper()} nėra sportinis.")


