# class Variklis:
#     def __init__(self, galia):
#         self.galia = galia
#
#     def startuoti(self):
#         print(f"🔧 Variklis veikia su galia: {self.galia} arklio galių.")
#
# class Automobilis:
#     def __init__(self, marke, modelis, variklis):
#         self.marke, self.modelis, self.variklis = marke, modelis, variklis
#
#     def vaziuoti(self):
#         print(f"🚗 {self.marke} {self.modelis} pradeda važiuoti...")
#         self.variklis.startuoti()
#
# variklis1 = Variklis(150)
# variklis2 = Variklis(300)
#
# auto1 = Automobilis("Toyota", "Verso", variklis1)
# auto2 = Automobilis("BMW", "535 X", variklis2)
#
# auto1.vaziuoti()
# auto2.vaziuoti()

class Variklis:
    def __init__(self, galia, kuro_tipas):
        self.galia = galia
        self.kuro_tipas = kuro_tipas

    def startuoti(self):
        print(f"🔧 Variklis ({self.kuro_tipas}) įjungtas su galia: {self.galia} AG.")

class Automobilis:
    def __init__(self, marke, modelis, variklis, kuro_kiekis=50):
        self.marke, self.modelis, self.variklis = marke, modelis, variklis
        self.kuro_kiekis = kuro_kiekis
        self.greitis = 0

    def vaziuoti(self):
        if self.kuro_kiekis > 0:
            print(f"🚗 {self.marke} {self.modelis} pradeda važiuoti...")
            self.variklis.startuoti()
            self.greitis = 20  # Pradinė greičio reikšmė
            self.kuro_kiekis -= 5  # Važiavimas mažina kuro kiekį
        else:
            print(f"⛽ {self.marke} {self.modelis} negali važiuoti – nėra kuro!")

    def pagreitis(self, kiek):
        kuro_sunaudojimas = kiek // 5  # Kuro sąnaudos priklauso nuo greičio
        if self.kuro_kiekis >= kuro_sunaudojimas:
            self.greitis += kiek
            self.kuro_kiekis -= kuro_sunaudojimas
            print(f"🚀 {self.marke} {self.modelis} įsibėgėja iki {self.greitis} km/h! Likęs kuras: {self.kuro_kiekis}L")
        else:
            print(f"⛽ {self.marke} {self.modelis} negali pagreitėti – trūksta kuro! Likęs kuras: {self.kuro_kiekis}L")

    def stabdyti(self):
        if self.greitis > 0:
            print(f"🛑 {self.marke} {self.modelis} sustoja nuo {self.greitis} km/h.")
            self.greitis = 0
        else:
            print(f"🚘 {self.marke} {self.modelis} jau sustojęs.")

    def pildyti_kura(self, kiekis):
        self.kuro_kiekis += kiekis
        print(f"⛽ {self.marke} {self.modelis} pripilta {kiekis}L kuro. Dabar yra {self.kuro_kiekis}L.")

# Sukuriame skirtingus variklius
variklis1 = Variklis(150, "Benzinas")
variklis2 = Variklis(300, "Dyzelinas")

# Sukuriame automobilius su skirtingais varikliais
auto1 = Automobilis("Toyota", "Verso", variklis1, kuro_kiekis=10)
auto2 = Automobilis("BMW", "535 X", variklis2, kuro_kiekis=30)

# Išbandome veikimą
auto1.vaziuoti()
auto1.pagreitis(30)  # Kuro nepakaks pagreitėjimui
auto1.stabdyti()
auto1.pildyti_kura(20)
auto1.vaziuoti()
auto1.pagreitis(50)  # Dabar kuro pakaks

print("\n")

auto2.vaziuoti()
auto2.pagreitis(60)
auto2.stabdyti()
