import sqlite3
import pandas as pd
from tabulate import tabulate

conn = sqlite3.connect("projects.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        deadline DATE NOT NULL
    )
''')
conn.commit()

projects = [
    ('Virtualios realybės mokymo platforma', '2025-06-01'),
    ('Automatinės apskaitos sistema', '2025-07-15'),
    ('Dirbtinio intelekto kalbos modelis', '2025-05-10'),
    ('Savavaldis dronas pašto pristatymui', '2025-09-30'),
    ('Naujos kartos kibernetinio saugumo sistema', '2025-08-20')
]

c.executemany('INSERT OR IGNORE INTO projects (name, deadline) VALUES (?, ?)', projects)
conn.commit()

c.execute("SELECT * FROM projects")
result = c.fetchall()

df = pd.DataFrame(result, columns=["ID", "Projekto pavadinimas", "Terminas"])
print("\nVisi projektai:")
print(tabulate(df, headers="keys", tablefmt="psql"))

conn.close()
