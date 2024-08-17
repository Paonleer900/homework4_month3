# db_main.py

import sqlite3

def sql_create():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        productid INTEGER,
        category TEXT,
        infoproduct TEXT
    )
    ''')

    conn.commit()
    conn.close()
