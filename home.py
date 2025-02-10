import pickle

class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def prisistatyti(self):
        return f"Aš esu {self.vardas} {self.pavarde}."

class Studentas(Zmogus):
    def __init__(self, vardas, pavarde, programa):
        super().__init__(vardas, pavarde)
        self.programa = programa

    def prisistatyti(self):
        return f"Aš esu {self.vardas} {self.pavarde}, studijuoju {self.programa}."

class Universitetas:
    def __init__(self):
        self.studentai = []

    def prideti_studenta(self, studentas):
        self.studentai.append(studentas)

    def rodyti_visus_studentus(self):
        for studentas in self.studentai:
            print(studentas.prisistatyti())

class Knyga:
    def __init__(self, pavadinimas, autorius, metai):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai

class Biblioteka:
    def __init__(self, failas='biblioteka.pkl'):
        self.failas = failas
        self.knygos = self.uzkrauti_knygas()

    def prideti_knyga(self, knyga):
        self.knygos.append(knyga)
        self.issaugoti_knygas()

    def istrinti_knyga(self, pavadinimas):
        self.knygos = [k for k in self.knygos if k.pavadinimas != pavadinimas]
        self.issaugoti_knygas()

    def rodyti_knygas(self):
        for knyga in self.knygos:
            print(f"{knyga.pavadinimas}, {knyga.autorius}, {knyga.metai}")

    def paieska(self, raktas):
        return [k for k in self.knygos if raktas.lower() in k.pavadinimas.lower() or raktas.lower() in k.autorius.lower()]

    def issaugoti_knygas(self):
        with open(self.failas, 'wb') as f:
            pickle.dump(self.knygos, f)

    def uzkrauti_knygas(self):
        try:
            with open(self.failas, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

# Testavimas
uni = Universitetas()
uni.prideti_studenta(Studentas("Jonas", "Jonaitis", "Informatika"))
uni.prideti_studenta(Studentas("Ona", "Onaite", "Ekonomika"))
print("Universiteto studentai:")
uni.rodyti_visus_studentus()

biblioteka = Biblioteka()
biblioteka.prideti_knyga(Knyga("Python", "Autorius A", 2020))
biblioteka.prideti_knyga(Knyga("Ekonomika", "Autorius B", 2018))
print("\nBibliotekoje esančios knygos:")
biblioteka.rodyti_knygas()

paieskos_rez = biblioteka.paieska("Python")
print("\nPaieškos rezultatai:")
for knyga in paieskos_rez:
    print(f"{knyga.pavadinimas}, {knyga.autorius}, {knyga.metai}")
