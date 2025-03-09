import sqlite3

# Prisijungiame prie SQLite duomenų bazės (arba sukuriame naują, jei tokios nėra)
conn = sqlite3.connect("mokykla.db")
cursor = conn.cursor()

# Sukuriame lentelę, jei ji dar neegzistuoja
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mokykla (
        pavadinimas TEXT,
        adresas TEXT,
        mokiniu_skaicius INTEGER
    )
''')

# Išsaugome pakeitimus ir uždarome ryšį
conn.commit()
conn.close()

print("Lentelė 'mokykla' sėkmingai sukurta arba jau egzistuoja.")
