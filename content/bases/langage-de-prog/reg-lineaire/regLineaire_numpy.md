+++
title = "Calcul d'une droite de régression linéaire avec NumPy"
weight = 11
+++


Voici comment calculer une droite de régression linéaire en utilisant NumPy, une bibliothèque Python puissante pour les calculs numériques.

## Étapes du calcul

1. **Importer NumPy** :
   Tout d'abord, vous devez importer la bibliothèque NumPy.
   ```python
   import numpy as np
   ```

2. **Préparer les données** :
   Vous devez avoir deux ensembles de données : les valeurs de la variable indépendante (x) et les valeurs de la variable dépendante (y).
   ```python
   x = np.array([1, 2, 3, 4, 5])
   y = np.array([2, 3, 5, 7, 11])
   ```

3. **Calculer les coefficients de la croite de régression** :
   Utilisez les formules de la régression linéaire pour calculer les coefficients `a` (pente) et `b` (ordonnée à l'origine).

   - **Formule pour la pente `a` ** :
     $$ a = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2} $$
   - **Formule pour l'ordonnée à l'origine `b` ** :
     $$ b = \frac{(\sum y) - a(\sum x)}{n} $$

   Voici comment les calculer avec NumPy :
   ```python
   n = len(x)
   sum_x = np.sum(x)
   sum_y = np.sum(y)
   sum_xy = np.sum(x * y)
   sum_x2 = np.sum(x**2)

   a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
   b = (sum_y - a * sum_x) / n
   ```

4. **Calculer les valeurs prédites** :
   Utilisez les coefficients `a` et `b`  pour calculer les valeurs prédites de `y`  pour chaque valeur de `x` .
   ```python
   y_pred = a * x + b
   ```

5. **Tracer le graphique** :
   Utilisez Matplotlib pour tracer les points de données et la droite de régression.
   ```python
   import matplotlib.pyplot as plt

   plt.scatter(x, y, color='blue', label='Données réelles')
   plt.plot(x, y_pred, color='red', label='Régression linéaire')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.title('Régression Linéaire')
   plt.legend()
   plt.show()
   ```

#### Exemple Complet

Voici le code complet pour calculer et tracer une droite de régression linéaire avec NumPy :
```python
import numpy as np
import matplotlib.pyplot as plt

# Données
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Calcul des coefficients
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - a * sum_x) / n

# Valeurs prédites
y_pred = a * x + b

# Tracer le graphique
plt.scatter(x, y, color='blue', label='Données réelles')
plt.plot(x, y_pred, color='red', label='Régression linéaire')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Régression Linéaire')
plt.legend()
plt.show()
```