import sqlite3

db_name = "bank.db"

def get_connection():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

def db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS account(
                Account_number INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                gender TEXT,
                DOB TEXT,
                email TEXT UNIQUE,
                phone_no TEXT UNIQUE,
                Balance INTEGER DEFAULT 0
            )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS credential(
                login_id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT NOT NULL,
                user_email TEXT NOT NULL,
                FOREIGN KEY(user_email) REFERENCES account(email)
            )
    ''')
    
    conn.commit()
    conn.close()