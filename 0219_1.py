import sqlite3

# Prisijungiame prie duomenų bazės
db_name = "gimnazija.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# 1. Sukuriame lentelę mokytojai
cursor.execute('''
CREATE TABLE IF NOT EXISTS mokytojai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vardas TEXT NOT NULL,
    pavarde TEXT NOT NULL,
    dalykas TEXT NOT NULL,
    atlyginimas INTEGER NOT NULL
);
''')
conn.commit()

# 2. Įrašome duomenis į mokytojų lentelę
data = [
    ('Jonas', 'Jonaitis', 'Matematika', 1800),
    ('Petras', 'Petraitis', 'Fizika', 1600),
    ('Lina', 'Linauskaitė', 'Chemija', 1400),
    ('Tomas', 'Tomaitis', 'Istorija', 2000),
    ('Agnė', 'Agnėnaitė', 'Anglų', 1700)
]
cursor.executemany("INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES (?, ?, ?, ?)", data)
conn.commit()

# 3. Atrenkame visus mokytojus ir pritaikome spalvas
print("\033[1;34m--- Visi mokytojai ---\033[0m")
cursor.execute("SELECT vardas, pavarde, dalykas, atlyginimas FROM mokytojai")
for row in cursor.fetchall():
    print(f"\033[31m{row[0]}\033[0m \033[32m{row[1]}\033[0m \033[34m{row[2]}\033[0m \033[35m{row[3]}\033[0m")

# 4. Filtravimai ir testai
print("\033[1;34m--- Mokytojai, kurie dėsto matematiką ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE dalykas = 'Matematika'")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojai, kurių atlyginimas > 1500 ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE atlyginimas > 1500")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojų vardai ir pavardės ---\033[0m")
cursor.execute("SELECT vardas, pavarde FROM mokytojai")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojai su atlyginimu tarp 1000 ir 2000 ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE atlyginimas BETWEEN 1000 AND 2000")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojai, dėstantys Lietuvių, Anglų arba Istoriją ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE dalykas IN ('Lietuvių', 'Anglų', 'Istorija')")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojai, kurių pavardė prasideda J ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE pavarde LIKE 'J%'")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojai, kurių vardas baigiasi s ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE vardas LIKE '%s'")
print(cursor.fetchall())

print("\033[1;34m--- Mokytojai, kurių antra vardo raidė yra e ---\033[0m")
cursor.execute("SELECT * FROM mokytojai WHERE vardas LIKE '_e%'")
print(cursor.fetchall())

# 5. TESTAVIMAS
print("\033[1;34m--- TESTAVIMAS ---\033[0m")

# Tikriname, ar lentelė egzistuoja
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mokytojai'")
print("Lentelė egzistuoja:", cursor.fetchone() is not None)

# Tikriname, ar yra 5 įrašai
cursor.execute("SELECT COUNT(*) FROM mokytojai")
print("Mokytojų skaičius:", cursor.fetchone()[0])

# Tikriname, ar egzistuoja mokytojas vardu 'Jonas'
cursor.execute("SELECT COUNT(*) FROM mokytojai WHERE vardas = 'Jonas'")
print("Ar yra Jonas:", cursor.fetchone()[0] > 0)

# Tikriname, ar bent vienas mokytojas turi atlyginimą >1500
cursor.execute("SELECT COUNT(*) FROM mokytojai WHERE atlyginimas > 1500")
print("Mokytojų su atlyginimu >1500 skaičius:", cursor.fetchone()[0])

# Uždaryti prisijungimą
conn.close()
