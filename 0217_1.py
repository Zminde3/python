import sqlite3
import logging

# Konfigūruojame logavimą
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
                conn.commit()
                return cursor.fetchone() if fetchone else cursor.fetchall() if fetchall else None
        except sqlite3.Error as e:
            logging.error(f'SQL klaida: {e}')
            return None

db = DatabaseManager()

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas.title()
        self.pavarde = pavarde.title()


class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase.upper()
        self.vidurkis = round(vidurkis, 2)

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Klasė: {self.klase}, Vidurkis: {self.vidurkis:.2f}"


class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas.title()

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Dėsto: {self.dalykas}"

def log_dekoratorius(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(arg) if not isinstance(arg, (list, tuple, dict)) else repr(arg) for arg in args)
        logging.info(f'Vykdoma operacija: {func.__name__} su parametrais ({args_str})')
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Klaida vykdant {func.__name__}: {e}')
    return wrapper

@log_dekoratorius
def prideti_mokini(mokinys):
    db.execute_query(
        'INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)',
        (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis)
    )

@log_dekoratorius
def perziureti_visus_mokinius():
    mokiniai = db.execute_query('SELECT id, vardas, pavarde, klase, vidurkis FROM mokiniai', fetchall=True)
    if mokiniai:
        for mokinys in mokiniai:
            print(f'ID: {mokinys[0]}, {mokinys[1]} {mokinys[2]}, Klasė: {mokinys[3]}, Vidurkis: {mokinys[4]:.2f}')
    else:
        print('Mokinių sąrašas tuščias.')

@log_dekoratorius
def atnaujinti_mokinio_duomenis(mokinys_id, klase=None, vidurkis=None):
    if klase:
        db.execute_query('UPDATE mokiniai SET klase = ? WHERE id = ?', (klase.upper(), mokinys_id))
    if vidurkis is not None:
        db.execute_query('UPDATE mokiniai SET vidurkis = ? WHERE id = ?', (round(vidurkis, 2), mokinys_id))


@log_dekoratorius
def istrinti_mokini(mokinys_id):
    db.execute_query('DELETE FROM mokiniai WHERE id = ?', (mokinys_id,))


@log_dekoratorius
def ieskoti_mokinio(vardas, pavarde):
    return db.execute_query(
        'SELECT id, vardas, pavarde, klase, vidurkis FROM mokiniai WHERE vardas = ? AND pavarde = ?',
        (vardas.title(), pavarde.title()), fetchall=True
    )


def pasirinkti_veiksma():
    veiksmai = {
        '1': lambda: prideti_mokini(Mokinys(
            input('Mokinio vardas: '), input('Mokinio pavardė: '),
            input('Mokinio klasė: '), float(input('Mokinio vidurkis: '))
        )),
        '2': perziureti_visus_mokinius,
        '3': lambda: atnaujinti_mokinio_duomenis(
            int(input('Mokinio ID: ')),
            input('Nauja klasė (palikite tuščią, jei nekeisite): ') or None,
            float(input('Naujas vidurkis (palikite tuščią, jei nekeisite): ') or 0) or None
        ),
        '4': lambda: istrinti_mokini(int(input('Mokinio ID: '))),
        '5': lambda: ieskoti_mokinio(input('Mokinio vardas: '), input('Mokinio pavardė: ')),
        '6': exit
    }

    while True:
        print('\nMokyklos duomenų valdymo sistema')
        print('1. Pridėti mokinį')
        print('2. Peržiūrėti visus mokinius')
        print('3. Atnaujinti mokinio duomenis')
        print('4. Ištrinti mokinį')
        print('5. Ieškoti mokinio')
        print('6. Išeiti')
        pasirinkimas = input('Pasirinkite veiksmą: ')
        veiksmai.get(pasirinkimas, lambda: print('Neteisingas pasirinkimas!'))()


pasirinkti_veiksma()
