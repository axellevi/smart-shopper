# 1. Imports des fonctions depuis tes fichiers
from src.database import setup_db, save_price
from src.scrapper import get_product_data

def main():
    # ÉTAPE A : Préparation
    print("--- Initialisation de la base de données ---")
    setup_db()

    # ÉTAPE B : Récupération (Choisis une URL de Coin Afrique)
    url_test = "https://bj.coinafrique.com/annonce/ordinateurs/pc-lenovo-v15-g2-5824030" # L'URL de ton image
    print(f"--- Scraping en cours sur : {url_test} ---")
    
    data = get_product_data(url_test)

    # ÉTAPE C : Sauvegarde
    if data:
        print(f"Produit trouvé : {data['name']} à {data['price']} FCFA")
        save_price(data['name'], data['url'], data['price'])
        print("--- Données sauvegardées avec succès ! ---")
    else:
        print("Erreur : Impossible de récupérer les données du produit.")

# Lancement du programme
if __name__ == "__main__":
    main()