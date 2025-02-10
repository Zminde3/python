class Darbuotojas:

    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas, self.pavarde = vardas, pavarde
        self.__atlyginimas = max(atlyginimas, 500)

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas):
        self.__atlyginimas = max(naujas, 500)

    @property
    def mokesciai(self):
        return self.__atlyginimas * 0.2

    def __str__(self):
        return f"{self.vardas} {self.pavarde} | Atlyginimas: {self.atlyginimas}€ | Mokesčiai: {self.mokesciai:.2f}€"



d = Darbuotojas("Mindaugas", "Bernotaitis", 400)
print(d)

d.atlyginimas = 1000
print(d)

d.atlyginimas = 300
print(d)
