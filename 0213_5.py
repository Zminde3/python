import sqlite3

def vykdyti_uzklausa(uzklausa, duomenys=(), fetch=False):
    with sqlite3.connect("mokykla.db") as conn:
        cursor = conn.cursor()
        cursor.execute(uzklausa, duomenys)
        return cursor.fetchall() if fetch else conn.commit()

def sukurti_lentele():
    vykdyti_uzklausa("""
        CREATE TABLE IF NOT EXISTS mokykla (
            pavadinimas TEXT,
            adresas TEXT,
            mokiniu_skaicius INTEGER
        )
    """)

def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    vykdyti_uzklausa("INSERT INTO mokykla VALUES (?, ?, ?)", (pavadinimas, adresas, mokiniu_skaicius))

def gauti_mokyklas(min_mokiniu=0):
    return vykdyti_uzklausa("SELECT * FROM mokykla WHERE mokiniu_skaicius > ?", (min_mokiniu,), fetch=True)

sukurti_lentele()
prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)

for mokykla in gauti_mokyklas():
    print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokinių skaičius: {mokykla[2]}")

print("\nMokyklos su daugiau nei 600 mokinių:")
for mokykla in gauti_mokyklas(600):
    print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokinių skaičius: {mokykla[2]}")
