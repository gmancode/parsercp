import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute("SELECT login FROM users")
if sql.fetchall() is None:
    sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
    db.commit()

    print('Зареган!')
else:
    print('Уже есть!')

    for valid in sql.execute("SELECT * FROM users"):
        print(values)