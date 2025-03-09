import sqlite3
import logging

# Logging konfigūracija
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 1. Saugi ir optimizuota duomenų bazės valdymo klasė
class DatabaseManager:
    def __init__(self, db_name='mokykla.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.executescript('''
                CREATE TABLE IF NOT EXISTS mokiniai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT NOT NULL,
                    pavarde TEXT NOT NULL,
                    klase TEXT NOT NULL,
                    vidurkis REAL CHECK (vidurkis BETWEEN 1 AND 10)
                );

                CREATE TABLE IF NOT EXISTS mokytojai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT NOT NULL,
                    pavarde TEXT NOT NULL,
                    dalykas TEXT NOT NULL
                );
            ''')
            conn.commit()

    def execute_query(self, query, params=(), fetchone=False, fetchall=False):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                if fetchone:
                    return cursor.fetchone()
                if fetchall:
                    return cursor.fetchall()
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f'SQLite klaida: {e}')
            return None


db = DatabaseManager()


# 2. OOP klases su validacija
class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas.strip().title()
        self.pavarde = pavarde.strip().title()


class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase.strip().upper()
        self.vidurkis = self.validate_vidurkis(vidurkis)

    def validate_vidurkis(self, vidurkis):
        if 1 <= vidurkis <= 10:
            return round(vidurkis, 2)
        raise ValueError('Vidurkis turi būti tarp 1 ir 10!')

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Klasė: {self.klase}, Vidurkis: {self.vidurkis:.2f}"


class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas.strip().capitalize()

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Dėsto: {self.dalykas}"


# 3. Dekoratorius su logging
def log_dekoratorius(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Vykdoma operacija: {func.__name__} su parametrais {args[1:]}')
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            logging.error(f'Klaida vykdant {func.__name__}: {e}')
        except ValueError as e:
            logging.warning(f'Netinkami duomenys: {e}')

    return wrapper


# 4. Funkcijos duomenų valdymui
@log_dekoratorius
def prideti_mokini(mokinys):
    db.execute_query(
        'INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)',
        (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis)
    )


@log_dekoratorius
def prideti_mokytoja(mokytojas):
    db.execute_query(
        'INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)',
        (mokytojas.vardas, mokytojas.pavarde, mokytojas.dalykas)
    )


@log_dekoratorius
def istrinti_mokini(mokinys_id):
    db.execute_query('DELETE FROM mokiniai WHERE id = ?', (mokinys_id,))


@log_dekoratorius
def istrinti_mokytoja(mokytojas_id):
    db.execute_query('DELETE FROM mokytojai WHERE id = ?', (mokytojas_id,))


@log_dekoratorius
def istrinti_baigusius_mokinius():
    db.execute_query("DELETE FROM mokiniai WHERE klase = '12'")


@log_dekoratorius
def ieskoti_mokinio(vardas):
    return db.execute_query('SELECT * FROM mokiniai WHERE vardas = ?', (vardas.title(),), fetchall=True)


@log_dekoratorius
def mokiniai_pavarde_p():
    return db.execute_query("SELECT * FROM mokiniai WHERE pavarde LIKE 'P%'", fetchall=True)


@log_dekoratorius
def mokytojai_vardas_s():
    return db.execute_query("SELECT * FROM mokytojai WHERE vardas LIKE '%s'", fetchall=True)
