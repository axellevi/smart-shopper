import sqlite3

def check():
    conn = sqlite3.connect('data/prices.db')
    cursor = conn.cursor()
    
    # On sélectionne les colonnes précisément pour éviter les erreurs d'index
    cursor.execute("SELECT id, product_name, price, timestamp FROM price_history")
    rows = cursor.fetchall()
    
    print(f"{'ID':<3} | {'Nom':<20} | {'Prix':<10} | {'Date'}")
    print("-" * 65)
    for row in rows:
        # row[0] = id, row[1] = nom, row[2] = prix, row[3] = date
        print(f"{row[0]:<3} | {row[1]:<20} | {row[2]:<10} | {row[3]}")
    
    conn.close()

if __name__ == "__main__":
    check()