+++
title = "Pandas"
weight = 111
+++

![Bibliothèque Pandas](../pandas.jpg?width=25vw)

## Qu'est-ce que Pandas et pourquoi l'utiliser ?

Pandas a été développé pour fournir des structures de données flexibles et intuitives, permettant de **manipuler facilement des tableaux de données** avec des étiquettes de variables (colonnes) et d’individus (lignes).
Pandas a été créé par Wes McKinney en 2008, depuis, elle est devenue une bibliothèque de référence pour l’analyse de données en Python.
Pandas se distingue par sa capacité à manipuler des **données hétérogènes** et étiquetées, contrairement à **NumPy** qui est principalement utilisé pour les tableaux numériques homogènes. 
De plus, Pandas intègre des fonctionnalités de visualisation via Matplotlib
Les principales structures de données de Pandas sont les **Series** et les **DataFrames**.

## Utilisation de Pandas

Pour commencer, vous devez l'importer dans votre script Python :

```python
import pandas as pd
```

Pour vérifier que Pandas est bien installé sur votre environnement :

```python
# Version de Pandas
pd.__version__
```

## Les structures de données de base

### Les Series

- Une **Series** est une structure de données **unidimensionnelle** similaire à une liste ou un tableau. 
- Chaque élément d’une Series a un **index**, ce qui permet un accès rapide et efficace aux données.
- L'index du premier élément est 0, le deuxième élément 1, etc.
- Pour une Series de taille n éléments, les index seront donc de 0 à n-1.

#### Comment créer une Series ?

Pour créer une Series, vous pouvez utiliser une **liste**, un **dictionnaire** ou même un **tableau NumPy**. Voici quelques exemples :

````python
# Importation de la bibliothèque Pandas
import pandas as pd

# Création d'une Series à partir d'une liste
ma_serie = pd.Series([1, 3, 5, 7, 9])
print(ma_serie)

# Création d'une Series à partir d'un dictionnaire
data = {'a': 1, 'b': 2, 'c': 3}
ma_serie = pd.Series(data)
print(ma_serie)
````

#### Comment accéder et sélectionner des données dans une Series ?

Vous pouvez accéder aux éléments d’une Series en utilisant leur index :

````python
# Accès par position
print(ma_serie[0])  # La donnée en première position

# Accès par étiquette
print(ma_serie['a'])   # La donnée à l'index 'a'
````

## Les DataFrames

Un **DataFrame** est une structure de données **bidimensionnelle** avec des étiquettes de lignes et de colonnes. 
Il est similaire à une **feuille de calcul** ou une table de base de données.

#### Comment créer un DataFrame ?

Vous pouvez créer un DataFrame à partir de diverses sources de données, telles que des **listes de listes**, des **dictionnaires de listes**, ou des **fichiers CSV**.

````python
# Création d'un DataFrame à partir d'un dictionnaire de listes
data = {
    'Nom': ['Julie', 'Robert', 'Charles'],
    'Age': [25, 30, 35],
    'Ville': ['Montréal', 'Laval', 'Rimouski']
}
df = pd.DataFrame(data)
print(df)
````

#### Comment accéder et sélectionner des données dans un DataFrame ?

Vous pouvez sélectionner des colonnes, des lignes ou des sous-ensembles de données en utilisant des méthodes comme `loc` et `iloc`.

````python
# Sélection d'une colonne
print(df['Nom'])

# Sélection de plusieurs colonnes
print(df[['Nom', 'Age']])

# Sélection de lignes par étiquette
print(df.loc[0])

# Sélection de lignes par position
print(df.iloc[0])
````

## Le traitement de fichiers textes

Le traitement des fichiers texte, tels que les fichiers CSV, est essentiel en programmation Python, en particulier dans le domaine de la science des données.

## Introduction aux fichiers CSV

CSV signifie **Comma-Separated Values** (valeurs séparées par des virgules). C'est un format de fichier simple utilisé pour stocker des données tabulaires, comme une feuille de calcul Excel ou une base de données.

## Lecture d'un fichier CSV

La bibliothèque Pandas fournit une fonction `read_csv()` pour lire les fichiers CSV et les convertir en DataFrame.

```python
import pandas as pd

df = pd.read_csv('fichier.csv')
```
**Explications** :

- `pd.read_csv('fichier.csv')` : Cette fonction lit le fichier CSV nommé 'fichier.csv'. Le fichier est supposé se trouver dans le même répertoire que le script Python. La fonction retourne un DataFrame où chaque ligne du CSV devient une ligne dans le DataFrame, et les en-têtes de colonne du CSV deviennent les noms de colonne du DataFrame.

- `df = ` : Cette partie du code assigne le DataFrame retourné par `pd.read_csv('fichier.csv')` à la variable `df`. Après cette ligne de code, vous pouvez utiliser `df` pour vous référer au DataFrame.

## Écriture dans un fichier CSV

Pandas fournit également une fonction `to_csv()` pour écrire un DataFrame dans un fichier CSV.

```python
df.to_csv('nouveau_fichier.csv', index=False)
```

**Explications** :

- `df.to_csv()` : Cette fonction écrit le contenu du DataFrame `df` dans un fichier CSV.

- `'nouveau_fichier.csv'` : C'est l'argument de la fonction `to_csv()`, qui spécifie le nom du fichier CSV dans lequel les données seront écrites. Dans ce cas, le fichier s'appellera 'nouveau_fichier.csv'.

- `index=False` : C'est un autre argument de la fonction `to_csv()`. Lorsqu'il est défini sur `False`, cela signifie que les indices des lignes du DataFrame ne seront pas écrits dans le fichier CSV. Par défaut, `to_csv()` écrit les indices des lignes dans le fichier CSV, donc si vous ne voulez pas cela, vous devez spécifier `index=False`.

## Les paramètres de la méthode `read_csv`

| Paramètre          | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `filepath_or_buffer` | Chemin du fichier ou objet de type fichier à lire.                          |
| `sep`              | Caractère ou motif regex à utiliser comme délimiteur (par défaut ',').       |
| `delimiter`        | Alias pour `sep`.                                                            |
| `header`           | Ligne(s) à utiliser comme en-têtes de colonnes (par défaut 'infer').         |
| `names`            | Liste des noms de colonnes à utiliser.                                       |
| `index_col`        | Colonne(s) à utiliser comme index des lignes.                                |
| `usecols`          | Liste des colonnes à lire.                                                   |
| `dtype`            | Type de données pour les colonnes.                                           |
| `engine`           | Moteur de parsing à utiliser ('c' ou 'python').                              |
| `converters`       | Dictionnaire de fonctions de conversion pour les colonnes.                   |
| `true_values`      | Liste des valeurs à considérer comme True.                                   |
| `false_values`     | Liste des valeurs à considérer comme False.                                  |
| `skipinitialspace` | Ignore les espaces après le délimiteur.                                      |
| `skiprows`         | Lignes à ignorer au début du fichier.                                        |
| `skipfooter`       | Lignes à ignorer à la fin du fichier.                                        |
| `nrows`            | Nombre de lignes à lire.                                                     |
| `na_values`        | Valeurs supplémentaires à considérer comme NA/NaN.                           |
| `keep_default_na`  | Garde les valeurs par défaut comme NA/NaN.                                   |
| `na_filter`        | Détecte les valeurs NA/NaN.                                                  |
| `verbose`          | Affiche des informations supplémentaires lors de la lecture.                 |
| `skip_blank_lines` | Ignore les lignes vides.                                                     |
| `parse_dates`      | Tente de convertir les colonnes en dates.                                    |
| `infer_datetime_format` | Infère le format des dates.                                             |
| `keep_date_col`    | Garde la colonne d'origine après conversion en date.                         |
| `date_parser`      | Fonction pour analyser les dates.                                            |
| `dayfirst`         | Considère le premier jour dans les dates.                                    |
| `cache_dates`      | Met en cache les dates converties.                                           |
| `iterator`         | Retourne un objet d'itération.                                               |
| `chunksize`        | Nombre de lignes par itération.                                              |
| `compression`      | Type de compression à utiliser.                                              |
| `thousands`        | Caractère utilisé pour les séparateurs de milliers.                          |
| `decimal`          | Caractère utilisé pour le séparateur décimal.                                |
| `lineterminator`   | Caractère utilisé pour terminer les lignes.                                  |
| `quotechar`        | Caractère utilisé pour les citations.                                        |
| `quoting`          | Contrôle la citation des champs.                                             |
| `doublequote`      | Contrôle le doublement des citations.                                        |
| `escapechar`       | Caractère utilisé pour échapper les délimiteurs.                             |
| `comment`          | Caractère utilisé pour indiquer les commentaires.                            |
| `encoding`         | Encodage du fichier.                                                         |
| `encoding_errors`  | Gestion des erreurs d'encodage.                                              |
| `dialect`          | Dialecte à utiliser pour le parsing.                                         |
| `on_bad_lines`     | Action à prendre pour les lignes incorrectes.                                |
| `delim_whitespace` | Utilise les espaces comme délimiteurs.                                       |
| `low_memory`       | Utilise moins de mémoire lors de la lecture.                                 |
| `memory_map`       | Utilise la mémoire mappée pour la lecture.                                   |
| `float_precision`  | Précision des nombres flottants.                                             |
| `storage_options`  | Options de stockage supplémentaires.                                         |

## Les paramètres de la méthode `to_csv`

| Paramètre          | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `filepath_or_buffer` | Chemin du fichier ou objet de type fichier à lire.                          |
| `sep`              | Caractère ou motif regex à utiliser comme délimiteur (par défaut ',').       |
| `delimiter`        | Alias pour `sep`.                                                            |
| `header`           | Ligne(s) à utiliser comme en-têtes de colonnes (par défaut 'infer').         |
| `names`            | Liste des noms de colonnes à utiliser.                                       |
| `index_col`        | Colonne(s) à utiliser comme index des lignes.                                |
| `usecols`          | Liste des colonnes à lire.                                                   |
| `dtype`            | Type de données pour les colonnes.                                           |
| `engine`           | Moteur de parsing à utiliser ('c' ou 'python').                              |
| `converters`       | Dictionnaire de fonctions de conversion pour les colonnes.                   |
| `true_values`      | Liste des valeurs à considérer comme True.                                   |
| `false_values`     | Liste des valeurs à considérer comme False.                                  |
| `skipinitialspace` | Ignore les espaces après le délimiteur.                                      |
| `skiprows`         | Lignes à ignorer au début du fichier.                                        |
| `skipfooter`       | Lignes à ignorer à la fin du fichier.                                        |
| `nrows`            | Nombre de lignes à lire.                                                     |
| `na_values`        | Valeurs supplémentaires à considérer comme NA/NaN.                           |
| `keep_default_na`  | Garde les valeurs par défaut comme NA/NaN.                                   |
| `na_filter`        | Détecte les valeurs NA/NaN.                                                  |
| `verbose`          | Affiche des informations supplémentaires lors de la lecture.                 |
| `skip_blank_lines` | Ignore les lignes vides.                                                     |
| `parse_dates`      | Tente de convertir les colonnes en dates.                                    |
| `infer_datetime_format` | Infère le format des dates.                                             |
| `keep_date_col`    | Garde la colonne d'origine après conversion en date.                         |
| `date_parser`      | Fonction pour analyser les dates.                                            |
| `dayfirst`         | Considère le premier jour dans les dates.                                    |
| `cache_dates`      | Met en cache les dates converties.                                           |
| `iterator`         | Retourne un objet d'itération.                                               |
| `chunksize`        | Nombre de lignes par itération.                                              |
| `compression`      | Type de compression à utiliser.                                              |
| `thousands`        | Caractère utilisé pour les séparateurs de milliers.                          |
| `decimal`          | Caractère utilisé pour le séparateur décimal.                                |
| `lineterminator`   | Caractère utilisé pour terminer les lignes.                                  |
| `quotechar`        | Caractère utilisé pour les citations.                                        |
| `quoting`          | Contrôle la citation des champs.                                             |
| `doublequote`      | Contrôle le doublement des citations.                                        |
| `escapechar`       | Caractère utilisé pour échapper les délimiteurs.                             |
| `comment`          | Caractère utilisé pour indiquer les commentaires.                            |
| `encoding`         | Encodage du fichier.                                                         |
| `encoding_errors`  | Gestion des erreurs d'encodage.                                              |
| `dialect`          | Dialecte à utiliser pour le parsing.                                         |
| `on_bad_lines`     | Action à prendre pour les lignes incorrectes.                                |
| `delim_whitespace` | Utilise les espaces comme délimiteurs.                                       |
| `low_memory`       | Utilise moins de mémoire lors de la lecture.                                 |
| `memory_map`       | Utilise la mémoire mappée pour la lecture.                                   |
| `float_precision`  | Précision des nombres flottants.                                             |
| `storage_options`  | Options de stockage supplémentaires.                                         |

Pour plus de fonctions : [Site officiel Pandas](https://pandas.pydata.org/docs/reference/index.html "Pandas").

## Manipulation des données

Une fois que les données sont chargées dans un DataFrame, vous pouvez utiliser les nombreuses fonctionnalités de Pandas, pour manipuler les données. 
Par exemple, pour les nettoyer, filtrer les lignes, trier les données, grouper les données, etc.

## Manipulation de données

La manipulation de données est une étape importante dans l'analyse de données. Elle permet de **nettoyer**, **transformer** et **préparer les données** pour une analyse plus approfondie. Pandas offre une multitude de méthodes pour manipuler les données de manière efficace et flexible.

### Exploration des données

Avant de nettoyer les données, c'est important de comprendre la structure et le contenu de vos données. 
Pour obtenir un aperçu de vos données utilisez les méthodes suivantes:
- `head()` 
- `info()` et
- `describe()`.

```python
df.head()
df.head(n) # où n est le nombre de lignes à afficher
df.info()
df.describe()
df['colonne'].describe() # où 'colonne' est le nom de la colonne à afficher
````

### Nettoyage de données

Le nettoyage des données est souvent la première étape dans la manipulation de données. Cela inclut :
- la gestion des valeurs manquantes, 
- la suppression des doublons et 
- la correction des erreurs de données.

#### La gestion des valeurs manquantes

Les valeurs manquantes peuvent être gérées de différentes manières, comme les **supprimer** ou les **remplacer** par une valeur spécifique.

```python
import pandas as pd

# Création d'un DataFrame avec des valeurs manquantes
data = {'Nom': ['Julie', 'Robert', 'Charles'], 'Age': [25, None, 35], 'Ville': ['Montréal', 'Laval', None]}
df = pd.DataFrame(data)

# Suppression des lignes avec des valeurs manquantes
df_suppr = df.dropna()
print(df_suppr)

# Remplacement des valeurs manquantes par une valeur spécifique
df_remplace = df.fillna({'Age': df['Age'].mean(), 'Ville': 'Inconnue'})
print(df_remplace)
```

#### Traitement d'autres valeurs comme valeurs manquantes

La méthode `read_csv` fourni un paramètre `na_values` pour pouvoir spécifier d'autres valeurs que `NaN`(Not a Number) à considérer comme étant manquantes, lors de la lecture d'un fichier `csv`.

**`na_values`** : Ce paramètre spécifie quelles valeurs doivent être traitées comme NaN (Not a Number, utilisé pour représenter les données manquantes ou indéfinies) dans un DataFrame.

**Exemple** :

Supposons que vous ayez un fichier CSV nommé 'donnees.csv' qui ressemble à ceci :

```
age,poids,taille
25,70,1.75
30,"?",1.80
35,75,"n.a"
```

Dans ce fichier, les valeurs manquantes sont représentées par "?" et "n.a". 
Vous pouvez utiliser le paramètre `na_values` pour indiquer à pandas de traiter ces valeurs comme NaN (Not a Number) lors de la lecture du fichier. 

Voici comment :

```python
import pandas as pd

df = pd.read_csv('donnees.csv', na_values=["?", "n.a"])
```

Après l'exécution de ce code, le DataFrame `df` ressemblera à ceci :

```
   age  poids  taille
0   25   70.0    1.75
1   30    NaN    1.80
2   35   75.0     NaN
```

#### La suppression des doublons

Les doublons peuvent être supprimés pour éviter les erreurs dans l'analyse.

```python
# Suppression des doublons
df_unique = df.drop_duplicates()
print(df_unique)
```

#### La transformation de données

La transformation de données inclut :
- **l'ajout** de colonnes, 
- **la suppression** de colonnes, 
- la **modification** de colonnes, 
- l'application de fonctions sur les données.

##### L'ajout et la suppression de colonnes

Vous pouvez facilement ajouter ou supprimer des colonnes dans un DataFrame.

```python
# Ajout d'une nouvelle colonne
df['Pays'] = 'France'
print(df)

# Suppression d'une colonne
df = df.drop(columns=['Ville'])
print(df)
```

##### Renommage de colonnes

Les colonnes peuvent être renommées pour une meilleure clarté.

```python
# Renommage des colonnes
df = df.rename(columns={'Nom': 'Prenom', 'Age': 'Annees'})
print(df)
```

##### Application de fonctions

Vous pouvez appliquer des fonctions personnalisées à des colonnes ou à des lignes entières.

```python
# Application d'une fonction à une colonne
df['Age'] = df['Age'].apply(lambda x: x * 2 if pd.notnull(x) else x)
print(df)

# Application d'une fonction à l'ensemble du DataFrame
df = df.applymap(lambda x: str(x).upper() if isinstance(x, str) else x)
print(df)
```

## L'analyse de données

L'analyse de données inclut le calcul de statistiques descriptives, le filtre, le tri, le groupement de données et l'affichage de graphiques avec MatplotLib.

### Les statistiques descriptives

Pandas permet de calculer facilement des statistiques descriptives comme la moyenne, la médiane et l'écart-type.

```python
# Calcul de la moyenne et de l'écart-type
print(df['Age'].mean())
print(df['Age'].std())
```

### Filtrer les données

Le filtre de données permet de visualiser une catégorie précise de données

```python
df_filtre = df[df['Age'] > 18]

### Trier les données

Le tri de données permet de les visualiser dans une ordre précis

```python
df_trie = df.sort_values('Age')
```

### Grouper les données

Le groupement de données permet de calculer des statistiques agrégées pour des sous-ensembles de données.

```python
# Groupement par une colonne et calcul de la moyenne
groupe = df.groupby('Ville')['Age'].mean()
print(groupe)
```

## La manipulation de dates

La manipulation des dates et des heures est une compétence essentielle en programmation, notamment pour les applications de planification, d'analyse de données et de gestion de bases de données. Python offre plusieurs modules pour travailler avec les dates et les heures, dont le plus utilisé est le module `datetime`.

### Importation du module

Pour commencer à travailler avec les dates et les heures, vous devez importer le module `datetime` :

```python
import datetime
```

## Création d'objets Date et Heure

### Date

Pour créer un objet date, utilisez la classe `date` du module `datetime` :

```python
from datetime import date

# Créer une date pour le 22 mai 2023
ma_date = date(2023, 5, 22)
print(ma_date)  # Affiche : 2023-05-22
```

### Heure

Pour créer un objet heure, utilisez la classe `time` :

```python
from datetime import time

# Créer une heure pour 14h30m15s
mon_heure = time(14, 30, 15)
print(mon_heure)  # Affiche : 14:30:15
```

### Date et Heure

Pour combiner une date et une heure, utilisez la classe `datetime` :

```python
from datetime import datetime

# Créer une date et une heure pour le 22 mai 2023 à 14h30m15s
ma_datetime = datetime(2023, 5, 22, 14, 30, 15)
print(ma_datetime)  # Affiche : 2023-05-22 14:30:15
```

## Manipulation des Dates et Heures

### Extraction des composants

Vous pouvez extraire les composants individuels d'un objet date ou datetime :

```python
# Extraire l'année, le mois et le jour
annee = ma_date.year
mois = ma_date.month
jour = ma_date.day

print(annee, mois, jour)  # Affiche : 2023 5 22
```

### Calculs avec les dates

Le module `datetime` permet également de faire des calculs avec les dates en utilisant la classe `timedelta` :

```python
from datetime import timedelta

# Ajouter 10 jours à une date
nouvelle_date = ma_date + timedelta(days=10)
print(nouvelle_date)  # Affiche : 2023-06-01
```

### Formatage des dates

Pour afficher les dates dans différents formats, utilisez la méthode `strftime` :

```python
# Formatage de la date
date_formatee = ma_date.strftime("%d/%m/%Y")
print(date_formatee)  # Affiche : 22/05/2023
```

## Visualisation des données

Bien que Pandas ne soit pas spécialement conçu pour la visualisation, il offre une intégration avec la bibliothèque **Matplotlib**, permettant de créer rapidement des graphiques pour visualiser les données:

```python
# Tracer un histogramme de la colonne 'Taille'
df['Taille'].plot.hist()
```

**NB**: Pour tracer les graphiques, nous utiliserons la bibliothèque **Matplotlib**.

Pour tout savoir sur Pandas: [Site officiel Pandas](https://pandas.pydata.org/ "Pandas").

## Atelier

[La bibliothèque Pandas](../atelier-Pandas.ipynb)  

[Fichier iris.csv](../iris.csv)

