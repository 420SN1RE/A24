+++
title = "Matplotlib"
weight = 121
+++

![Bibliohèque MatplotLib](../matplotlib.jpg?width=30vw)

## Qu'est-ce que Matplotlib ?

La visualisation de données est une compétence essentielle en sciences afin de représenter graphiquement des données complexes pour en faciliter l'analyse et l'interprétation. **Matplotlib** est une bibliothèque pour la visualisation de données. Elle permet de créer une variété de graphiques pour représenter les données de manière claire et informative.

## Utilisation de Matplotlib

Pour commencer, vous devez importer dans votre script Python :

```python
import matplotlib.pyplot as plt
```

Pour vérifier que Matplotlib est bien installé sur votre environnement :

```python
# Version de Matplotlib
plt.__version__
```

## Création de graphiques simples

### Graphique en Lignes

```python
import matplotlib.pyplot as plt

# Les coordonnées de 5 points
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Traçage du graphique
plt.plot(x, y)

# Définition des axes
plt.xlabel('Axe x')
plt.ylabel('Axe y')

# Ajout du titre du graphique
plt.title('Graphique en lignes')

# Affichage du graphique
plt.show()
```

**Résultat:**
![Graphique en lignes](../matplotlib-lignes.png?width=20vw)

### Graphique en barres

```python
categories = ['A', 'B', 'C', 'D']
valeurs = [3, 7, 5, 4]

plt.bar(categories, valeurs)
plt.xlabel('Catégories')
plt.ylabel('Valeurs')
plt.title('Graphique en barres')
plt.show()
```

**Résultat:**
![Graphique en barres](../matplotlib-barres.png?width=20vw)

### Histogramme

```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, range=(1, 5), density=False, cumulative=False, color='green', edgecolor='black')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('Histogramme')
plt.show()
```
#### Explication de la fonction `hist` :

- **x** : Les données à tracer sous forme de liste ou de tableau.
- **bins** : Le nombre de bacs (ou intervalles) dans lesquels les données sont regroupées. Par défaut, Matplotlib choisit automatiquement le nombre de bacs.
- **range** : Une paire de valeurs (min, max) pour définir la plage des bacs.
- **density** : Si `True`, l'aire sous l'histogramme sera normalisée à 1 (utile pour les distributions de probabilité).
- **cumulative** : Si `True`, l'histogramme sera cumulatif.
- **color** : La couleur des barres de l'histogramme.
- **edgecolor** : La couleur des bordures des barres.

**Résultat:**
![Histogramme](../matplotlib-histo.png?width=20vw)


### Graphique en nuages de points

```python
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 80, 200, 500]
plt.scatter(x, y, s=sizes)
plt.xlabel('Axe x')
plt.ylabel('Axe y')
plt.title('Graphique en nuage de points')
plt.show()
```

**Résultat:**
![Graphique en nuage](../matplotlib-nuage.png?width=20vw)

### Graphique en secteurs

```python
# Données
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # Décale le deuxième secteur

# Création du graphique en secteurs
plt.pie(sizes, explode=explode, labels=labels, colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'],
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Assure que le graphique est circulaire
plt.title('Graphique en secteurs')
plt.show()
```

#### Explication de la fonction `pie`

- **sizes** : Les tailles des secteurs, sous forme de liste ou de tableau.
- **labels** : Une séquence de chaînes de caractères fournissant les étiquettes pour chaque secteur.
- **colors** : Une séquence de couleurs pour les secteurs.
- **autopct** : Une chaîne de format ou une fonction utilisée pour étiqueter les secteurs avec leur valeur numérique. Par exemple, `'%1.1f%%'` affiche les pourcentages avec une décimale.
- **pctdistance** : La distance relative le long du rayon à laquelle le texte généré par `autopct` est dessiné.
- **shadow** : Si `True`, dessine une ombre sous le graphique.
- **startangle** : L'angle par lequel le début du graphique est tourné, dans le sens inverse des aiguilles d'une montre à partir de l'axe des x.
- **radius** : Le rayon du graphique.
- **explode** : Une séquence de fractions du rayon avec lesquelles décaler chaque secteur.
- **Secteurs** : Chaque secteur représente une catégorie des données.
- **Étiquettes** : Les étiquettes sont affichées à côté de chaque secteur.
- **Pourcentages** : Les pourcentages sont affichés à l'intérieur des secteurs si `autopct` est spécifié.
- **Ombre** : Une ombre peut être ajoutée pour un effet visuel supplémentaire.


**Résultat:**
![Graphique en secteurs](../matplotlib-secteur.png?width=20vw)

## Personnalisation et mise en forme des graphiques

### Couleurs et styles de lignes

```python
# Tirets verts, points marqués avec des cercles o
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.show()
```

### Ajout de légendes

```python
plt.plot(x, y, label='Données')
plt.legend()
plt.show()
```

### Annotations

```python
plt.plot(x, y)
plt.annotate('Point clé', xy=(3, 5), xytext=(4, 6), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

## Graphiques multiples

### Deux graphiques en lignes sur le même dessin

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Création du graphique
plt.plot(x, y1, label='Série 1', color='blue', linestyle='-', marker='o')
plt.plot(x, y2, label='Série 2', color='red', linestyle='--', marker='x')

# Ajout des étiquettes et du titre
plt.xlabel('Axe x')
plt.ylabel('Axe y')
plt.title('Deux graphiques en lignes')
plt.legend()

# Affichage du graphique
plt.show()
```

**Résultat:**
![Graphique en secteurs](../matplotlib-double.png?width=20vw)


### Graphiques multiples (sous-graphes)

```python
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 80, 200, 500]

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, y)
axs[0, 0].set_title('Graphique 1')

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Graphique 2')

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
axs[1, 0].hist(data, bins=5)
axs[1, 0].set_title('Graphique 3')

axs[1, 1].scatter(x, y, s=sizes)
axs[1, 1].set_title('Graphique 4')

plt.tight_layout()
plt.show()
```

**Explication**

Ce code crée une figure avec quatre types de graphiques différents (ligne, barres, histogramme, nuages de points) disposés dans une grille 2x2, chacun avec son propre titre. Cela permet de visualiser plusieurs types de données sur une seule figure.

### Étapes du Code

1. **Création de la figure et des sous-graphes** :
```python
fig, axs = plt.subplots(2, 2)
```
- `plt.subplots(2, 2)` crée une figure avec une grille de 2 lignes et 2 colonnes de sous-graphes.
- `fig` est la figure globale.
- `axs` est un tableau 2x2 d'axes (sous-graphes).

2. **Premier sous-graphe (Graphique 1)** :
```python
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Graphique 1')
```
- `axs[0, 0]` fait référence au sous-graphe en haut à gauche.
- `plot(x, y)` trace un graphique en lignes.
- `set_title('Graphique 1')` ajoute un titre au sous-graphe.

3. **Deuxième sous-graphe (Graphique 2)** :
```python
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Graphique 2')
```
- `axs[0, 1]` fait référence au sous-graphe en haut à droite.
- `bar(categories, values)` crée un graphique en barres.
- `set_title('Graphique 2')` ajoute un titre au sous-graphe.

4. **Troisième sous-graphe (Graphique 3)** :
```python
axs[1, 0].hist(data, bins=5)
axs[1, 0].set_title('Graphique 3')
```
- `axs[1, 0]` fait référence au sous-graphe en bas à gauche.
- `hist(data, bins=5)` crée un histogramme avec 5 bacs.
- `set_title('Graphique 3')` ajoute un titre au sous-graphe.

5. **Quatrième sous-graphe (Graphique 4)** :
```python
axs[1, 1].scatter(x, y, s=sizes)
axs[1, 1].set_title('Graphique 4')
```
- `axs[1, 1]` fait référence au sous-graphe en bas à droite.
- `scatter(x, y, s=sizes)` crée un graphique en nuages de points avec des tailles de points spécifiées par `sizes`.
- `set_title('Graphique 4')` ajoute un titre au sous-graphe.

6. **Ajustement de la mise en page** :
```python
plt.tight_layout()
```
- `tight_layout()` ajuste automatiquement les sous-graphes pour qu'ils ne se chevauchent pas.

7. **Affichage de la figure** :
```python
plt.show()
```
- `show()` affiche la figure avec les quatre sous-graphes.

**Résultat:**
![Graphiques multiples](../matplotlib-multi.png?width=40vw)


## Liste des principales méthodes de Matplotlib

Voici un tableau listant certaines des méthodes courantes de Matplotlib avec leurs descriptions :

| Méthode                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `plot()`               | Crée un graphique en ligne.                                                 |
| `scatter()`            | Crée un graphique de dispersion.                                            |
| `bar()`                | Crée un graphique à barres verticales.                                      |
| `barh()`               | Crée un graphique à barres horizontales.                                    |
| `hist()`               | Crée un histogramme.                                                        |
| `pie()`                | Crée un graphique en secteurs (camembert).                                  |
| `boxplot()`            | Crée un diagramme en boîte.                                                 |
| `violinplot()`         | Crée un diagramme en violon.                                                |
| `imshow()`             | Affiche une image sur un graphique.                                         |
| `contour()`            | Crée un graphique de contours.                                              |
| `contourf()`           | Crée un graphique de contours remplis.                                      |
| `pcolormesh()`         | Crée un graphique en maillage de couleurs.                                  |
| `errorbar()`           | Crée un graphique en ligne avec des barres d'erreur.                        |
| `stackplot()`          | Crée un graphique empilé.                                                   |
| `fill_between()`       | Remplit l'espace entre deux courbes.                                        |
| `subplots()`           | Crée une figure et un ensemble de sous-graphiques.                          |
| `subplot()`            | Ajoute un sous-graphe à une figure existante.                               |
| `legend()`             | Ajoute une légende au graphique.                                            |
| `xlabel()`             | Ajoute une étiquette à l'axe des x.                                         |
| `ylabel()`             | Ajoute une étiquette à l'axe des y.                                         |
| `title()`              | Ajoute un titre au graphique.                                               |
| `savefig()`            | Enregistre le graphique sous forme de fichier image.                        |
| `show()`               | Affiche le graphique à l'écran.                                             |

## Les paramètres des méthodes de traçage

Voici un tableau listant les paramètres des méthodes `plot`, `hist`, `scatter`, `pie` et `subplot` avec leurs descriptions :

| Méthode  | Paramètre          | Description                                                                 |
|----------|--------------------|-----------------------------------------------------------------------------|
| `plot`   | `x`                | Données pour l'axe des x.                                                   |
|          | `y`                | Données pour l'axe des y.                                                   |
|          | `color`            | Couleur de la ligne.                                                        |
|          | `linestyle`        | Style de la ligne (par exemple, '-', '--', '-.', ':').                       |
|          | `linewidth`        | Largeur de la ligne.                                                        |
|          | `marker`           | Marqueur pour les points de données (par exemple, 'o', 's', '^').            |
|          | `label`            | Étiquette pour la légende.                                                  |
|          | `alpha`            | Transparence de la ligne (0.0 à 1.0).                                       |
| `hist`   | `x`                | Données pour l'histogramme.                                                 |
|          | `bins`             | Nombre de bacs (bins) ou séquence définissant les bacs.                     |
|          | `range`            | Plage des valeurs à inclure.                                                |
|          | `density`          | Si True, normalise l'histogramme.                                           |
|          | `cumulative`       | Si True, affiche un histogramme cumulatif.                                  |
|          | `color`            | Couleur des barres de l'histogramme.                                        |
|          | `label`            | Étiquette pour la légende.                                                  |
|          | `alpha`            | Transparence des barres (0.0 à 1.0).                                        |
| `scatter`| `x`                | Données pour l'axe des x.                                                   |
|          | `y`                | Données pour l'axe des y.                                                   |
|          | `s`                | Taille des marqueurs.                                                       |
|          | `c`                | Couleur des marqueurs.                                                      |
|          | `marker`           | Style des marqueurs (par exemple, 'o', 's', '^').                           |
|          | `alpha`            | Transparence des marqueurs (0.0 à 1.0).                                     |
|          | `label`            | Étiquette pour la légende.                                                  |
| `pie`    | `x`                | Données pour les parts du graphique en secteurs.                            |
|          | `labels`           | Étiquettes pour chaque part.                                                |
|          | `colors`           | Couleurs des parts.                                                         |
|          | `autopct`          | Format des pourcentages affichés (par exemple, '%1.1f%%').                  |
|          | `shadow`           | Si True, ajoute une ombre.                                                  |
|          | `explode`          | Décale une part du centre (par exemple, [0, 0.1, 0, 0]).                    |
|          | `startangle`       | Angle de départ pour le premier secteur.                                    |
|          | `radius`           | Rayon du graphique en secteurs.                                             |
|          | `counterclock`     | Si True, les secteurs sont tracés dans le sens antihoraire.                 |
|          | `pctdistance`      | Distance du centre pour les étiquettes de pourcentage.                      |
| `subplot`| `nrows`            | Nombre de lignes dans la grille de sous-graphiques.                         |
|          | `ncols`            | Nombre de colonnes dans la grille de sous-graphiques.                       |
|          | `index`            | Index du sous-graphe (commence à 1, va de gauche à droite, puis de haut en bas). |
|          | `sharex`           | Si True, partage l'axe x avec les autres sous-graphiques.                   |
|          | `sharey`           | Si True, partage l'axe y avec les autres sous-graphiques.                   |
|          | `figsize`          | Taille de la figure (largeur, hauteur) en pouces.                           |
|          | `subplot_kw`       | Dictionnaire de mots-clés pour les sous-graphiques.                         |
|          | `gridspec_kw`      | Dictionnaire de mots-clés pour le placement des sous-graphiques.            |

Pour tout savoir sur Matplotlib: [Site officiel Matplotlib](https://matplotlib.org/stable/ "Matplotlib").

## Atelier

[La bibliothèque Matplotlib](../atelier-Matplotlib.ipynb)  

[Fichier ventes.csv](../ventes.csv)