class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas, self.amzius = vardas, amzius

    def __str__(self):
        return f"👤 {self.vardas}, {self.amzius} metų"

class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos

    def __str__(self):
        return f"👔 {self.vardas}, {self.amzius} metų – {self.pareigos}"

darbuotojas = Darbuotojas("Jonas", 35, "Inžinierius")
print(darbuotojas)

class TransportoPriemone:
    def judeti(self):
        print("🚗 Transporto priemonė juda.")

class Dviratis(TransportoPriemone):
    def judeti(self):
        print("🚴‍♂️ Dviratis važiuoja pedalais.")

# Sukuriame objektus ir patikriname metodų veikimą
auto = TransportoPriemone()
dviratis = Dviratis()

auto.judeti()
dviratis.judeti()
