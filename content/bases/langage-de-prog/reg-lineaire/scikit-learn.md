+++
title = "La bibliothèque Scikit-learn"
weight = 186
draft = true
+++

![scikit-learn](./scikit-learn-logo-small.png?width=25vw)

## Introduction à scikit-learn

`Scikit-learn` est une bibliothèque open-source de machine learning pour Python. Elle offre une gamme d'outils pour l'analyse et la modélisation des données. `Scikit-learn` est construite sur `NumPy`, `SciPy` et `matplotlib`, ce qui en fait une bibliothèque puissante et facile à utiliser.

https://scikit-learn.org/stable/

## Installation

Pour installer scikit-learn, vous pouvez utiliser pip :
```bash
pip install scikit-learn
```

## Principales fonctionnalités de scikit-learn

Scikit-learn est une bibliothèque Python très populaire pour le machine learning. Voici quelques-unes de ses principales fonctionnalités, expliquées de manière simple pour les débutants :

1. **Jeux de données intégrés** : Scikit-learn propose plusieurs ensembles de données intégrés, comme l'ensemble de données Iris ou celui des prix des maisons. Ces ensembles sont parfaits pour apprendre et tester des modèles de machine learning sans avoir à chercher des données ailleurs.

2. **Régression** : Pour les tâches où l'on veut prédire une valeur continue (comme le prix d'une maison), Scikit-learn propose des algorithmes de régression, comme la régression linéaire et la régression Ridge.

3. **Division des données** : Avant d'entraîner un modèle, il est essentiel de diviser les données en deux parties : une pour l'entraînement et une pour les tests. La fonction `train_test_split` de Scikit-learn permet de faire cela facilement en une seule ligne de code.

4. **Algorithmes de classification** : Scikit-learn offre une variété d'algorithmes pour classer les données, comme les forêts aléatoires, les machines à vecteurs de support (SVM) et les k-plus proches voisins (k-NN). Ces algorithmes aident à prédire des catégories ou des classes.

5. **Clustering** : Scikit-learn permet également de regrouper des données similaires ensemble avec des algorithmes de clustering comme k-means. Cela est utile pour découvrir des structures cachées dans les données.

6. **Réduction de dimensionnalité** : Pour simplifier les modèles et réduire le temps de calcul, Scikit-learn propose des techniques de réduction de dimensionnalité comme l'analyse en composantes principales (PCA).

7. **Prétraitement des données** : Scikit-learn inclut des outils pour normaliser et standardiser les données, ce qui est crucial pour de nombreux algorithmes de machine learning.

## Exemple d'Utilisation : Régression Linéaire
Voici un exemple simple de régression linéaire avec scikit-learn.

### Étape 1 : Importation des bibliothèques
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
```

### Étape 2 : Chargement des données
Pour cet exemple, nous allons utiliser un jeu de données fictif :
```python
# Création des données
data = {
    'Superficie': [50, 60, 80, 100, 120, 150],
    'Prix': [150, 180, 240, 300, 360, 450]
}
df = pd.DataFrame(data)
X = df[['Superficie']]
y = df['Prix']
```

### Étape 3 : Division des données en enseignement et test
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### Étape 4 : Création et entraînement du modèle
```python
# Création du modèle de régression linéaire
modele = LinearRegression()

# Entraînement du modèle
modele.fit(X_train, y_train)
```

#### Étape 5 : Prédiction et évaluation
```python
# Prédiction des valeurs
y_pred = modele.predict(X_test)

# Évaluation du modèle
mse = mean_squared_error(y_test, y_pred)
print(f'Erreur quadratique moyenne : {mse}')
```

#### Étape 6 : Visualisation des résultats
```python
# Tracé des points de données
plt.scatter(X, y, color='blue', label='Données réelles')

# Tracé de la ligne de régression
plt.plot(X, model.predict(X), color='red', label='Ligne de régression')

# Ajout de l'équation de la droite de régression
a = modele.coef_[0]
b = modele.intercept_
equation = f'y = {a:.2f}x + {b:.2f}'
plt.text(1, 4.5, equation, fontsize=12, color='black')

# Ajout des labels et de la légende
plt.xlabel('Superficie (m²)')
plt.ylabel('Prix (en milliers de dollars)')
plt.title('Régression Linéaire avec scikit-learn')
plt.legend()

# Affichage du graphique
plt.show()
```

### Explication

**Importation des bibliothèques** : Nous importons numpy pour les calculs numériques, matplotlib pour la visualisation, et LinearRegression de sklearn pour créer le modèle de régression linéaire.
**Préparation des Données** : Nous créons un jeu de données simple avec X et y.
**Création et entraînement du modèle** : Nous créons un modèle de régression linéaire et l’entraînons avec les données.
**Prédiction** : Nous utilisons le modèle pour prédire les valeurs de y en fonction de X.
**Tracé du graphique et ajout de l’équation** : Nous traçons les points de données et la ligne de régression. Ensuite, nous ajoutons l’équation de la droite de régression sur le graphique en utilisant plt.text.