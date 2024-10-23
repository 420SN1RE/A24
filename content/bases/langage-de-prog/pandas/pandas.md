+++
alwaysopen = false
title = "Pandas (intermédiaire-avancé)"
weight = 9
+++

![Bibliothèque Pandas](../pandas.jpg?width=25vw)


## Qu'est-ce que pandas?

Pandas est une bibliothèque Python utilisée pour la manipulation et l'analyse de données. Elle est particulièrement utile pour traiter de grandes quantités de données expérimentales. 

Ce cours couvre les concepts de base de Pandas, en mettant l'accent sur les applications pratiques dans les sciences.

## Installation de Pandas

Avant de commencer, assurez vous d'avoir Pandas installé. Vous pouvez l'installer via pip :

```bash
pip install pandas
```

## Étape obligatoire pour utiliser Pandas

Pour commencer, vous devez l'importer dans votre code.

```python
import pandas as pd
```

Pour vérifier que Pandas est bien installé sur votre environnement :

```python
# Version de Pandas
pd.__version__
```

## Structures de données de base

### Les Series

Une `Series` est une structure de données **unidimensionnelle** semblable à une **liste**. Elle peut contenir des données de tout type (entiers, flottants, chaînes, etc.).

#### Création d'une série et accès à ses éléments

```python
import pandas as pd

# Création d'une Series
ma_serie = pd.Series([1, 2, 3, 4, 5])
print(f"La série:\n{ma_serie}")

# Accès par position
print(f"Premier élément: {ma_serie[0]}")  # La donnée en première position
```

**Affiche**:
```plaintext
La série:
0    1
1    2
2    3
3    4
4    5
dtype: int64
Premier élément: 1
```

### Les *DataFrames*

Un `DataFrame` est une structure de données **bidimensionnelle** avec des étiquettes de **lignes** et de **colonnes**. C'est l'équivalent d'une feuille de calcul comme Excel.

#### Création d'un *DataFrame*

```python
# Création d'un DataFrame
donnee = {
    "Nom": ["Aline", "Robert", "Charles"],
    "Âge": [25, 30, 35],
    "Note": [85.5, 90.3, 78.9]
}
df = pd.DataFrame(donnee)
print(df)
```

**Affiche**:
```plaintext
       Nom  Âge  Note
0    Aline   25  85.5
1   Robert   30  90.3
2  Charles   35  78.9
```

#### Création d'un *Dataframe* à partir d'une Serie

La méthode `to_frame()` permet de transformer une série en un DataFrame avec une seule colonne. Cela peut être utile lorsque vous souhaitez appliquer des opérations ou des méthodes spécifiques aux DataFrames sur une série.

```python
import pandas as pd

# Création d'une série
ma_serie = pd.Series([1, 2, 3, 4, 5], name='Valeurs')

# Conversion de la série en DataFrame
df = ma_serie.to_frame()

# Affichage du DataFrame
print(df)
```

**Affiche**:

```plaintext
   Valeurs
0        1
1        2
2        3
3        4
4        5
```

Dans cet exemple, `ma_serie` est convertie en un DataFrame `df` avec une seule colonne nommée "Valeurs". 

#### Accès aux colonnes et aux lignes d'un *DataFrame*

Les méthodes `df.loc` et `df.iloc` de pandas sont utilisées pour accéder aux données dans un *DataFrame*, mais elles fonctionnent de manière différente :

- **`df.loc`** : est basée sur les noms des lignes et des colonnes pour sélectionner les données. Par exemple :
  ```python
  df.loc['nom_ligne', 'nom_colonne']
  ```
  - **Avantages** : Plus intuitif lorsque vous travaillez avec des étiquettes de lignes et de colonnes.
  - **Inconvénients** : Peut être plus lent que `iloc` pour de grandes quantités de données.

- **`df.iloc`** : est basée sur les indices numériques des lignes et des colonnes pour sélectionner les données. Par exemple :
  ```python
  df.iloc[0, 1]
  ```
  - **Avantages** : Plus rapide et utile pour des opérations basées sur des positions.
  - **Inconvénients** : Moins intuitif si vous ne connaissez pas les positions exactes des lignes et des colonnes¹².

En résumé, utilisez `loc` lorsque vous travaillez avec des étiquettes et `iloc` lorsque vous travaillez avec des indice (nombres entiers).

**Exemples:**

```python
import pandas as pd

# Création du dataframe
donnee = {
    'Nom': ['Aline', 'Robert', 'Charles'],
    'Âge': [25, 30, 35],
    'Note': [85.5, 90.3, 78.9]
}
df = pd.DataFrame(donnee)
print(f"Le dataframe \n{df}")
print()

# Utilisation de df.loc
# Sélection de la ligne avec l'index 1 (Robert)
ligne_loc = df.loc[1]
print("Utilisation de df.loc pour sélectionner la ligne avec l'index 1:")
print(ligne_loc)

# Sélection des lignes avec les index 0 et 2 (Aline et Charles)
lignes_loc = df.loc[[0, 2]]
print("\nUtilisation de df.loc pour sélectionner les lignes avec les index 0 et 2:")
print(lignes_loc)

# Utilisation de df.iloc
# Sélection de la ligne à la position 1 (Robert)
ligne_iloc = df.iloc[1]
print("\nUtilisation de df.iloc pour sélectionner la ligne à la position 1:")
print(ligne_iloc)

# Sélection des lignes aux positions 0 et 2 (Aline et Charles)
lignes_iloc = df.iloc[[0, 2]]
print("\nUtilisation de df.iloc pour sélectionner les lignes aux positions 0 et 2:")
print(lignes_iloc)
```

Voici ce que fait chaque partie du code :

- `df.loc[1]` sélectionne la ligne avec l'index 1, c'est-à-dire la ligne correspondant à Robert.
- `df.loc[[0, 2]]` sélectionne les lignes avec les index 0 et 2, c'est-à-dire les lignes correspondant à Aline et Charles.
- `df.iloc[1]` sélectionne la ligne à la position 1, c'est-à-dire la ligne correspondant à Robert.
- `df.iloc[[0, 2]]` sélectionne les lignes aux positions 0 et 2, c'est-à-dire les lignes correspondant à Aline et Charles.

**Affiche** :

```plaintext
Le dataframe 
       Nom  Âge  Note
0    Aline   25  85.5
1   Robert   30  90.3
2  Charles   35  78.9

Utilisation de df.loc pour sélectionner la ligne avec l'index 1:
Nom     Robert
Âge         30
Note      90.3
Name: 1, dtype: object

Utilisation de df.loc pour sélectionner les lignes avec les index 0 et 2:
       Nom  Âge  Note
0    Aline   25  85.5
2  Charles   35  78.9

Utilisation de df.iloc pour sélectionner la ligne à la position 1:
Nom     Robert
Âge         30
Note      90.3
Name: 1, dtype: object

Utilisation de df.iloc pour sélectionner les lignes aux positions 0 et 2:
       Nom  Âge  Note
0    Aline   25  85.5
2  Charles   35  78.9
```

#### Ajout et suppression de colonnes

Vous pouvez facilement ajouter ou supprimer des colonnes dans un DataFrame.

```python
import pandas as pd

donnee = {
    'Nom': ['Aline', 'Robert', 'Charles'],
    'Âge': [25, 30, 35],
    'Note': [85.5, 90.3, 78.9]
}
df = pd.DataFrame(donnee)

# Ajout d'une nouvelle colonne
df["Session"] = "Automne"
print(f"La colonne Session ajoutée \n{df}\n")

# Suppression d'une colonne
df = df.drop(columns=["Session"])
print(f"La colonne Session supprimée \n{df}\n")
```

**Affiche**:

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

#### Renommage de colonnes

Les colonnes peuvent être renommées pour une meilleure clarté.

```python
# Renommage des colonnes
df = df.rename(columns={"Nom": "Prénom"})
print(f"La colonne Nom modifiée \n{df}\n")
```

**Affiche**:

```plaintext
La colonne Nom modifiée 
    Prénom  Âge  Note
0    Aline   25  85.5
1   Robert   30  90.3
2  Charles   35  78.9
```

#### Tri d'un *DataFrame*

Supposons que nous ayons un DataFrame `df` que nous voulons trier par la colonne `âge`.

```python
import pandas as pd

# Création du DataFrame
df = pd.DataFrame({
    'Nom': ['Aline', 'Robert', 'Charles'],
    'Âge': [25, 30, 35],
})

# Tri du DataFrame par la colonne 'âge'
df_trie = df.sort_values(by='Âge')

print(df_trie)
```

Dans cet exemple, nous avons un DataFrame `df` avec deux colonnes : `Nom` et `Âge`. La fonction `sort_values()` pour trier le DataFrame par la colonne `âge`. Le paramètre `by='âge'` indique la colonne sur laquelle nous voulons effectuer le tri.

**Affiche**:

```plaintext
       nom  âge
2  Charles   20
0    Aline   25
1   Robert   30
```

#### Fusion de *Dataframes*

Supposons que nous ayons deux DataFrames, `df1` et `df2`, que nous voulons fusionner sur une colonne commune appelée `id`.

```python
import pandas as pd

# Création des DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'prénom': ['Aline', 'Robert', 'Charles']
})

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'âge': [25, 30, 35]
})

# Fusion des DataFrames sur la colonne 'id'
df_fusionne = pd.merge(df1, df2, on='id', how='inner')

print(df_fusionne)
```

Dans cet exemple, nous avons deux DataFrames `df1` et `df2`. Nous utilisons la fonction `merge()` pour les fusionner sur la colonne `id`. Le paramètre `how='inner'` indique que nous voulons une jointure interne, ce qui signifie que seules les lignes avec des valeurs correspondantes dans les deux DataFrames seront incluses dans le résultat final.

**Affiche**:

```plaintext
   id     prénom  âge
0   1   Aline   25
1   2     Robert   30
```

## Gestion des données de type date

Travailler avec des données temporelles est essentiel dans de nombreuses disciplines scientifiques. Pandas rend cette tâche beaucoup plus simple en fournissant des outils pour manipuler et analyser les dates. 

### Conversion des chaînes de caractères en dates

Lorsque vous chargez des données, les dates peuvent être sous forme de chaînes de caractères. La première étape consiste donc à les convertir type `datetime`.

```python
import pandas as pd

# Chargement des données
donnees_date = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03'], 'Température': [20, 21, 19]}
df = pd.DataFrame(donnees_date)

# Conversion en datetime
df['Date'] = pd.to_datetime(df['Date'])

print(df)
```

**Affiche**:

```plaintext
        Date  Température
0 2024-01-01           20
1 2024-01-02           21
2 2024-01-03           19
```

### Extraction des composants de la date

Une fois les dates converties en `datetime`, vous pouvez extraire facilement des composants spécifiques comme l'année, le mois ou le jour.

```python
# Extraction de l'année
df['Année'] = df['Date'].dt.year

# Extraction du mois
df['Mois'] = df['Date'].dt.month

# Extraction du jour
df['Jour'] = df['Date'].dt.day

print(df)
```

**Affiche**:

```plaintext
        Date  Température  Année  Mois  Jour
0 2024-01-01           20   2024     1     1
1 2024-01-02           21   2024     1     2
2 2024-01-03           19   2024     1     3

```

### Manipulation des dates

Pandas permet aussi de faire des manipulations temporelles comme le filtrage par date, l'ajout de jours ou la création de plages de dates.

#### Filtrage par date

```python
# Filtrage pour obtenir les données de janvier 2024
masque = (df['Date'] >= '2024-01-01') & (df['Date'] <= '2024-01-31')
donnee_janvier = df.loc[masque]

print(donnee_janvier)
```

**Affiche**:

```plaintext
         Date  Température
0  2024-01-01           20
1  2024-01-02           21
2  2024-01-03           19
```

#### Ajout de jours

```python
# Ajout de 5 jours à chaque date
df['Date plus 5'] = df['Date'] + pd.Timedelta(days=5)

print(df)
```

**Affiche**:

```plaintext
        Date  Température Date plus 5
0 2024-01-01           20  2024-01-06
1 2024-01-02           21  2024-01-07
2 2024-01-03           19  2024-01-08
```

#### Création d'une plage de dates

```python
# Création d'une plage de dates (D = Day)
plage_date = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')

print(plage_date)
```

**Affiche**:

```plaintext
DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
               '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
               '2024-01-09', '2024-01-10'],
              dtype='datetime64[ns]', freq='D')
```

#### Exemple complet

```python
import pandas as pd

# Données
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'Température': [20, 21, 19]}
df = pd.DataFrame(data)

# Conversion en datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extraction des composants de la date
df['Année'] = df['Date'].dt.year
df['Mois'] = df['Date'].dt.month
df['Jour'] = df['Date'].dt.day

# Filtrage par date
masque = (df['Date'] >= '2024-01-01') & (df['Date'] <= '2024-01-31')
donnees_janvier = df.loc[masque]

# Ajout de jours
df['Date plus 5'] = df['Date'] + pd.Timedelta(days=5)

# Création d'une plage de dates
plage_date = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')

print(f"Le dataframe \n{df}\n")
print(f"Les données du mois de janvier \n{donnees_janvier}\n")
print(f"La plage de dates du 1er au 10 janvier 2024 \n{plage_date}\n")
```

**Affiche**:

```plaintext
Le dataframe 
        Date  Température  Année  Mois  Jour Date plus 5
0 2024-01-01           20   2024     1     1  2024-01-06
1 2024-01-02           21   2024     1     2  2024-01-07
2 2024-01-03           19   2024     1     3  2024-01-08

Les données du mois de janvier 
        Date  Température  Année  Mois  Jour
0 2024-01-01           20   2024     1     1
1 2024-01-02           21   2024     1     2
2 2024-01-03           19   2024     1     3

La plage de dates du 1er au 10 janvier 2024 
DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
               '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
               '2024-01-09', '2024-01-10'],
              dtype='datetime64[ns]', freq='D')

```

## Utilisation de fichiers de données

Le traitement des fichiers contenant des données est essentiel en programmation Python, en particulier dans le domaine des sciences de données.

### Introduction aux fichiers CSV

CSV signifie ***Comma-Separated Values*** (valeurs séparées par des virgules). C'est un format de fichier simple utilisé pour stocker des données tabulaires, comme une feuille de calcul Excel.

Pandas fourni des fonctionnalités pour lire des fichiers csv ou en créer.

### Importation et exportation de données

#### Lecture de fichiers CSV

Pandas permet de les lire facilement. Le code suivant, permet de lire le contenu du fichier **donnees.csv** et d'afficher  les premières lignes (par défaut 5). On peut préciser le nombre de ligne à afficher, en spécifiant une valeur dans `head()` par exemple `df.head(12)` affichera les 12 premières lignes du dataframe. 

```python
# Lecture d'un fichier CSV
df = pd.read_csv("donnees.csv")
print(df.head())
```

#### Écriture de fichiers CSV

Vous pouvez également écrire des données dans un fichier CSV.

```python
# Écriture d'un DataFrame dans un fichier CSV
df.to_csv("fichier.csv", index=False)
```
L'argument `index=False` est utilisé pour indiquer que vous ne souhaitez pas inclure l'index du dataframe dans le fichier CSV exporté. Par défaut, Pandas inclut l'index du dataframe comme première colonne dans le fichier CSV. En utilisant `index=False`, vous pouvez éviter cela.

Voici un exemple pour illustrer :

```python
import pandas as pd

# Création du dataframe
donnee = {
    'Nom': ['Aline', 'Robert', 'Charles'],
    'Âge': [25, 30, 35],
    'Note': [85.5, 90.3, 78.9]
}
df = pd.DataFrame(donnee)

# Exportation du dataframe en CSV sans l'index
df.to_csv("fichier-sans-index.csv", index=False)

# Exportation du dataframe en CSV avec l'index (par défaut)
df.to_csv("fichier-avec-index.csv")
```

Dans `fichier_sans_index.csv`, le fichier CSV n'aura pas de colonne d'index, tandis que dans `fichier_avec_index.csv`, la première colonne sera l'index du dataframe.

**Fichier csv avec index**

![Fichier avec index](../fichier_csv_avec_index.png?width=25vw)
[Fichier csv avec index](../fichier_avec_index.csv)

**Fichier csv sans index**

![Fichier sans index](../fichier_csv_sans_index.png?width=25vw)
[Fichier csv sans index](../fichier_sans_index.csv)


## Manipulation de données

### Sélection et filtrage de données

Vous pouvez sélectionner des **colonnes** spécifiques ou filtrer des **lignes** en fonction de conditions.

```python
# Sélection de colonnes
ages = df['Âge']
print(f"Les âges sont:\n{ages}\n")

# Filtrage de lignes
df_filtre = df[df['Note'] > 80]
print(f"Le dataframe contenant seulement les notes > 80 \n{df_filtre}\n")
```

**Affiche** :

```plaintext
Les âges sont:
0    25
1    30
2    35
Name: Âge, dtype: int64

Le dataframe contenant seulement les notes > 80 
      Nom  Âge  Note
0   Aline   25  85.5
1  Robert   30  90.3
```

### Gestion des valeurs manquantes

Les données expérimentales peuvent souvent contenir des valeurs manquantes. Pandas offre des méthodes pour les gérer.

**Remplissage des valeurs manquantes**:

```python
df.fillna(0, inplace=True)
```
Cette ligne remplace toutes les valeurs manquantes (NaN) dans le dataframe `df` par `0`. L'argument `inplace=True` signifie que la modification est faite directement sur le dataframe `df` sans créer une nouvelle copie.

**Suppression des lignes avec des valeurs manquantes**:

```python
df.dropna(inplace=True)
```
Cette ligne supprime toutes les lignes du dataframe `df` qui contiennent au moins une valeur manquante (NaN). Comme précédemment, `inplace=True` signifie que la modification est faite directement sur le dataframe `df`.

Si `inplace=False`, les modifications ne sont pas appliquées directement au dataframe original. Au lieu de cela, une nouvelle copie du dataframe avec les modifications est retournée. Le dataframe original reste inchangé.

## Analyse de données

### Statistiques descriptives

Pandas fournit des méthodes pour calculer des statistiques descriptives rapidement.

```python
# Statistiques descriptives
print(f"Statistiques : \n{df.describe()}\n")
```

**Affiche** :

```plaintext
Statistiques : 
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

La méthode `df.describe()` fournit des statistiques descriptives pour les colonnes numériques d’un dataframe. Voici les informations qu’elle donne :

| Statistique | Description |
|-------------|-------------|
| count       | Le nombre de valeurs non manquantes |
| mean        | La moyenne des valeurs |
| std         | L’écart type, qui mesure la dispersion des valeurs par rapport à la moyenne |
| min         | La valeur minimale |
| 25%         | Le premier quartile (25ème percentile), qui est la valeur en dessous de laquelle se trouvent 25% des données |
| 50%         | La médiane (50ème percentile), qui est la valeur en dessous de laquelle se trouvent 50% des données |
| 75%         | Le troisième quartile (75ème percentile), qui est la valeur en dessous de laquelle se trouvent 75% des données |
| max         | La valeur maximale |


### Groupement et agrégation

Le groupement et l'agrégation sont essentiels pour analyser des données catégorielles.

```python
import pandas as pd

# Création du DataFrame
data = {
    'Substance': ['Eau', 'Eau', 'Eau', 'Acide sulfurique', 'Acide sulfurique', 'Acide sulfurique', 'Sodium', 'Sodium', 'Sodium'],
    'Concentration (mol/L)': [0.1, 0.2, 0.3, 1.0, 1.5, 2.0, 0.5, 0.7, 0.9],
    'pH': [7.0, 7.1, 7.2, 1.0, 1.2, 1.5, 13.0, 13.2, 13.5],
    'Température (°C)': [25, 25, 25, 20, 20, 20, 30, 30, 30]
}

df = pd.DataFrame(data)

# Affichage du DataFrame
print(f"Affichage des données \n{df}\n")

# Grouper par la colonne Substance et calcul de la moyenne des autres colonnes
df_groupe = df.groupby("Substance").mean()
print(f"Affichage des données groupées par substance \n{df_groupe}\n")
```

**Affiche**:

```plaintext
Affichage des données 
          Substance  Concentration (mol/L)    pH  Température (°C)
0               Eau                    0.1   7.0                25
1               Eau                    0.2   7.1                25
2               Eau                    0.3   7.2                25
3  Acide sulfurique                    1.0   1.0                20
4  Acide sulfurique                    1.5   1.2                20
5  Acide sulfurique                    2.0   1.5                20
6            Sodium                    0.5  13.0                30
7            Sodium                    0.7  13.2                30
8            Sodium                    0.9  13.5                30

Affichage de la moyenne des données groupées par substance 
                  Concentration (mol/L)         pH  Température (°C)
Substance                                                           
Acide sulfurique                    1.5   1.233333              20.0
Eau                                 0.2   7.100000              25.0
Sodium                              0.7  13.233333              30.0
```

### Cas avertissement de *FutureWarning*

{{% notice style=warning title=Attention %}}
Si vous rencontrez un avertissement ***FutureWarning***: The default value of `numeric_only` in DataFrameGroupBy.mean is deprecated. In a future version, `numeric_only` will default to False. Either specify `numeric_only` or select only columns which should be valid for the function.*, vous devez soit spécifier explicitement `numeric_only=True` ou sélectionner uniquement les colonnes numériques avant d’appliquer la fonction mean()
{{% /notice %}}

**Exemple**: 

```python
donnee = {
    "Nom": ["Aline", "Robert", "Charles", "Julie"],
    "Âge": [25, 30, 35, 25],
    "Note": [85.5, 90.3, 78.9, 88.9]
}
df = pd.DataFrame(donnee)

df_groupe = df.groupby("Âge").mean(numeric_only=True)
print(f"Affichage de la moyenne des données groupées par âge \n{df_groupe}\n")
```

**Affiche**:

```plaintext
Affichage de la moyenne des données groupées par âge 
     Note
Âge      
25   87.2
30   90.3
35   78.9
```

### Les attributs index et values des *DataFrames* et des Series

1. **`.index`** :
   - **Définition** : L'attribut `.index` d'un DataFrame ou d'une Series représente les étiquettes des lignes. Pour un DataFrame, il s'agit des étiquettes des lignes, et pour une Series, il s'agit des étiquettes des éléments.
   - **Utilisation** : Il est souvent utilisé pour accéder ou manipuler les indices des données. Par exemple, dans une Series contenant des précipitations annuelles (Année, Précipitation), `.index` contiendrait les années.

```python
total_annee = df.groupby('Année')['Précipitation'].sum()
print(total_annee.index)  # Affiche les années
```

2. **`.values`** :
   - **Définition** : L'attribut `.values` d'un DataFrame ou d'une Series représente les données sous forme de tableau (numPy). Pour un DataFrame, il s'agit des valeurs de toutes les cellules, et pour une Series, il s'agit des valeurs des éléments.
   - **Utilisation** : Il est utilisé pour accéder directement aux valeurs des données sans les étiquettes. Par exemple, dans une Series contenant des précipitations annuelles (Année, Précipitation), `.values` contiendrait les valeurs des précipitations.

```python
total_par_annee = df.groupby('Année')['Précipitation'].sum()
print(total_par_annee.values)  # Affiche les précipitations totales pour chaque année
```

En résumé, `.index` vous donne les étiquettes des lignes (ou des éléments dans une Series), tandis que `.values` vous donne les valeurs des données.

## Fonctions et méthodes

Voici un tableau de quelques méthodes et fonctions incontournables en analyse de données scientifiques :

| Méthode/Fonction | Description |
|------------------|-------------|
| `read_csv()`     | Lire des fichiers CSV et les convertir en DataFrame |
| `head()`         | Afficher les premières lignes d'un DataFrame |
| `describe()`     | Fournir des statistiques descriptives pour les colonnes numériques d'un DataFrame |
| `info()`         | Afficher un résumé concis du DataFrame, y compris le type de données et les valeurs manquantes |
| `groupby()`      | Grouper les données par une ou plusieurs colonnes et appliquer des fonctions d'agrégation |
| `pivot_table()`  | Créer des tableaux croisés dynamiques pour résumer les données |
| `plot()`         | Générer des graphiques simples pour visualiser les données |
| `corr()`         | Calculer la matrice de corrélation entre les colonnes numériques |
| `merge()`        | Fusionner deux DataFrames sur une ou plusieurs colonnes clés |
| `dropna()`       | Supprimer les lignes ou colonnes contenant des valeurs manquantes |
| `fillna()`       | Remplace les lignes ou colonnes contenant des valeurs manquantes par une valeur donnée |
| `to_frame()`     | Transforme une série en un DataFrame avec une seule colonne |
| `sort_values()`  | Trie les valeurs d'une colonne d'un DataFrame |


## Visualisation de données

Bien que Pandas ne soit pas une bibliothèque de visualisation, il s'intègre bien avec Matplotlib pour créer des graphiques simples.

{{% notice style=info %}}
Nous verrons comment utiliser la bibliothèque Matplotlib pour tracer des graphiques, la semaine prochaine.
{{% /notice %}}

Pour tout savoir sur Pandas: [Site officiel Pandas](https://pandas.pydata.org/ "Pandas").
