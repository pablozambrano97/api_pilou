import sqlite3
DATABASE_NAME="contacts.db" 

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn 

def create_tables():
    tables = [
            """CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGRER NOT NULL,
                phone INTEGER NOT NULL,
                photo TEXT NOT NULL,
                email TEXT NOT NULL,
                nick TEXT NOT NULL
            )"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)