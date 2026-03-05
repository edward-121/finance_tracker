import sqlite3

def create_database():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

create_database()
print("Database created successfully!")