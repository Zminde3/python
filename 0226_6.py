import sqlite3
import pandas as pd
from tabulate import tabulate

# ANSI spalvų kodai
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Prisijungiame prie SQLite duomenų bazės
conn = sqlite3.connect("projects2.db")
cursor = conn.cursor()

# Sukuriame lenteles
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Project (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        deadline DATE NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('Pending', 'In Progress', 'Completed')),
        FOREIGN KEY (project_id) REFERENCES Project(id) ON DELETE CASCADE
    );
""")

# Pridedame projektus
projects = [
    ("Senelio šiltnamio renovacija", "2025-06-01"),
    ("Dronų lenktynių trasos įrengimas", "2025-07-15"),
    ("Interaktyvus šachmatų turnyras", "2025-05-10"),
    ("Robo-šuns mokymo algoritmas", "2025-09-30"),
    ("Ateities cepelinų recepto konkursas", "2025-08-20"),
]

cursor.executemany("INSERT OR IGNORE INTO Project (name, deadline) VALUES (?, ?);", projects)
conn.commit()

# Sukuriame užduotis projektams
cursor.execute("SELECT id FROM Project;")
project_ids = [row[0] for row in cursor.fetchall()]

tasks = []
statuses = ["Pending", "In Progress", "Completed"]
for project_id in project_ids:
    tasks.append((project_id, "Pirmoji užduotis", statuses[0]))
    tasks.append((project_id, "Antroji užduotis", statuses[1]))
    tasks.append((project_id, "Trečioji užduotis", statuses[2]))

cursor.executemany("INSERT OR IGNORE INTO Task (project_id, description, status) VALUES (?, ?, ?);", tasks)
conn.commit()

# Pasirinkto projekto užduotys
project_id = 5
cursor.execute("SELECT id, description, status FROM Task WHERE project_id = ?;", (project_id,))
tasks_for_project = cursor.fetchall()

df_tasks = pd.DataFrame(tasks_for_project, columns=["ID", "Užduotis", "Būsena"])
print(f"\n🔹 {RED}Užduotys, priklausančios projektui {project_id}:{RESET}")
print(tabulate(df_tasks, headers="keys", tablefmt="psql").replace("-", f"{BLUE}-{RESET}"))

# Projektai su nebaigtomis užduotimis
cursor.execute("""
    SELECT DISTINCT p.id, p.name, p.deadline
    FROM Project p
    JOIN Task t ON p.id = t.project_id
    WHERE t.status IN ('Pending', 'In Progress');
""")
projects_with_pending_tasks = cursor.fetchall()

df_projects = pd.DataFrame(projects_with_pending_tasks, columns=["ID", "Projekto pavadinimas", "Terminas"])
print(f"\n🔹 {RED}Projektai su nebaigtomis užduotimis:{RESET}")
print(tabulate(df_projects, headers="keys", tablefmt="psql").replace("-", f"{BLUE}-{RESET}"))

conn.close()
