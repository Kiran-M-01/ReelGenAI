import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("""create table if not exists users (id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(100) UNIQUE NOT NULL, email varchar(100) UNIQUE NOT NULL, password_hash varchar(255) NOT NULL)""")



# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

connection.commit()
connection.close()


print("Users table created successfully!")