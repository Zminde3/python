import sqlite3
import hashlib


# Prisijungiame prie duomenų bazės ir sukuriame lentelę, jei jos nėra
def sukurti_duombaze():
    conn = sqlite3.connect("saugus_duomenys.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vartotojai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vardas TEXT UNIQUE,
            slaptazodis TEXT,
            el_pastas TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()


# Slaptažodžio šifravimas su SHA-256
def sifruoti_slaptazodi(slaptazodis):
    return hashlib.sha256(slaptazodis.encode()).hexdigest()


# Vartotojo registracija
def registruoti_vartotoja(vardas, slaptazodis, el_pastas):
    sifruotas = sifruoti_slaptazodi(slaptazodis)
    conn = sqlite3.connect("saugus_duomenys.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO vartotojai (vardas, slaptazodis, el_pastas) VALUES (?, ?, ?)",
                       (vardas, sifruotas, el_pastas))
        conn.commit()
        print("Vartotojas sėkmingai užregistruotas!")
    except sqlite3.IntegrityError:
        print("Klaida: toks vartotojas jau egzistuoja arba el. paštas naudojamas.")
    finally:
        conn.close()


# Prisijungimas prie sistemos
def prisijungti(vardas, slaptazodis):
    sifruotas = sifruoti_slaptazodi(slaptazodis)
    conn = sqlite3.connect("saugus_duomenys.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vartotojai WHERE vardas = ? AND slaptazodis = ?", (vardas, sifruotas))
    vartotojas = cursor.fetchone()
    conn.close()

    if vartotojas:
        print("Prisijungimas sėkmingas! Sveiki,", vardas)
    else:
        print("Neteisingas vardas arba slaptažodis.")


# Testavimas
sukurti_duombaze()
registruoti_vartotoja("Jonas", "slaptas123", "jonas@example.com")
prisijungti("Jonas", "slaptas123")
