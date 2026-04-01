import sqlite3 as sql3
from datetime import datetime

def setup_db():
    conn = sql3.connect('data/prices.db')

    curseur = conn.cursor()

    curseur.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price INTEGER,
            url TEXT NOT NULL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_price(name, url, price):
    conn = sql3.connect('data/prices.db')
    curseur = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    requete = "INSERT INTO price_history (product_name, price, url, timestamp) VALUES (?, ?, ?, ?)"
    valeurs = (name, price, url, timestamp)
    curseur.execute(requete, valeurs)
    conn.commit()
    conn.close()