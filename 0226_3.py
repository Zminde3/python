import sqlite3

conn = sqlite3.connect("projects.db")
cursor = conn.cursor()

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

projects = [
    ("Senelio šiltnamio renovacija", "2025-06-01"),
    ("Dronų lenktynių trasos įrengimas", "2025-07-15"),
    ("Interaktyvus šachmatų turnyras", "2025-05-10"),
    ("Robo-šuns mokymo algoritmas", "2025-09-30"),
    ("Ateities cepelinų recepto konkursas", "2025-08-20"),
]

cursor.executemany("INSERT INTO Project (name, deadline) VALUES (?, ?);", projects)

cursor.execute("SELECT id FROM Project;")
project_ids = [row[0] for row in cursor.fetchall()]

tasks = []
statuses = ["Pending", "In Progress", "Completed"]
for project_id in project_ids:
    tasks.append((project_id, "Task 1 description", statuses[0]))
    tasks.append((project_id, "Task 2 description", statuses[1]))
    tasks.append((project_id, "Task 3 description", statuses[2]))

cursor.executemany("INSERT INTO Task (project_id, description, status) VALUES (?, ?, ?);", tasks)

conn.commit()

project_id = 5
cursor.execute("SELECT * FROM Task WHERE project_id = ?;", (project_id,))
tasks_for_project = cursor.fetchall()

print(f"\n🔹 Užduotys, priklausančios projektui {project_id}:")
for task in tasks_for_project:
    print(task)

cursor.execute("""
    SELECT DISTINCT p.id, p.name, p.deadline
    FROM Project p
    JOIN Task t ON p.id = t.project_id
    WHERE t.status IN ('Pending', 'In Progress');
""")
projects_with_pending_tasks = cursor.fetchall()

print("\n🔹 Projektai su nebaigtomis užduotimis:")
for project in projects_with_pending_tasks:
    print(project)

conn.close()
