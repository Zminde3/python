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

# Testavimo klasė
class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager('mokykla_test.db')
        self.db.execute_query("DELETE FROM mokiniai")
        self.db.execute_query("DELETE FROM mokytojai")

    def test_istrinti_mokini(self):
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)", ('Test', 'Student', '10', 8.5))
        mokiniai = self.db.execute_query("SELECT id FROM mokiniai", fetchall=True)
        istrinti_mokini(mokiniai[0][0])
        self.assertEqual(len(self.db.execute_query("SELECT * FROM mokiniai", fetchall=True)), 0)

    def test_istrinti_mokytoja(self):
        self.db.execute_query("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)", ('Jonas', 'Petraitis', 'Matematika'))
        mokytojai = self.db.execute_query("SELECT id FROM mokytojai", fetchall=True)
        istrinti_mokytoja(mokytojai[0][0])
        self.assertEqual(len(self.db.execute_query("SELECT * FROM mokytojai", fetchall=True)), 0)

    def test_istrinti_baigusius_mokinius(self):
        self.db.execute_query("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)", ('Testas', 'Baiges', '12', 7.0))
        istrinti_baigusius_mokinius()
        self.assertEqual(len(self.db.execute_query("SELECT * FROM mokiniai", fetchall=True)), 0)

if __name__ == "__main__":
    unittest.main()
