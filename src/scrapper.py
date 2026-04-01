import re
import requests
from bs4 import BeautifulSoup

def clean_price(price_str):
    if not price_str or not isinstance(price_str, str):
        return None
    chiffres = re.findall(r'\d+', price_str)
    chainefinal = ''.join(chiffres)
    return int(chainefinal) if chainefinal else None

def get_product_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Code de réponse : {response.status_code}") # AJOUTE CETTE LIGNE

        if response.status_code != 200:
            print("Le site nous bloque ou l'URL est mauvaise.")
        soup = BeautifulSoup(response.text, "html.parser") # S majuscule

        price_tag = soup.find('p', class_='price')
        title_tag = soup.find('h1', class_='title')
        # Juste avant le if price_tag:
        print(f"Prix trouvé ? {price_tag is not None}")
        print(f"Titre trouvé ? {title_tag is not None}")
        if price_tag and title_tag:
            raw_price = price_tag.get_text()
            product_name = title_tag.get_text().strip()
            
            # Correction de l'orthographe ici
            cleaned_price = clean_price(raw_price) 

            return {
                "name": product_name,
                "price": cleaned_price,
                "url": url
            }
    except Exception as e:
        print(f"Erreur lors du scraping : {e}")
        
    return None