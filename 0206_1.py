class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas, self.amzius = vardas, amzius

    def judeti(self):
        print(f"🐾 {self.vardas} ({self.amzius} m.) juda!")

class Kate(Gyvunas):
    def miaukseti(self):
        print(f"😺 {self.vardas} ({self.amzius} m.) sako MIAU!")

class Suo(Gyvunas):
    def loti(self):
        print(f"🐶 {self.vardas} ({self.amzius} m.) sako AU AU!")

kate = Kate("Murka", 3)
suo = Suo("Rikis", 5)

kate.judeti()
kate.miaukseti()

suo.judeti()
suo.loti()
