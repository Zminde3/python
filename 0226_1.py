import sqlite3

conn = sqlite3.connect("admin_users.db")
c = conn.cursor()

query = ''' 
CREATE TABLE IF NOT EXISTS admin_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT "user"
);
'''
with conn:
    c.execute(query)

with conn:
    c.execute('INSERT OR IGNORE INTO admin_users (username, password, role) VALUES ("admin", "admin123", "admin");')
    c.execute('INSERT OR IGNORE INTO admin_users (username, password) VALUES ("bronius69", "654321");')
    c.execute('INSERT OR IGNORE INTO admin_users (username, password) VALUES ("maryte420", "abcdefg");')
    c.execute('INSERT OR IGNORE INTO admin_users (username, password, role) VALUES ("Statyspop", "administratorius", "admin");')

inp_username = input('🔑 Įveskite naudotojo vardą: ')
inp_password = input('🔐 Įveskite slaptažodį: ')

with conn:
    c.execute("SELECT * FROM admin_users WHERE username = ? AND password = ?;", (inp_username, inp_password))
    res = c.fetchone()

if res:
    print(f'✅ Prisijungimas sėkmingas! Sveiki, {res[1]}! Jūsų rolė: {res[3]}')
else:
    print('❌ Klaida: neteisingas naudotojo vardas arba slaptažodis.')

conn.close()
