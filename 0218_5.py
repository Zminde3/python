import sqlite3
import logging
import unittest
from colorama import Fore, Style, init

# Inicijuojame colorama (tik Windows)
init(autoreset=True)

# Logging konfigūracija
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_colored(level, message):
    colors = {
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED
    }
    print(f"{colors.get(level, '')}{level}: {message}{Style.RESET_ALL}")

# 1. Saugi ir optimizuota duomenų bazės valdymo klasė
class DatabaseManager:
    def __init__(self, db_name='mokykla_test.db'):
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
                    klase INTEGER NOT NULL,
                    vidurkis REAL CHECK (vidurkis BETWEEN 1 AND 10)
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
            log_colored('ERROR', f'SQLite klaida: {e}')
            return None

db = DatabaseManager()

# Dekoratorius funkcijų registracijai
def log_dekoratorius(func):
    def wrapper(*args, **kwargs):
        log_colored('INFO', f'Vykdoma operacija: {func.__name__} su parametrais {args[1:]}')
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            log_colored('ERROR', f'Klaida vykdant {func.__name__}: {e}')
        except ValueError as e:
            log_colored('WARNING', f'Netinkami duomenys: {e}')
    return wrapper

@log_dekoratorius
def rikiuoti_mokinius_pagal_klase():
    return db.execute_query("SELECT klase FROM mokiniai ORDER BY klase ASC", fetchall=True)

@log_dekoratorius
def skaiciuoti_mokiniu_kiekvienoje_klaseje():
    return db.execute_query("SELECT klase, COUNT(*) FROM mokiniai GROUP BY klase", fetchall=True)

@log_dekoratorius
def vidutinis_mokiniu_skaicius():
    result = db.execute_query("SELECT COUNT(*) * 1.0 / COUNT(DISTINCT klase) FROM mokiniai", fetchone=True)
    return round(result[0], 1) if result else 0

# Testavimo klasė
class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager('mokykla_test.db')
        self.db.execute_query("DELETE FROM mokiniai")

    def test_rikiuoti_mokinius_pagal_klase(self):
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Mindaugas', 'Bernotas', 8, 8.5)")
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Tomas', 'Matukas', 9, 9.0)")
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Gabija', 'Barauskaitė', 10, 9.5)")
        result = [row[0] for row in rikiuoti_mokinius_pagal_klase()]
        self.assertEqual(result, [8, 9, 10])  # Patikriname visą seką vietoj vieno įrašo

    def test_skaiciuoti_mokiniu_kiekvienoje_klaseje(self):
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Mindaugas', 'Bernotas', 10, 8.5)")
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Tomas', 'Matukas', 10, 9.0)")
        result = skaiciuoti_mokiniu_kiekvienoje_klaseje()
        self.assertEqual(result[0][1], 2)

    def test_vidutinis_mokiniu_skaicius(self):
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Mindaugas', 'Bernotas', 8, 8.5)")
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Tomas', 'Matukas', 9, 9.0)")
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Sergej', 'Purikov', 10, 7.5)")
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES ('Gabija', 'Barauskaitė', 10, 9.5)")
        result = vidutinis_mokiniu_skaicius()
        self.assertAlmostEqual(result, 1.5, places=1)

if __name__ == "__main__":
    unittest.main()
