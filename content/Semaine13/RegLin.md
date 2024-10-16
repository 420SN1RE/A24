+++
title = "Régression linéaire avec NumPy"
weight = 132
+++

![Régression linéaire](../regLineaire.png?width=20vw)


La régression linéaire est une technique statistique utilisée pour modéliser la relation entre une variable dépendante (souvent notée `y`) et une ou plusieurs variables indépendantes (notées `x`). En termes simples, c'est une méthode qui permet de tracer une ligne droite (appelée droite de régression) qui s'ajuste le mieux aux données.

## Calcul de la Régression Linéaire (à la main)

1. **Concept de base**:
   La formule de la régression linéaire simple est :
   \[
   y = ax + b
   \]
   où :
   - `y` est la variable dépendante.
   - `x` est la variable indépendante.
   - `a` est la pente de la ligne.
   - `b` est l'ordonnée à l'origine (le point où la ligne coupe l'axe des y).

2. **Calcul de `a` et `b`**:
   Pour trouver les valeurs de `a` et `b`, on utilise les formules suivantes :
   \[
   a = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}
   \]
   \[
   b = \frac{(\sum y)(\sum x^2) - (\sum x)(\sum xy)}{n(\sum x^2) - (\sum x)^2}
   \]
   où \(n\) est le nombre de points de données.

3. **Exemple en Python**:

   ```python
   # Données
   x = [1, 2, 3, 4, 5]
   y = [2, 3, 5, 7, 11]

   # Calcul des paramètres
   n = len(x)
   sum_x = sum(x)
   sum_y = sum(y)
   sum_x_sq = sum([i**2 for i in x])
   sum_xy = sum([x[i]*y[i] for i in range(n)])

   a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x**2)
   b = (sum_y * sum_x_sq - sum_x * sum_xy) / (n * sum_x_sq - sum_x**2)

   print(f'Pente (a): {a}')
   print(f'Ordonnée à l\'origine (b): {b}')
   ```

## Calcul de la Régression Linéaire avec NumPy

NumPy simplifie grandement le processus de calcul des paramètres de la régression linéaire. Voici comment :

1. **Utilisation de NumPy**:
   ```python
   import numpy as np

   # Données
   x = np.array([1, 2, 3, 4, 5])
   y = np.array([2, 3, 5, 7, 11])

   # Calcul des paramètres
   A = np.vstack([x, np.ones(len(x))]).T
   a, b = np.linalg.lstsq(A, y, rcond=None)[0]

   print(f'Pente (a): {a}')
   print(f'Ordonnée à l\'origine (b): {b}')
   ```

### Exercices Pratiques

#### Exercice 1: Régression linéaire en biologie

**Objectif**: Trouver la relation entre la concentration d'un nutriment dans le sol et la croissance des plantes.

**Données**: Un fichier CSV nommé `plantes.csv` contenant les colonnes `Concentration` (en ppm) et `Croissance` (en cm).

**Instructions**:
1. **Charger les données**:
    ```python
    import pandas as pd

    df = pd.read_csv('plantes.csv')
    x = df['Concentration'].values
    y = df['Croissance'].values
    ```

2. **Effectuer la régression linéaire sans bibliothèques**:
    ```python
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(x**2)
    sum_xy = sum(x * y)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x**2)
    b = (sum_y * sum_x_sq - sum_x * sum_xy) / (n * sum_x_sq - sum_x**2)

    print(f'Pente (m): {m}')
    print(f'Ordonnée à l\'origine (b): {b}')
    ```

3. **Effectuer la régression linéaire avec NumPy**:
    ```python
    import numpy as np

    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]

    print(f'Pente (m): {m}')
    print(f'Ordonnée à l\'origine (b): {b}')
    ```

4. **Visualiser les résultats**:
    ```python
    import matplotlib.pyplot as plt

    plt.scatter(x, y, label='Données')
    plt.plot(x, m*x + b, color='red', label='Régression linéaire')
    plt.xlabel('Concentration (ppm)')
    plt.ylabel('Croissance (cm)')
    plt.title('Croissance des plantes en fonction de la concentration de nutriments')
    plt.legend()
    plt.show()
    ```

#### Exercice 2: Régression linéaire en santé

**Objectif**: Trouver la relation entre l'âge et le taux de cholestérol.

**Données**: Un fichier CSV nommé `sante.csv` contenant les colonnes `Age` et `Cholestérol`.

**Instructions**:
1. **Charger les données**:
    ```python
    import pandas as pd

    df = pd.read_csv('sante.csv')
    x = df['Age'].values
    y = df['Cholestérol'].values
    ```

2. **Effectuer la régression linéaire sans bibliothèques**:
    ```python
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(x**2)
    sum_xy = sum(x * y)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x**2)
    b = (sum_y * sum_x_sq - sum_x * sum_xy) / (n * sum_x_sq - sum_x**2)

    print(f'Pente (m): {m}')
    print(f'Ordonnée à l\'origine (b): {b}')
    ```

3. **Effectuer la régression linéaire avec NumPy**:
    ```python
    import numpy as np

    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]

    print(f'Pente (m): {m}')
    print(f'Ordonnée à l\'origine (b): {b}')
    ```

4. **Visualiser les résultats**:
    ```python
    import matplotlib.pyplot as plt

    plt.scatter(x, y, label='Données')
    plt.plot(x, m*x + b, color='red', label='Régression linéaire')
    plt.xlabel('Age')
    plt.ylabel('Cholestérol (mg/dL)')
    plt.title('Cholestérol en fonction de l\'âge')
    plt.legend()
    plt.show()
    ```

