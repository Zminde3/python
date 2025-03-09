import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')  # Sukuria laikiną DB atmintyje
cur = conn.cursor()

cur.execute('''
CREATE TABLE mokytojai (
    id INTEGER PRIMARY KEY,
    vardas TEXT,
    pavarde TEXT,
    dalykas TEXT,
    atlyginimas INTEGER
)
''')

# Įterpiame pavyzdinius duomenis
mokytojai = [
    ("Jonas", "Jonaitis", "Matematika", 2500),
    ("Petras", "Petraitis", "Fizika", 1800),
    ("Asta", "Astaite", "Chemija", 2200),
    ("Rasa", "Rasaitė", "Lietuvių", 1900),
    ("Tomas", "Tomaitis", "Istorija", 2100)
]

cur.executemany("INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES (?, ?, ?, ?)", mokytojai)
conn.commit()
