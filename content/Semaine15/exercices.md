+++
title = "Exercices pratiques (Pandas)"
weight = 151
+++

### Objectifs

Ces exercices vous permettront de pratiquer les concepts suivants avec Pandas:
- Création de listes uniques.
- Filtrage de données.
- Calcul de moyennes.
- Recherche de valeurs maximales avec des données.

### Exercice 1: Analyse des ventes de produits

**Objectif:**
L'objectif de cet exercice est de pratiquer les concepts de création de listes uniques, de filtrage de données et de calcul de moyennes avec des données de ventes de produits.

**Données et fichier Jupyter notebook**

- [Fichier de données](../produits.csv)
- [Fichier Jupyter Notebook](../produits.ipynb)


**Instructions**:
1. Créer une liste des produits uniques:
	- À partir de la colonne 'Produit' du dataframe, créez une liste des produits uniques.

2. Créer une liste contenant les produits et leurs ventes:
	- Sélectionnez les colonnes 'Produit' et 'Ventes' du dataframe et convertissez-les en une liste (le résultat sera une liste de liste [ [sous-liste1], [sous-liste2],...[sous-listeX] ]).

3. Calculer la vente moyenne pour chaque produit:
	- Parcourez la liste des produits uniques un produit à la fois.
	- Pour chaque produit, obtenez la somme des ventes et calculez la moyenne.

4. Afficher la vente moyenne pour chaque produit:
	- Affichez la vente moyenne pour chaque produit sous la forme: "Produit X: La vente moyenne est de Y unités".

**Résultat attendu**:
```plaintext
Produit B: La vente moyenne est de 206.67 unités
Produit A: La vente moyenne est de 223.33 unités
Produit C: La vente moyenne est de 200.0 unités
```

### Exercice 2: Analyse des ventes de voitures

**Objectif**:
L'objectif de cet exercice est de pratiquer les concepts de filtrage de données et de calcul de moyennes avec des données de ventes de voitures.

**Données et fichier Jupyter notebook**

- [Fichier de données](../voitures.csv)
- [Fichier Jupyter Notebook](../voitures.ipynb)

**Instructions**
1. Filtrer les données pour les ventes de voitures entre 2015 et 2020:
	- Utilisez les données fournies pour filtrer les ventes de voitures entre les années 2015 et 2020.

2. Calculer le nombre moyen de ventes de voitures:
	- Parcourez les données filtrées pour calculer la somme des ventes de voitures.
	- Calculez la moyenne des ventes de voitures sur la période donnée.

3. Afficher le nombre moyen de ventes de voitures:
	- Affichez le nombre moyen de ventes de voitures sous la forme: "Le nombre moyen de ventes de voitures de 2015 à 2020 est de X".

**Résultat attendu**:
```plaintext
Le nombre moyen de ventes de voitures de 2015 à 2020 est de 14.5$
```

### Exercice 3: Analyse des scores des étudiants

**Objectif:**
L'objectif de cet exercice est de pratiquer les concepts de filtrage de données et de calcul de moyennes avec des données de scores d'examen des étudiants.

**Données et fichier Jupyter notebook**
- [Fichier de données](../etudiants.csv)
- [Fichier Jupyter Notebook](../etudiants.ipynb)

**Instructions**
1. Filtrer les données pour un étudiant spécifique:
	- Utilisez les données fournies pour filtrer les scores d'un étudiant spécifique, par exemple, 'Étudiant 1'.

2. Calculer le score moyen de l'étudiant:
	- Parcourez les données filtrées pour calculer la somme des scores de l'étudiant.

3. Calculez la moyenne des scores de l'étudiant sur la période donnée.

4. Afficher le score moyen de l'étudiant:
	- Affichez le score moyen de l'étudiant sous la forme: "Le score moyen de l'étudiant X est de Y".

**Résultat attendu**
```plaintext
La matière où l'Étudiant 1 a obtenu le meilleur score est 9    Informatique
Name: Matière, dtype: object
```
