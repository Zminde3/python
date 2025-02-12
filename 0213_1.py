import sqlite3

def log_operacija(funkcija):
    def vidine(*args, **kwargs):
        print(f"Vykdoma operacija: {funkcija.__name__}")
        return funkcija(*args, **kwargs)

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
        except sqlite3.Error as e:
            print("Klaida įrašant mokinį:", e)

    @log_operacija
    def prideti_mokytoja(self, vardas, pavarde, dalykas):
        try:
            self.cursor.execute("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)",
                                (vardas, pavarde, dalykas))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Klaida įrašant mokytoją:", e)

    @log_operacija
    def gauti_mokinius(self):
        self.cursor.execute("SELECT * FROM mokiniai")
        return self.cursor.fetchall()

    @log_operacija
    def ieskoti_mokinio(self, vardas):
        self.cursor.execute("SELECT * FROM mokiniai WHERE vardas LIKE ?", (vardas + '%',))
        return self.cursor.fetchall()

    @log_operacija
    def atnaujinti_mokinio_klase(self, mokinio_id, nauja_klase):
        self.cursor.execute("UPDATE mokiniai SET klase = ? WHERE id = ?", (nauja_klase, mokinio_id))
        self.conn.commit()

    @log_operacija
    def trinti_mokini(self, mokinio_id):
        self.cursor.execute("DELETE FROM mokiniai WHERE id = ?", (mokinio_id,))
        self.conn.commit()

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

def testuoti():
    db = MokyklaDB()
    db.prideti_mokini("Mindaugas", "Bernotas", "8A", 8.5)
    db.prideti_mokini("Tomas", "Matukas", "7B", 9.1)
    db.prideti_mokytoja("Dariuš", "Daškevičius", "Matematika")

    print("\nGauti visi mokiniai:")
    mokiniai = db.gauti_mokinius()
    for mokinys in MokiniaiIteratorius(mokiniai):
        print(f"Mokinys: {mokinys}")

    print("\nIeškome mokinio vardu 'Jonas':")
    print(db.ieskoti_mokinio("Jonas"))

    print("\nAtnaujiname pirmo mokinio klasę į '9A':")
    if mokiniai:
        db.atnaujinti_mokinio_klase(mokiniai[0][0], "9A")

    print("\nTriname pirmą mokinį ir tikriname sąrašą:")
    if mokiniai:
        db.trinti_mokini(mokiniai[0][0])
    mokiniai = db.gauti_mokinius()
    for mokinys in MokiniaiIteratorius(mokiniai):
        print(f"Mokinys: {mokinys}")


testuoti()
