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
print(df.head())  # Affiche les 5 premières lignes du DataFrame
```

**Exemple**:
```plaintext
       Nom  Âge  Note
0    Aline   25  85.5
1   Robert   30  90.3
2  Charles   35  78.9
```

## Renommage de colonnes

Les colonnes peuvent être renommées pour une meilleure clarté.

```python
# Renommage des colonnes
df = df.rename(columns={"Nom": "Prénom"})
print(f"La colonne Nom modifiée \n{df}\n")
```

```plaintext
La colonne Nom modifiée 
    Prénom  Âge  Note
0    Aline   25  85.5
1   Robert   30  90.3
2  Charles   35  78.9
```

## Ajout et suppression de colonnes

Pour renommer une ou plusieurs colonnes :
```python
# Ajout d'une nouvelle colonne
df["Session"] = "Automne"
print(f"La colonne Session ajoutée \n{df}\n")

# Suppression d'une colonne
df = df.drop(columns=["Session"])
print(f"La colonne Session supprimée \n{df}\n")
```

```plaintext
La colonne Session ajoutée 
       Nom  Âge  Note  Session
0    Aline   25  85.5  Automne
1   Robert   30  90.3  Automne
2  Charles   35  78.9  Automne

La colonne Session supprimée 
       Nom  Âge  Note
0    Aline   25  85.5
1   Robert   30  90.3
2  Charles   35  78.9
```

## Informations sur le DataFrame

Pour obtenir des informations générales sur votre DataFrame, telles que le nombre de lignes et de colonnes, les types de données, etc. :
```python
print(df.info())
```
```plaintext
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Nom     3 non-null      object 
 1   Âge     3 non-null      int64  
 2   Note    3 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 204.0+ bytes
```

## Statistiques de base

Pandas offre des méthodes simples pour obtenir des statistiques de base sur vos données :
```python
print(df.describe())  # Affiche les statistiques descriptives des colonnes numériques
```

```plaintext
        Âge       Note
count   3.0   3.000000
mean   30.0  84.900000
std     5.0   5.723635
min    25.0  78.900000
25%    27.5  82.200000
50%    30.0  85.500000
75%    32.5  87.900000
max    35.0  90.300000
```

## Accès direct aux données

Vous pouvez accéder directement aux données d'une colonne du DataFrame.
```python
print(df["Âge"])  # Accède aux données de la colonne Âge
```

```plaintext
0    25
1    30
2    35
Name: Âge, dtype: int64
```

## Sélection et filtrage de données

Pour sélectionner des colonnes spécifiques :
```python
df_selection = df[['Colonne1', 'Colonne2']]  # Sélectionne les colonnes 'Colonne1' et 'Colonne2'
print(df_selection.head())
```

Pour filtrer les données selon une condition :
```python
df_filtre = df[df['Colonne'] > valeur]  # Filtre les lignes où les valeurs de 'Colonne' sont supérieures à 'valeur'
print(df_filtre.head())
```

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
valeurs = df.values	# Accède à la première ligne sous forme de tableau numpy
print(valeurs)
```

```plaintext
[['Aline' 25 85.5]
 ['Robert' 30 90.3]
 ['Charles' 35 78.9]]
```

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