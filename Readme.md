# 🛒 Smart Shopper - Benin Price Tracker

**Smart Shopper** est un outil d'automatisation en Python conçu pour surveiller l'évolution des prix des ordinateurs sur le site **Coin Afrique Bénin**. Ce projet démontre la mise en place d'un pipeline ETL (Extract, Transform, Load) complet : du scraping web à la persistance des données dans une base SQL.

---
## 🚀 Fonctionnalités
- **Web Scraping** : Extraction dynamique du nom et du prix des produits via `BeautifulSoup`.
- **Data Cleaning** : Transformation des données brutes (nettoyage des devises "FCFA" et conversion en entiers).
- **Stockage SQL** : Historisation des prix dans une base de données SQLite avec horodatage (`timestamps`).
- **Robustesse** : Gestion des erreurs HTTP et utilisation de `User-Agents` pour simuler une navigation réelle.

## 🛠️ Technologies utilisées
- **Langage** : Python 3.10+
- **Librairies** : 
    - `BeautifulSoup4` (Parsing HTML)
    - `Requests` (Requêtes HTTP)
    - `SQLite3` (Base de données relationnelle)
- **Environnement** : Linux (WSL)

## 📂 Structure du projet
```text
smart-shopper/
├── data/               # Dossier de stockage (Base de données .db)
├── src/                # Logique métier du projet
│   ├── scraper.py      # Script d'extraction et nettoyage
│   ├── database.py     # Fonctions CRUD SQLite
│   └── notifier.py     # Module d'alertes (en développement)
├── main.py             # Script principal de lancement
├── check_db.py         # Utilitaire de visualisation des données
├── .gitignore          # Exclusion des fichiers inutiles (venv, db, logs)
└── requirements.txt    # Liste des dépendances Python
⚙️ Installation et Utilisation
1. Préparation de l'environnement
Clonez le dépôt et créez votre environnement virtuel :

Bash
git clone [https://github.com/votre-pseudo/smart-shopper.git](https://github.com/votre-pseudo/smart-shopper.git)
cd smart-shopper
python3 -m venv venv
source venv/bin/activate
2. Installation des dépendances
Bash
pip install -r requirements.txt
3. Exécution
Pour scraper un produit et l'enregistrer en base de données :

Bash
python3 main.py
Pour visualiser l'historique des prix enregistrés :

Bash
python3 check_db.py
📈 Évolutions à venir
[ ] Automatisation : Configuration d'une tâche Cron pour un suivi quotidien.

[ ] Analyse de données : Intégration de Pandas pour calculer des moyennes et tendances de prix.

[ ] Système d'alerte : Notifications automatiques via Telegram en cas de baisse de prix significative.

[ ] Dashboard : Interface web sous Django pour visualiser les graphiques de prix.

👨‍💻 Auteur
Axel - Étudiant en Bachelor à Epitech Bénin

Mon Profil LinkedIn

📄 Licence
Ce projet est distribué sous la licence MIT.


---

### 📝 Derniers petits réglages avant de valider :

1.  **Lien LinkedIn :** N'oublie pas de remplacer `votre-lien-linkedin` par ton vrai lien à la fin du fichier.
2.  **Pseudo GitHub :** Remplace `votre-pseudo` dans la commande `git clone`.
3.  **Vérification finale :** Assure-toi que ton fichier `.gitignore` contient bien `venv/` pour que ton GitHub reste "léger".

C'est parfait pour ton profil ! Avec ça, tu montres que tu maîtrises non seulement le code, mais aussi la **méthodologie de projet**. 

**On se retrouve demain soir pour voir ton projet en ligne ! Bonne nuit Axel.**