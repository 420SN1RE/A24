+++
title = "NumPy"
weight = 131
+++

![NumPy](../numpy.jpg?width=18vw)

NumPy (***Numerical Python***) est une bibliothèque pour le calcul scientifique en Python. Elle offre des structures de données (Tableaux et Matrices), des fonctions mathématiques pour manipuler les structures de données.
 
#### Installation

Pour installer NumPy, utilisez pip:
```bash
pip install numpy
```

## Création et manipulation de Tableaux

1. **Création de tableaux**:
    ```python
    import numpy as np

    # Création d'un tableau 1D
    a = np.array([1, 2, 3, 4, 5])
    
    # Création d'un tableau 2D (Matrice)
    b = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(a)
    print(b)
    ```

    ```plaintext
    [1 2 3 4 5]
    [[1 2 3]
     [4 5 6]]
    ```

2. **Accès aux éléments**:
    ```python
    # Accès à un élément du tableau 1D
    print(a[2])  # Affiche: 3
    
    # Accès à un élément du tableau 2D
    print(b[1, 2])  # Affiche: 6
    ```

3. **Opérations mathématiques**:
    ```python
    # Addition
    c = a + 10
    print(c)  # Affiche: [11 12 13 14 15]
    
    # Multiplication
    d = a * 2
    print(d)  # Affiche: [ 2  4  6  8 10]
    
    # Racine carrée
    e = np.sqrt(a)
    print(e)  # Affiche: [1.         1.41421356 1.73205081 2.         2.23606798]
    ```

4. **Statistiques**:
    ```python
    # Moyenne
    print(np.mean(a))  # Affiche: 3.0
    
    # Écart-type
    print(np.std(a))  # Affiche: 1.4142135623730951
    
    # Somme
    print(np.sum(a))  # Affiche: 15
    ```

5. **Manipulation de la forme des tableaux**:
    ```python
    # Redimensionnement
    b_reshaped = b.reshape(3, 2)
    print(b_reshaped)
    
    # Transpose
    b_transposed = b.T
    print(b_transposed)
    ```

    ```plaintext
    b transformé : 
    [[1 2]
     [3 4]
     [5 6]]
    b transposé : 
    [[1 4]
     [2 5]
     [3 6]]
    ```

## Tableau des fonctions et méthodes incontournables

| Méthode                     | Description                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------|
| `np.array()`                | Crée un tableau NumPy à partir d'une liste ou d'une liste de listes.              |
| `np.mean()`                 | Calcule la moyenne des éléments du tableau.                                       |
| `np.std()`                  | Calcule l'écart-type des éléments du tableau.                                     |
| `np.sum()`                  | Calcule la somme des éléments du tableau.                                         |
| `np.sqrt()`                 | Calcule la racine carrée des éléments du tableau.                                 |
| `np.reshape()`              | Change la forme du tableau sans modifier ses données.                             |
| `np.transpose()`            | Transpose le tableau (intervertit les lignes et les colonnes).                    |
| `np.arange()`               | Crée un tableau contenant une séquence d'entiers.                                 |
| `np.linspace()`             | Crée un tableau contenant une séquence de valeurs régulièrement espacées.        |
| `np.random.random()`        | Génère un tableau de dimensions spécifiées rempli de nombres aléatoires compris entre 0 et 1. |

### Exercices Pratiques

#### Exercice 1: Analyse des données de précipitations

Objectif: Calculer des statistiques descriptives des précipitations et visualiser les données.

Données: Un fichier CSV nommé `precipitations.csv` contenant les colonnes `Année` et `Précipitation` (en mm).

Instructions:
1. **Charger les données**:
    ```python
    import numpy as np
    import pandas as pd
    
    df = pd.read_csv('precipitations.csv')
    precipitations = df['Précipitation'].values
    ```

2. **Calculer des statistiques descriptives**:
    ```python
    moyenne = np.mean(precipitations)
    ecart_type = np.std(precipitations)
    somme = np.sum(precipitations)
    
    print(f'Moyenne: {moyenne}, Écart-type: {ecart_type}, Somme: {somme}')
    ```

3. **Visualiser les données avec Matplotlib**:
    ```python
    import matplotlib.pyplot as plt
    
    plt.plot(df['Année'], precipitations)
    plt.xlabel('Année')
    plt.ylabel('Précipitation (mm)')
    plt.title('Précipitations annuelles')
    plt.show()
    ```

#### Exercice 2: Analyse des données de patients

Objectif: Étudier la distribution d'âges des patients et comparer les taux de cholestérol par groupe d'âge.

Données: Un fichier CSV nommé `patients.csv` contenant les colonnes `Age`, `Sexe`, `Cholestérol`.

Instructions:
1. **Charger les données**:
    ```python
    import numpy as np
    import pandas as pd
    
    df = pd.read_csv('patients.csv')
    ages = df['Age'].values
    cholesterol = df['Cholestérol'].values
    ```

2. **Calculer des statistiques descriptives pour les âges**:
    ```python
    age_moyen = np.mean(ages)
    age_ecart_type = np.std(ages)
    
    print(f'Âge moyen: {age_moyen}, Écart-type: {age_ecart_type}')
    ```

3. **Créer des groupes d'âge**:
    ```python
    bins = np.arange(0, 101, 20)
    groups = np.digitize(ages, bins)
    ```

4. **Calculer la moyenne de cholestérol par groupe d'âge**:
    ```python
    cholesterol_moyen_par_groupe = [np.mean(cholesterol[groups == i]) for i in range(1, len(bins))]
    ```

5. **Visualiser les données avec Matplotlib**:
    ```python
    import matplotlib.pyplot as plt
    
    plt.bar(range(len(cholesterol_moyen_par_groupe)), cholesterol_moyen_par_groupe, tick_label=[f'{bins[i]}-{bins[i+1]-1}' for i in range(len(bins)-1)])
    plt.xlabel('Groupe d\'âge')
    plt.ylabel('Cholestérol moyen (mg/dL)')
    plt.title('Cholestérol moyen par groupe d\'âge')
    plt.show()
    ```