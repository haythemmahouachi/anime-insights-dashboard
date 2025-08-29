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
   git clone https://github.com/<ton-username>/anime-insights-dashboard.git
# anime-insights-dashboard
