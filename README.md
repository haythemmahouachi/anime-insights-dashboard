<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/5521c681-8c60-425e-949d-2cdf0ac95fcf" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/768e2c5f-078b-4ffd-9ec9-5796cc65f3ce" />



# English
# 🎌 Anime Insights Dashboard

This project is an analysis of anime data from a raw dataset.  
The goal is to clean the data, create derived tables, and build an interactive dashboard with **Power BI**.

---

## 📊 Dashboard Overview
The dashboard includes the following indicators:
- **Total Anime**
- **Total Users**
- **Average Ratings**
- **Top 10 Highest Rated Anime**
- **Top 10 Most Popular Anime**
- **Genre Distribution**
- **Ratings Distribution**
- **Average Rating by Type (TV, Movie, OVA, etc.)**

---

## ⚙️ Project Steps

### 1. Data Cleaning & Preparation
- Removal of special characters in anime titles.
- Normalization of genres (splitting and exploding into unique rows).
- Creation of a lookup table (`genre_lookup`).

The cleaning script can be found in [`clean_anime.py`](clean_anime.py).

### 2. Data Modeling
- Creation of derived tables (`anime_genres`, `genre_lookup`, `anime_genre_split`).
- Integration of cleaned datasets into Power BI.

### 3. Visualization
The Power BI file (`Anime Dashs.pbix`) contains all interactive visualizations.

---

## 🚀 How to Use the Project

1. Clone the repo:
   ```bash
   git clone https://github.com/haythemmahouachi/anime-insights-dashboard.git
   ```

# Install dependencies:
```bash
pip install pandas
```

# Run the cleaning script:
```bash
python clean_anime_data.py
```

📁 **Datasets Used**

- `Anime.csv` : original dataset  
- `Rating.csv` : user data  
- `Anime_cleaned.csv` : cleaned dataset  
- `Anime_genre_split.csv` : exploded genres  
- `Genre_lookup.csv` : genre dictionary  

✨ **Technologies Used**

- Python (pandas, regex, html) → data cleaning and transformation  
- Power BI → interactive visualization and dashboard  
- GitHub → sharing and collaboration  

📌 **Author**

👨‍💻 Developed by **Haythem Mahouachi**  
📍 Nabeul, Tunisia  
📧 **haythemmahouachi@outlook.com**  
📱 **+216 54 461 033**


# Français
# 🎌 Anime Insights Dashboard

Ce projet est une analyse des données d'anime à partir d'un dataset brut.  
L'objectif est de nettoyer les données, créer des tables dérivées, et construire un dashboard interactif avec **Power BI**.

---

## 📊 Aperçu du Dashboard
Le dashboard contient les indicateurs suivants :
- **Total Anime**
- **Total Users**
- **Moyenne des Ratings**
- **Top 10 des animes les mieux notés**
- **Top 10 des animes les plus populaires**
- **Répartition des genres**
- **Distribution des ratings**
- **Note moyenne par type (TV, Movie, OVA, etc.)**

---

## ⚙️ Étapes du projet

### 1. Nettoyage et préparation des données
- Suppression de caractères spéciaux dans les noms d'anime.
- Normalisation des genres (séparation et explosion en lignes uniques).
- Création d'une table de correspondance (`genre_lookup`).

Le script de nettoyage se trouve dans [`clean_anime_data.py`](clean_anime_data.py).

### 2. Modélisation des données
- Création de tables dérivées (`anime_genres`, `genre_lookup`, `anime_genre_split`).
- Intégration des datasets nettoyés dans Power BI.

### 3. Visualisation
Le fichier Power BI (`Anime Dashs.pbix`) contient toutes les visualisations interactives.

---

## 🚀 Comment utiliser le projet

1. Cloner le repo :
   ```bash
   git clone https://github.com/haythemmahouachi/anime-insights-dashboard.git
# anime-insights-dashboard

# Installer les dépendances :
   pip install pandas
 

# Lancer le script de nettoyage :
   python clean_anime_data.py


## 📁 Datasets utilisés

- `Anime.csv` : dataset original  
- `Rating.csv` : données des utilisateurs  
- `Anime_cleaned.csv` : dataset nettoyé  
- `Anime_genre_split.csv` : genres explosés  
- `Genre_lookup.csv` : dictionnaire des genres  

## ✨ Technologies utilisées

- Python (pandas, regex, html) → nettoyage et transformation des données  
- Power BI → visualisation et dashboard interactif  
- GitHub → partage et collaboration  

## 📌 Auteur

👨‍💻 Développé par **Haythem Mahouachi**  
📍 Nabeul, Tunisie  
## 📧 haythemmahouachi@outlook.com 
## 📱 +216 54 461 033


