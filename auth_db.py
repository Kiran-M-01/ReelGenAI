import sqlite3

# FOR CREATING USER TABLE TO STORE USER INFORMATION
def create_users_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("""create table if not exists users (id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(100) UNIQUE NOT NULL, email varchar(100) UNIQUE NOT NULL, password_hash varchar(255) NOT NULL)""")



# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

    connection.commit()
    connection.close()


    print("Users table created successfully!")


# TO STORE USER INFORMATIONS
def create_user(username, email, password_hash):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(
        """ 
        INSERT INTO users(username, email, password_hash) 
        values(?,?,?) 
        """,
        (username, email, password_hash)
        )
    
    connection.commit()
    connection.close()

#TO VERIFY IF THE EMAIL EXISTS OR NOT
def get_user_by_email(email):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()
    connection.close()
    # print(user)
    return user

#TO VERIFY IF THE USER EXISTS OR NOT
def get_user_by_username(username):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM users 
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()
    connection.close()
    return user


def get_user_by_id(user_id):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        """ 
        SELECT * FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()
    connection.close()
    return user