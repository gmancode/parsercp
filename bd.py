import sqlite3


db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")
db.commit()

user_login = input('Логин: ')
user_password = input('Пароль: ')

sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
    db.commit()

    print('Зарегестрирован!')
else:
    print('Такая запись уже есть!')

    for value in sql.execute("SELECT * FROM users"):
        print(value)