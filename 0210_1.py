from datetime import date, timedelta
import pickle

class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10:
            self._pazymiai.append(pazymys)
        else:
            print("⚠️ Klaida: pažymys turi būti tarp 1 ir 10.")

    def rodyti_vidurki(self):
        return sum(self._pazymiai) / len(self._pazymiai) if self._pazymiai else 0

    def __str__(self):
        return f"🎓 {self.vardas} {self.pavarde} | Vidurkis: {self.rodyti_vidurki():.2f}"

class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonus=0):
        super().__init__(vardas, pavarde)
        self.bonus = bonus

    def rodyti_vidurki(self):
        return super().rodyti_vidurki() + self.bonus

    def __str__(self):
        return f"🏆 {self.vardas} {self.pavarde} | Vidurkis: {self.rodyti_vidurki():.2f}"

s1 = Studentas("Mindaugas", "Bernotas")
s1.prideti_pazymi(8)
s1.prideti_pazymi(9)
s1.prideti_pazymi(11)
print(s1)

s2 = StudentasLyderis("Anžela", "Bernotienė", bonus=0.5)
s2.prideti_pazymi(7)
s2.prideti_pazymi(8)
print(s2)

# --------------------------------------------------
class BankoSaskaita:
    def __init__(self, savininkas, pradinis_balansas=0):
        self.savininkas = savininkas
        self.__balansas = pradinis_balansas

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, kiek):
        if kiek < 0:
            print("⚠️ Klaida: negalima pridėti neigiamų pinigų!")
            return
        self.__balansas += kiek
        print(f"💰 Pridėta {kiek} EUR. Naujas balansas: {self.__balansas} EUR.")

    def nuskaičiuoti_pinigus(self, kiek):
        if kiek < 0:
            print("⚠️ Klaida: negalima nuskaičiuoti neigiamų pinigų!")
            return False
        if self.__balansas >= kiek:
            self.__balansas -= kiek
            print(f"✅ Nuskaičiuota {kiek} EUR. Naujas balansas: {self.__balansas} EUR.")
            return True
        print("⚠️ Klaida: nepakanka lėšų!")
        return False

    def __str__(self):
        return f"🏦 Sąskaita: {self.savininkas} | Balansas: {self.__balansas} EUR"

saskaita = BankoSaskaita("Mindaugas Bernotas", 100)
print(saskaita)
saskaita.prideti_pinigus(50)
saskaita.nuskaičiuoti_pinigus(30)
saskaita.nuskaičiuoti_pinigus(150)

# --------------------------------------------------
class Knyga:
    def __init__(self, pavadinimas, autorius, metai):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai

    def __str__(self):
        return f"📖 {self.pavadinimas} - {self.autorius} ({self.metai})"

class Biblioteka:
    def __init__(self, failas='biblioteka.pkl'):
        self.failas = failas
        self.knygos = self.uzkrauti_knygas()

    def prideti_knyga(self, knyga):
        self.knygos.append(knyga)
        self.issaugoti_knygas()
        print(f"📚 Knyga pridėta: {knyga}")

    def istrinti_knyga(self, pavadinimas):
        nauja_knygos = [k for k in self.knygos if k.pavadinimas.lower() != pavadinimas.lower()]
        if len(nauja_knygos) < len(self.knygos):
            self.knygos = nauja_knygos
            self.issaugoti_knygas()
            print(f"🗑️ Ištrinta knyga: {pavadinimas}")
        else:
            print(f"⚠️ Klaida: Knyga „{pavadinimas}“ nerasta!")

    def rodyti_knygas(self):
        print("\n📚 Bibliotekos knygos:")
        for knyga in self.knygos:
            print(knyga)

    def paieska(self, raktas):
        rezultatai = [k for k in self.knygos if raktas.lower() in k.pavadinimas.lower() or raktas.lower() in k.autorius.lower()]
        print("\n🔍 Paieškos rezultatai:")
        if rezultatai:
            for knyga in rezultatai:
                print(knyga)
        else:
            print("⚠️ Pagal šiuos kriterijus knygų nėra.")

    def issaugoti_knygas(self):
        with open(self.failas, 'wb') as f:
            pickle.dump(self.knygos, f)

    def uzkrauti_knygas(self):
        try:
            with open(self.failas, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

biblioteka = Biblioteka()
biblioteka.prideti_knyga(Knyga("Python", "Autorius A", 2020))
biblioteka.prideti_knyga(Knyga("Ekonomika", "Autorius B", 2018))
biblioteka.rodyti_knygas()
biblioteka.paieska("Python")
biblioteka.istrinti_knyga("Ekonomika")
biblioteka.rodyti_knygas()
