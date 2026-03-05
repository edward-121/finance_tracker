import sqlite3

def add_expense(date, category, amount, description):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))

    conn.commit()
    conn.close()
    print("Expense added!")

# sample data
add_expense("2026-02-01", "Food", 50, "Groceries")
add_expense("2026-02-02", "Transport", 20, "Bus ticket")
add_expense("2026-02-03", "Entertainment", 100, "Movies")