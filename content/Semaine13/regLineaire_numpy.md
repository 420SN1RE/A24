+++
title = "Calcul d'une droite de régression linéaire avec NumPy"
weight = 134
+++


Voici comment calculer une droite de régression linéaire en utilisant NumPy:

## Étapes du calcul

1. **Importer les bibliothèques nécessaires** :
   - Vous aurez besoin de NumPy pour les calculs mathématiques et de Matplotlib pour tracer les graphiques.

   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   ```

2. **Préparer les données** :
   - Supposons que vous avez deux ensembles de données : `x` (variable indépendante) et `y` (variable dépendante).

   ```python
   x = np.array([1, 2, 3, 4, 5])
   y = np.array([2, 4, 5, 4, 5])
   ```

{{% notice style=tip title=Astuce %}}
Ici, les données pourraient venir d'un DataFrame de pandas. [Voir comment ici](https://420sn1re.github.io/A24/semaine13/numpy/index.html#conversion-dun-dataframe-en-tableau-numpy)
{{% /notice %}}

3. **Calculer les coefficients de la droite de régression** :
   - **Rappel**: l'équation d'une droite est `y = ax + b` où `a` est la pente de la droite et b l'ordonnée à l'origine.
   - Utilisez `np.polyfit` pour calculer les coefficients de la droite de régression. Cette fonction prend en entrée les données `x` et `y`, ainsi que le degré du polynôme (1 pour une droite).

   ```python
   coefficients = np.polyfit(x, y, 1) 
   # ou plus clair
   pente, b = np.polyfit(x, y, 1) 
   ```

4. **Créer une fonction polynomiale** :
   - Utilisez `np.poly1d` pour créer une fonction polynomiale à partir des coefficients calculés. Cette fonction représente la droite de régression.

   ```python
   polynomial = np.poly1d(coefficients)
   ```

5. **Calculer les valeurs de la droite de régression** :
   - Appliquez la fonction polynomiale aux valeurs de `x` pour obtenir les valeurs correspondantes de la droite de régression.

   ```python
   regression_line = polynomial(x)
   ```

6. **Tracer les données et la droite de régression** :
   - Utilisez Matplotlib pour tracer les points de données et la droite de régression.

   ```python
   # La fonction scatter() trace le nuage de points
   plt.scatter(x, y, color='blue', label='Données')

   # La fonction plot() sert à tracer la droite de régression. Les paramètres essentiels sont x et y
   plt.plot(x, regression_line, color='red', label='Droite de régression') 

   # Ajout des titres
   plt.title("Régression linéaire")
   plt.xlabel("X")
   plt.ylabel("Y")
   plt.legend()
   plt.show()
   ```

Voici l'exemple complet :

```python
import numpy as np
import matplotlib.pyplot as plt

# Données
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calcul de la droite de régression linéaire
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
regression_line = polynomial(x)

# Tracer les points de données et la droite de régression
plt.scatter(x, y, color='blue', label='Données')
plt.plot(x, regression_line, color='red', label='Droite de régression')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Régression linéaire")
plt.legend()
plt.show()
```

## Comment interpréter les coefficients de la droite de régression linéaire ?

Interpréter une droite de régression linéaire est une compétence essentielle en analyse de données. Voici un guide simple pour comprendre cette interprétation :

1. **Pente de la droite** :
   - La pente indique la direction et la force de la relation entre les deux variables. Si la pente est positive, cela signifie que lorsque la variable indépendante (x) augmente, la variable dépendante (y) augmente également. Si la pente est négative, y diminue lorsque x augmente.

2. **Ordonnée à l'origine** :
   - L'ordonnée à l'origine est le point où la droite de régression croise l'axe des y. Elle représente la valeur de y lorsque x est égal à zéro. Bien que cette valeur puisse ne pas toujours avoir une signification pratique, elle est importante pour définir la droite.

3. **Visualisation** :
   - En traçant la droite de régression sur un graphique, on peut visualiser comment les points de données se répartissent par rapport à cette droite. Si les points sont proches de la droite, cela indique une bonne adéquation du modèle. Si les points sont dispersés, cela peut indiquer que d'autres facteurs influencent la variable dépendante.



![Régression linéaire](../regression.png?width=40vw)
