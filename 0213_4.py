import sqlite3

conn = sqlite3.connect("mokykla.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mokykla (
        pavadinimas TEXT,
        adresas TEXT,
        mokiniu_skaicius INTEGER
    )
''')
conn.commit()


def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    try:
        conn = sqlite3.connect("mokykla.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?, ?, ?)",
                       (pavadinimas, adresas, mokiniu_skaicius))
        conn.commit()
        print(f"Mokykla '{pavadinimas}' pridėta sėkmingai.")
    except sqlite3.Error as e:
        print("Klaida įterpiant duomenis:", e)
    finally:
        conn.close()

prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)


def gauti_visas_mokyklas(min_mokiniu_skaicius=0):
    try:
        conn = sqlite3.connect("mokykla.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mokykla WHERE mokiniu_skaicius > ?", (min_mokiniu_skaicius,))
        mokyklos = cursor.fetchall()

        if mokyklos:
            for mokykla in mokyklos:
                print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokinių skaičius: {mokykla[2]}")
        else:
            print("Nėra mokyklų atitinkančių kriterijus.")
    except sqlite3.Error as e:
        print("Klaida skaitant duomenis:", e)
    finally:
        conn.close()

print("\nVisos mokyklos:")
gauti_visas_mokyklas()
print("\nMokyklos su daugiau nei 600 mokinių:")
gauti_visas_mokyklas(600)
