class Matematika:
    @staticmethod
    def sudeti(a, b): return a + b

    @staticmethod
    def atimti(a, b): return a - b

    @staticmethod
    def dauginti(a, b): return a * b

    @staticmethod
    def dalinti(a, b): return a / b if b else "Klaida: dalyba iš nulio"

    @staticmethod
    def ar_lyginis(skaicius): return skaicius % 2 == 0


class Automobilis:
    def __init__(self, marke, modelis, metai):
        self.marke, self.modelis, self.metai = marke, modelis, int(metai)

    @classmethod
    def sukurti_is_string(cls, tekstas):
        *marke_modelis, metai = tekstas.rsplit(" ", 1)
        return cls(" ".join(marke_modelis), "", int(metai))

    @classmethod
    def naujausias_modelis(cls, auto_sarasas):
        return max(auto_sarasas, key=lambda auto: auto.metai)

print(Matematika.sudeti(5, 3))
print(Matematika.atimti(10, 4))
print(Matematika.dauginti(6, 7))
print(Matematika.dalinti(10, 2))
print(Matematika.dalinti(10, 0))
print(Matematika.ar_lyginis(8))

auto1 = Automobilis.sukurti_is_string("BMW 535 i xdrive 2020")
auto2 = Automobilis.sukurti_is_string("Audi A6 Quattro 2022")
auto3 = Automobilis.sukurti_is_string("Mercedes-Benz E220 2019")

print(auto1.marke, auto1.modelis, auto1.metai)
naujausias = Automobilis.naujausias_modelis([auto1, auto2, auto3])
print(f"Naujausias automobilis: {naujausias.marke} {naujausias.modelis} {naujausias.metai}")
