+++
title = "Introduction à Pandas"
weight = 111
+++

![Bibliothèque Pandas](../pandas.jpg?width=25vw)


## Qu'est-ce que pandas ?

Pandas est une bibliothèque Python puissante et flexible utilisée pour la manipulation et l'analyse de données. Elle est particulièrement utile pour les scientifiques qui travaillent avec de grandes quantités de données.

## Installation de pandas

Avant de commencer, assurez-vous d'avoir pandas installé. Vous pouvez l'installer via pip :
```bash
pip install pandas
```

## Importation de pandas

Pour utiliser pandas, vous devez d'abord l'importer dans votre script Python :
```python
import pandas as pd
```

## La structure de données principale de Pandas

Un ***DataFrame*** est une structure de données bidimensionnelle fournie par la bibliothèque pandas en Python. Il ressemble à une feuille de calcul Excel, avec des lignes et des colonnes. Chaque colonne peut contenir des types de données différents (nombres, chaînes de caractères, etc.), ce qui le rend très flexible pour manipuler et analyser des données.

## Chargement des données à partir d'un fichier CSV

Le traitement des fichiers contenant des données est essentiel en programmation Python, en particulier dans le domaine des sciences de données.
CSV signifie ***Comma-Separated Values*** (valeurs séparées par des virgules). C'est un format de fichier simple utilisé pour stocker des données tabulaires, comme une feuille de calcul Excel.

Pandas fourni des fonctionnalités pour lire des fichiers csv ou en créer.

La première étape pour travailler avec des données est de les charger dans un DataFrame. Supposons que vous avez un fichier CSV nommé `data.csv` :

```python
df = pd.read_csv('data.csv')
```

## Affichage des données

Une fois les données chargées, vous pouvez les afficher pour avoir un aperçu :
```python
df.head()  # Affiche les 5 premières lignes du DataFrame
```

![5 premières lignes](../head.png?width=25vw)

```python
df.tail()  # Affiche les 5 dernières lignes du DataFrame
```
![5 dernières lignes](../tail.png?width=25vw)

## Renommage de colonnes

Les colonnes peuvent être renommées pour une meilleure clarté.

```python
# Renommage des colonnes
df = df.rename(columns={"Nom": "Prénom"})
print("La colonne Nom modifiée")
df
```

![Rename](../rename.png?width=25vw)

## Ajout et suppression de colonnes

Pour renommer une ou plusieurs colonnes :
```python
# Ajout d'une nouvelle colonne
df["Session"] = "Automne"
print("La colonne Session ajoutée")
df

# Suppression d'une colonne
df = df.drop(columns=["Session"])
print("La colonne Session supprimée")
df
```

![Session ajoutée](../session.png?width=25vw)

![Session supprimée](../session_suppr.png?width=25vw)

## Informations sur le *DataFrame*

Pour obtenir des informations générales sur votre *DataFrame*, telles que le nombre de lignes et de colonnes, les types de données, etc. :

```python
df.info()
```
```plaintext
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Prénom  8 non-null      object 
 1   Age     8 non-null      int64  
 2   Note    8 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 324.0+ bytes
```
On a bien les types de variables connus : `int`, `float`, `object` fait souvent référence au type `str`.

## Statistiques de base

Pandas offre des méthodes simples pour obtenir des statistiques de base sur vos données :

```python
df.describe()  # Affiche les statistiques descriptives des colonnes numériques
```

![describre](../describe.png?width=25vw)

## Accès direct aux données

Vous pouvez accéder directement aux données d'une colonne du DataFrame.
```python
df["Age"]  # Accède aux données de la colonne Age
```

```plaintext
0    25
1    30
2    35
3    42
4    55
5    67
6    37
7    23
Name: Age, dtype: int64
```

## Sélection et filtrage de données

Pour sélectionner des colonnes spécifiques :
```python
df_selection = df[['Colonne1', 'Colonne2']]  # Sélectionne les colonnes 'Colonne1' et 'Colonne2'
df_selection.head()
```

Pour filtrer les données selon une condition :
```python
df_filtre = df[df['Colonne'] > valeur]  # Filtre les lignes où les valeurs de 'Colonne' sont supérieures à 'valeur'
df_filtre.head()
```

{{%notice style="warning" title="Attention"%}}
Dans les chapitres précédents, on utilisait `and` et `or` pour combiner des comparaisons. Avec Pandas, il faut utiliser `&` pour `and` et `|` pour `or`.
{{% /notice%}}

## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)

### Grouper les données

Le groupement de données permet de calculer des statistiques agrégées pour des sous-ensembles de données.

![Avant groupe](../avant_groupe.png?width=30vw)

Ci-dessous, voici comment faire, sans utiliser les fonctionnalités avancées de Pandas et en utilisant les notions déjà vues dans ce cours.

#### Boucler sur une colonne pour effectuer des groupements

Calculons la moyenne pour les étudiants de l'automne.

1. On **filtre** notre jeu de données en rapport avec les données de la session d'Automne.
```python
df_automne = df[df["Session"] == "Automne"]
```

![Groupe Automne](../automne.png?width=35vw)

2. On **calcule la moyenne** des notes à l'aide d'une boucle `for`
```python
somme_note = 0
for note in df_automne["Note"]:
   somme_note = somme_note + note

moyenne = somme_note / len(df_automne)
print(f"La moyenne des étudiants de l'automne est de {round(moyenne,2)}%")
```
```plaintext
La moyenne des étudiants de l'automne est de 77.97%
```

## Identification des données manquantes dans un dataframe

L'utilisation de `isna` dans Pandas est très simple et pratique pour identifier les données manquantes dans un DataFrame.

La fonction `isna()` retourne un DataFrame de la même taille que l'original, mais avec des valeurs booléennes (`True` ou `False`). Chaque valeur `True` indique la présence d'une donnée manquante (comme `NaN`), tandis que `False` indique que la donnée est présente.

```python
import pandas as pd

# Exemple de DataFrame avec des valeurs manquantes
data = {'A': [1, 2, NaN, 4],
        'B': [NaN, 2, 3, 4],
        'C': [1, NaN, NaN, 4]}
df = pd.DataFrame(data)

# Utilisation de isna() pour identifier les valeurs manquantes
donnees_manquantes = df.isna()

print(donnees_manquantes)
```
```plaintext
       A      B      C
0  False   True  False
1  False  False   True
2   True  False   True
3  False  False  False
```

Dans cet exemple, `donnees_manquantes` sera un DataFrame où chaque `True` indique une valeur manquante dans le DataFrame original.

## Les attributs index et values des DataFrames

Pour accéder à l'index du DataFrame :
```python
index = df.index
print(index)
```

```plaintext
RangeIndex(start=0, stop=3, step=1)
```

Pour accéder aux valeurs du DataFrame sous forme de tableau :
```python
valeurs = df.values	# Accède à la première ligne sous forme de tableau numPy
print(valeurs)
```

```plaintext
[['Aline' 25 85.5]
 ['Robert' 30 90.3]
 ['Charles' 35 78.9]]
```

## Conversion d'un *DataFrame* en liste

La méthode `tolist()` est utilisée pour convertir un *DataFrame* en une liste. Chaque ligne du *DataFrame* sera un élément de la liste. C’est particulièrement utile lorsqu'on souhaite manipuler les données sans utiliser le dataframe. Par exemple, pour identifier et modifier les données manquantes (Ex.: *None* ou *NaN*).

{{%notice style="warning" title="Attention"%}}
**NB**: Le DataFrame **n'est pas modifié**, seule la liste le sera.
{{% /notice%}}

```python
import pandas as pd

# Charger les données dans un DataFrame
df = pd.read_csv('data.csv')

# Convertir le DataFrame en liste
liste = df.values.tolist()

# Remplacer les valeurs manquantes par 0
for ligne in liste:
    for i in range(len(ligne)):
        if ligne[i] != ligne[i]:
            ligne[i] = 0

# Afficher la liste modifiée
print(liste)
```

```plaintext
[['Aline', 25, 85.5, 'Laval'], ['Robert', 30, 0, 'Laval'], ['Charles', 35, 78.9, 'Montréal'], ['Sophie', 28, 0, 'Québec'], ['Luc', 22, 88.0, 'Sherbrooke'], ['Marie', 27, 0, 'Trois-Rivières'], ['Jean', 32, 92.3, 'Gatineau'], ['Paul', 29, 0, 'Saguenay'], ['Julie', 24, 81.7, 'Drummondville'], ['Marc', 31, 0, 'Longueuil']]
```

La condition `if ligne[i] != ligne[i]:` fonctionne grâce à une propriété unique des valeurs NaN (Not a Number) en Python. :

### Propriété des valeurs *NaN*

En Python, et plus généralement dans les langages de programmation, les valeurs `NaN` ont une propriété spéciale : elles ne sont pas égales à elles-mêmes. Cela signifie que si vous comparez une valeur `NaN` à elle-même, le résultat sera toujours `False`.

## Reconstruction d'un *DataFrame*

L'utilisation de `pd.DataFrame(donnees_nettoyees, columns=dataframe.columns)` permet reconstruire un *DataFrame* nettoyé avec les mêmes colonnes que l’original.

## Fonctions les plus utiles avec un DataFrame

| Fonction           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `df.head(n)`        | Affiche les premières `n` lignes du DataFrame.                                   |
| `df.tail(n)`        | Affiche les dernières  `n` lignes du DataFrame.                                   |
| `df.describe()`    | Fournit des statistiques descriptives pour les colonnes numériques.          |
| `df.info()`        | Affiche un résumé concis du DataFrame, y compris le type de données et les valeurs manquantes. |
| `df.shape`         | Renvoie les dimensions du DataFrame (nombre de lignes et de colonnes).       |
| `df.columns`       | Affiche les noms des colonnes du DataFrame.                                  |
| `df.dtypes`        | Affiche les types de données de chaque colonne.                              |
| `df.isnull()`      | Renvoie un DataFrame de la même forme indiquant les valeurs manquantes.      |
| `df.isna()` 	     | Renvoie un DataFrame de la même taille que l'original, mais avec `True` à la place d'une donnée manquante (comme `NaN`)|
| `df.dropna()`      | Supprime les lignes ou les colonnes contenant des valeurs manquantes.        |
| `df.fillna()`      | Remplit les valeurs manquantes avec une valeur spécifiée.                    |
| `df.sort_values()` | Trie les valeurs d'une ou plusieurs colonnes.                                |
| `df.merge()`       | Fusionne deux DataFrames en fonction d'une ou plusieurs colonnes clés.       |
| `df.apply()`       | Applique une fonction à chaque élément d'une colonne ou d'un DataFrame.      |


## Visualisation des données

Bien que Pandas ne soit pas une bibliothèque de visualisation, il s'intègre bien avec Matplotlib pour créer des graphiques simples.

{{% notice style=info %}}
Nous verrons comment utiliser la bibliothèque Matplotlib pour tracer des graphiques, la semaine prochaine.
{{% /notice %}}

Pour tout savoir sur Pandas: [Site officiel Pandas](https://pandas.pydata.org/ "Pandas").

## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)

## Présentation du projet final (Étape 1)

[Projet final](https://420sn1re.github.io/A24/semaine11/projet/index.html#projet-final)