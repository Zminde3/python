import sqlite3


def log_operacija(funkcija):
    def vidine(*args, **kwargs):
        print(f"Vykdoma operacija: {funkcija.__name__}")
        rezultatas = funkcija(*args, **kwargs)
        print(f"Operacija '{funkcija.__name__}' baigta.")
        return rezultatas

    return vidine


class MokyklaDB:
    def __init__(self):
        self.conn = sqlite3.connect("mokykla.db")
        self.cursor = self.conn.cursor()
        self.sukurti_lentes()

    def sukurti_lentes(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS mokiniai (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            vardas TEXT, pavarde TEXT, klase TEXT, vidurkis REAL)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS mokytojai (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            vardas TEXT, pavarde TEXT, dalykas TEXT)""")
        self.conn.commit()

    @log_operacija
    def prideti_mokini(self, vardas, pavarde, klase, vidurkis):
        try:
            self.cursor.execute("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)",
                                (vardas, pavarde, klase, vidurkis))
            self.conn.commit()
            print("✅ Mokinys pridėtas sėkmingai.")
        except sqlite3.Error as e:
            print("❌ Klaida įrašant mokinį:", e)

    @log_operacija
    def prideti_mokytoja(self, vardas, pavarde, dalykas):
        try:
            self.cursor.execute("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)",
                                (vardas, pavarde, dalykas))
            self.conn.commit()
            print("✅ Mokytojas pridėtas sėkmingai.")
        except sqlite3.Error as e:
            print("❌ Klaida įrašant mokytoją:", e)

    @log_operacija
    def gauti_mokinius(self):
        self.cursor.execute("SELECT * FROM mokiniai")
        mokiniai = self.cursor.fetchall()
        print(f"🔍 Rasta mokinių: {len(mokiniai)}")
        return mokiniai

    @log_operacija
    def ieskoti_mokinio(self, vardas):
        self.cursor.execute("SELECT * FROM mokiniai WHERE vardas LIKE ?", (vardas + '%',))
        rezultatai = self.cursor.fetchall()
        print(f"🔍 Rasta {len(rezultatai)} atitikčių.")
        return rezultatai

    @log_operacija
    def atnaujinti_mokinio_klase(self, mokinio_id, nauja_klase):
        self.cursor.execute("UPDATE mokiniai SET klase = ? WHERE id = ?", (nauja_klase, mokinio_id))
        self.conn.commit()
        print("✅ Mokinio klasė atnaujinta.")

    @log_operacija
    def trinti_mokini(self, mokinio_id):
        self.cursor.execute("DELETE FROM mokiniai WHERE id = ?", (mokinio_id,))
        self.conn.commit()
        print("✅ Mokinys pašalintas.")


class MokiniaiIteratorius:
    def __init__(self, mokiniai):
        self.mokiniai = mokiniai
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.mokiniai):
            raise StopIteration
        mokinys = self.mokiniai[self.index]
        self.index += 1
        return mokinys

if __name__ == "__main__":
    db = MokyklaDB()
    vykdyti = True
    while vykdyti:
        print("\n1. Pridėti mokinį")
        print("2. Pridėti mokytoją")
        print("3. Peržiūrėti visus mokinius")
        print("4. Ieškoti mokinio pagal vardą")
        print("5. Atnaujinti mokinio klasę")
        print("6. Ištrinti mokinį")
        print("7. Išeiti")
        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == "1":
            v = input("Vardas: ")
            p = input("Pavardė: ")
            k = input("Klasė: ")
            while True:
                try:
                    vid = float(input("Vidurkis (naudok tašką vietoje kablelio): ").replace(",", "."))
                    break
                except ValueError:
                    print("❌ Klaida: Įveskite tinkamą skaičių naudodami tašką vietoje kablelio.")
            db.prideti_mokini(v, p, k, vid)
        elif pasirinkimas == "2":
            v = input("Vardas: ")
            p = input("Pavardė: ")
            d = input("Dalykas: ")
            db.prideti_mokytoja(v, p, d)
        elif pasirinkimas == "3":
            for m in MokiniaiIteratorius(db.gauti_mokinius()):
                print(f"Mokinys: {m}")
        elif pasirinkimas == "4":
            v = input("Įveskite vardą: ")
            print(db.ieskoti_mokinio(v))
        elif pasirinkimas == "5":
            id = int(input("Mokinio ID: "))
            nauja_kl = input("Nauja klasė: ")
            db.atnaujinti_mokinio_klase(id, nauja_kl)
        elif pasirinkimas == "6":
            id = int(input("Mokinio ID: "))
            db.trinti_mokini(id)
        elif pasirinkimas == "7":
            vykdyti = False
        else:
            print("❌ Neteisingas pasirinkimas!")
