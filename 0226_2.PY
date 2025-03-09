import sqlite3
import bcrypt

conn = sqlite3.connect("admin_users.db")
c = conn.cursor()

query = ''' 
CREATE TABLE IF NOT EXISTS admin_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,  -- Čia saugosime užšifruotus slaptažodžius
    role TEXT NOT NULL DEFAULT "user"
);
'''
with conn:
    c.execute(query)

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(stored_hash, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), stored_hash)

with conn:
    c.execute('INSERT OR IGNORE INTO admin_users (username, password, role) VALUES (?, ?, ?)',
              ("admin", hash_password("admin123"), "admin"))
    c.execute('INSERT OR IGNORE INTO admin_users (username, password) VALUES (?, ?)',
              ("bronius69", hash_password("654321")))
    c.execute('INSERT OR IGNORE INTO admin_users (username, password) VALUES (?, ?)',
              ("maryte420", hash_password("abcdefg")))
    c.execute('INSERT OR IGNORE INTO admin_users (username, password, role) VALUES (?, ?, ?)',
              ("Statyspop", hash_password("administratorius"), "admin"))

inp_username = input('🔑 Įveskite naudotojo vardą: ')
inp_password = input('🔐 Įveskite slaptažodį: ')

with conn:
    c.execute("SELECT password, role FROM admin_users WHERE username = ?;", (inp_username,))
    res = c.fetchone()

if res:
    stored_hash, role = res
    if check_password(stored_hash, inp_password):
        print(f'✅ Prisijungimas sėkmingas! Sveiki, {inp_username}! Jūsų rolė: {role}')
    else:
        print('❌ Klaida: neteisingas slaptažodis.')
else:
    print('❌ Klaida: toks naudotojas neegzistuoja.')

conn.close()