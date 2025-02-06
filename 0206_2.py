class Variklis:
    def __init__(self, galia):
        self.galia = galia

    def startuoti(self):
        print(f"🔧 Variklis veikia su galia: {self.galia} arklio galių.")

class Automobilis:
    def __init__(self, marke, modelis, variklis):
        self.marke, self.modelis, self.variklis = marke, modelis, variklis

    def vaziuoti(self):
        print(f"🚗 {self.marke} {self.modelis} pradeda važiuoti...")
        self.variklis.startuoti()

variklis1 = Variklis(150)
variklis2 = Variklis(300)

auto1 = Automobilis("Toyota", "Verso", variklis1)
auto2 = Automobilis("BMW", "535 X", variklis2)

auto1.vaziuoti()
auto2.vaziuoti()
