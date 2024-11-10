+++
title = "Matpotlib"
weight = 121
+++

![Bibliohèque MatplotLib](../matplotlib.jpg?width=30vw)

Matplotlib est une bibliothèque de visualisation de données en Python qui permet de créer une grande variété de graphiques.

## Installation de Matplotlib (déjà fait sur les ordinateurs du cégep)

Avant de commencer, assurez vous d'avoir Matplotlib installé. Vous pouvez l'installer via pip :

```bash
pip install matplotlib
```

## Importation de Matplotlib

Pour utiliser Matplotlib, vous devez en premier l'importer dans votre code.

```python
import matplotlib.pyplot as plt
```

Pour vérifier que Matplotlib est bien installé sur votre environnement:

```python
# Version de Matplotlib
plt.__version__
```

## Étapes des base pour créer et mettre en forme un graphique

### Création d'un graphique simple

Pour créer un graphique simple, utilisez la fonction `plot()`.

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Création du graphique
plt.plot(x, y)

# Affichage du graphique
plt.show()
```

| Méthode       	 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `plt.plot(x, y)`       | Crée un graphique en ligne avec les valeurs de `x` et `y`.                  |
| `plt.show()`           | Affiche le graphique créé.                                                  |

![graphe 1](../graphe1.png?width=50vw)

### Ajout de titres

Vous pouvez ajouter des titres au graphique et aux axes pour rendre le graphique plus informatif.

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Création du graphique
plt.plot(x, y)

# Ajout de titres
plt.title('Graphique simple')
plt.xlabel("L'axe X")
plt.ylabel("L'axe Y")

# Affichage du graphique
plt.show()
```

| Méthode       | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `plt.title('Graphique simple')` | Ajoute un titre au graphique avec le texte 'Graphique simple'.      |
| `plt.xlabel("L'axe X")` | Ajoute une étiquette à l'axe des abscisses (x) avec le texte "L'axe X".     |
| `plt.ylabel("L'axe Y")` | Ajoute une étiquette à l'axe des ordonnées (y) avec le texte "L'axe Y".     |

![graphe 2](../graphe2.png?width=50vw)

### Personnalisation des styles de ligne et des couleurs

Matplotlib permet de personnaliser les styles de ligne et les couleurs.

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Création du graphique avec personnalisation
plt.plot(x, y, color='green', linestyle='--', marker='o')

# Ajout de titres
plt.title('Graphique personnalisé')
plt.xlabel("L'axe X")
plt.ylabel("L'axe Y")

# Affichage du graphique
plt.show()
```

| Méthode       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `plt.plot(x, y,`<br>`color='green',`<br>`linestyle='--',`<br>`marker='o')` | Crée un graphique en ligne avec les valeurs de `x` et `y`, en utilisant des paramètres supplémentaires pour personnaliser l'apparence de la ligne : `color='green'` pour la couleur verte, `linestyle='--'` pour une ligne en pointillés, et `marker='o'` pour des marqueurs en forme de cercle sur chaque point de données. |

![graphe 3](../graphe3.png?width=50vw)

**Liste de marqueurs**

Voici un tableau de quelques marqueurs possibles:

| Marqueur         | Description             |
|------------------|-------------------------|
| `'.'`            | Point                   |
| `','`            | Pixel                   |
| `'o'`            | Cercle                  |
| `'v'`            | Triangle                |
| `'s'`            | Carré                   |
| `'p'`            | Pentagone               |
| `'*'`            | Étoile                  |
| `'h'`,  `'H'`    | Hexagone                |
| `'+'`            | Plus                    |
| `'x'`            | Croix                   |
| `'D'`, `'d'`     | Diamant                 |
| `'\|'`           | Ligne verticale         |
| `'_'`            | Ligne horizontale       |

### Ajout de légende

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Création du graphique avec personnalisation
plt.plot(x, y, color='green', linestyle='--', marker='o', label='Croissance')

# Ajout de titres
plt.title('Graphique personnalisé')
plt.xlabel("L'axe X")
plt.ylabel("L'axe Y")

# Ajout de la légende
plt.legend()

# Affichage du graphique
plt.show()
```

![graphe 6](../graphe6.png?width=50vw)

## Définir les étiquettes de graduations des axes x et y

Les fonctions `xticks()` et `yticks()` sont utilisées pour obtenir ou définir les étiquettes des graduations sur les axes x et y d’un graphique.

```python
import matplotlib.pyplot as plt

# Exemple de données
x = [0, 1, 2, 3, 4]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)

# Définir les étiquettes des graduations de l'axe x
plt.xticks([0, 1, 2, 3, 4], ['A', 'B', 'C', 'D', 'E'])

# Définir les étiquettes des graduations de l'axe y
plt.yticks([10, 20, 30, 40], ['Dix', 'Vingt', 'Trente', 'Quarante'])

plt.show()
```

| Méthode              | Description                                                   |
|----------------------|---------------------------------------------------------------|
| `plt.xticks`         | Définit ou obtient les étiquettes des graduations de l’axe x. |
| `plt.yticks`         | Définit ou obtient les étiquettes des graduations de l’axe y. |


![graphe 8](../graphe8.png?width=50vw)


## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)

### Création de graphiques multiples

Vous pouvez créer plusieurs graphiques dans une seule figure en utilisant `subplot()`.

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Création de la figure
plt.figure()

# Premier graphique
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title('Premier graphique')

# Deuxième graphique
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title('Deuxième graphique')

# Affichage des graphiques
plt.tight_layout()
plt.show()
```

| Méthode                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `plt.figure()`         | Crée une nouvelle figure dans laquelle vous pouvez tracer vos graphiques. |
| `plt.subplot(2, 1, 2)` | Crée un sous-graphique dans une grille de 2 lignes et 1 colonne, et place ce sous-graphique dans la deuxième position (en bas). Cela permet de créer plusieurs graphiques dans une seule figure. |
| `plt.tight_layout()`   | Ajuste automatiquement les paramètres des sous-graphiques pour qu'ils s'adaptent proprement à la zone de la figure, en évitant les chevauchements entre les étiquettes, les titres et les axes. |

![graphe 4](../graphe4.png?width=50vw)

## Sauvegarde du graphique

Vous pouvez sauvegarder le graphique dans un fichier en utilisant `savefig()`.

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Création du graphique
plt.plot(x, y)

# Ajout de titres
plt.title('Graphique à sauvegarder')
plt.xlabel("L'axe X")
plt.ylabel("L'axe Y")

# Sauvegarde du graphique
plt.savefig('graphique.png')

# Affichage du graphique
plt.show()
```

| Méthode                      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `plt.savefig`                | Enregistre le graphique actuel dans le fichier spécifié. Le format du fichier peut être `PNG`, `JPG`, `PDF`, `SVG`, etc. On peut inclure un chemin pour spécifier où enregistrer le fichier.                 |                     

![graphe 5](../graphe5.png?width=50vw)

## Les différents types de graphiques

En plus des graphiques de type ligne, Matplotlib permet de créer une multitude d'autres graphiques.

### Histogramme

```python
import matplotlib.pyplot as plt

donnees = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(donnees, bins=5, range=(1, 5), density=False, cumulative=False, color='green', edgecolor='black')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('Histogramme')
plt.show()
```

| Méthode              | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| `plt.hist`           | Fonction pour créer un histogramme à partir des données fournies.                               |
|            | `donnees`: Les données à analyser et à représenter sous forme d'histogramme. `bins=5`le nombre de barres dans l'histogramme. `range=(1, 5)` la plage de valeurs à inclure dans l'histogramme. `density=False`: Si `True`, l'histogramme affiche une densité de probabilité plutôt que le nombre brut d'observations. `cumulative=False` Si `True`, l'histogramme est cumulatif, affichant la somme des fréquences jusqu'à chaque point. `color='green'`et `edgecolor='black'`couleurs des barres de l'histogramme et des contours des barres.                         |

![Histogramme](../matplotlib-histo.png?width=50vw)

### Graphique en barres

```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
valeurs = [3, 7, 5, 4]

plt.bar(categories, valeurs)
plt.xlabel('Catégories')
plt.ylabel('Valeurs')
plt.title('Graphique en barres')
plt.show()
```

| Méthode        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `plt.bar`      | Fonction pour créer un diagramme à barres. `categories`: la liste des catégories ou étiquettes pour chaque barre. `valeurs`: La liste des valeurs correspondant à la hauteur de chaque barre.  |                                 

![Graphique en barres](../matplotlib-barres.png?width=50vw)

#### Différence entre un histogramme et un graphique en barres

- **Histogramme** : Utilisé pour montrer la **distribution d'un ensemble de données continues**. Les données sont regroupées en intervalles, et chaque barre représente le nombre de données dans chaque intervalle. Par exemple, un histogramme peut montrer la distribution des âges d'un groupe de personnes.

- **Graphique en barres** : Utilisé pour **comparer des catégories distinctes**. Chaque barre représente une catégorie et la hauteur de la barre montre la valeur de cette catégorie. Par exemple, un graphique en barres peut montrer les ventes de différents produits.

En résumé, un histogramme montre la distribution d'un ensemble de données continues, tandis qu'un graphique en barres compare des catégories distinctes.

### Graphique en secteurs

{{% notice style=warning title=Attention %}}
Un graphique en secteurs ne peut pas contenir des valeurs négatives. Avant de créer le graphique il faut filtrer les données pour ne garder que les données positives.
{{% /notice %}}

```python
import matplotlib.pyplot as plt

# Données
etiquettes = ['A', 'B', 'C', 'D']
tailles = [15, 30, 45, 10]
secteur = (0, 0.1, 0, 0)  # Décale le deuxième secteur

# Création du graphique en secteurs
plt.pie(tailles, explode=secteur, labels=etiquettes, colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'],
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Assure que le graphique est circulaire
plt.title('Graphique en secteurs')
plt.show()
```

Voici une explication simple des deux méthodes `plt.pie` et `plt.axis('equal')` dans Matplotlib, présentée sous forme de tableau :

| Méthode                    | Description                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `plt.pie`                  | Fonction pour créer un graphique circulaire (camembert). `tailles`: Les valeurs déterminant la taille de chaque secteur (portion) du camembert. `explode=secteur`:   Liste déterminant quelle portion est décalée (mise en avant). `labels=etiquettes`: Étiquettes pour chaque secteur, décrivant ce que chaque portion représente. `colors`:  Liste des couleurs utilisées pour chaque secteur. `autopct='%1.1f%%'`: Affiche le pourcentage de chaque secteur à l'intérieur de celui-ci, formaté à une décimale près. `shadow=True`:  Ajoute une ombre au graphique pour un effet de profondeur. `startangle=140`: Angle de départ pour le premier secteur. 
|`plt.axis('equal')` | Assure que le graphique est parfaitement circulaire en réglant les axes x et y à la même échelle.                              |

![Graphique en secteurs](../matplotlib-secteur.png?width=50vw)

#### Ajouter une légende à un graphique en secteur

Ajouter une légende à un graphique en secteur est assez simple avec matplotlib.

1. **Créer le graphique en secteur** :
   - Utilise la fonction `plt.pie()` pour créer le graphique en secteur.
2. **Capturer les éléments du graphique** :
   - La fonction `plt.pie()` peut renvoyer des objets que tu peux utiliser pour créer la légende. Par exemple, tu peux capturer les "secteurs" (les parts du camembert) et les "étiquettes".
3. **Ajouter la légende** :
   - Utilise la fonction `plt.legend()` pour ajouter la légende au graphique. Tu peux spécifier les éléments capturés et leur position.

Voici un exemple de code :

```python
import matplotlib.pyplot as plt

# Données
etiquettes = ['A', 'B', 'C', 'D']
tailles = [15, 30, 45, 10]
secteur = (0, 0.1, 0, 0)  # Décale le deuxième secteur

# Créer le graphique en secteur
plt.figure(figsize=(10, 7))
secteurs, texts, autotexts = plt.pie(tailles, labels=etiquettes, autopct='%1.1f%%', startangle=140)

# Ajouter une légende
plt.legend(secteurs, etiquettes, title="Légende", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ajouter un titre
plt.title('Graphique en secteurs')

# Afficher le graphique
plt.show()
```

### Explication :
- **`secteurs, etiquettes, autotexts = plt.pie(...)`** : Cette ligne crée le graphique en secteur et capture les éléments nécessaires pour la légende.

![Graphique en secteurs avec légende](../matplotlib-secteur-legende.png?width=50vw)

### Graphique en nuages de points

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
tailles = [20, 50, 80, 200, 500]
plt.scatter(x, y, s=tailles)
plt.xlabel('Axe x')
plt.ylabel('Axe y')
plt.title('Graphique en nuage de points')
plt.show()
```

| Méthode                    | Description                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `plt.scatter`                 |  utilisée pour tracer un graphique en nuage de points. **`x` et `y`** : les coordonnées des points sur le graphique. - **`s=tailles`** : L'argument `s` définit la taille des marqueurs de chaque point. Cela peut être une valeur unique qui s'applique à tous les points, ou une liste de valeurs qui spécifie une taille différente pour chaque point. 

![Graphique en nuage](../matplotlib-nuage.png?width=50vw)


## Quelques méthodes

| Méthode        | Description                                                              |
|-------------------------|--------------------------------------------------------------------------|
| `plt.plot()`            | Crée un graphique linéaire.                                              |
| `plt.hist()`            | Crée un histogramme.                                                     |
| `plt.bar()`             | Crée un graphique en barres.                                             |
| `plt.scatter()`         | Crée un graphique en dispersion.                                         |
| `plt.xlabel()`          | Ajoute une étiquette à l'axe des abscisses.                              |
| `plt.ylabel()`          | Ajoute une étiquette à l'axe des ordonnées.                              |
| `plt.title()`           | Ajoute un titre au graphique.                                            |
| `plt.show()`            | Affiche le graphique.                                                    |
| `plt.savefig()`         | Enregistre le graphique sous forme d'image.                              |
| `fig, ax = plt.subplots()`| Crée une figure et des axes, permettant des graphes plus complexes.    |
| `fig = plt.figure(figsize=(width, height)`| `figsize` : Une tuple (largeur, hauteur) en pouces, définissant la taille de la figure.|
| `plt.grid()`            |  Afficher ou masquer la grille quadrillée sur un graphique.              |

## Les paramètres des méthodes de traçage

- Voici un tableau listant les paramètres des méthodes `plot`, `hist`, `scatter`, `pie` avec leurs descriptions :

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

Pour tout savoir sur Matplotlib: [Site officiel Matplotlib](https://matplotlib.org/stable/ "Matplotlib").

## Liste de couleurs
### Couleurs de bases
![Base](../sphx_glr_named_colors_001.webp)

### Couleurs type CSS
![Avancé](../sphx_glr_named_colors_003.webp)


## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)