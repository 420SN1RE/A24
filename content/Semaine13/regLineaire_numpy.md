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
Ici, les données pourraient venir d'un DataFrame de pandas. [Voir comment ici](http://localhost:1313/semaine13/numpy/#conversion-dun-dataframe-en-tableau-numpy)
{{% /notice %}}

3. **Calculer les coefficients de la droite de régression** :
   - Utilisez `np.polyfit` pour calculer les coefficients de la droite de régression. Cette fonction prend en entrée les données `x` et `y`, ainsi que le degré du polynôme (1 pour une droite).

   ```python
   coefficients = np.polyfit(x, y, 1)
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
   plt.scatter(x, y, color='blue', label='Données')
   plt.plot(x, regression_line, color='red', label='Droite de régression')
   plt.xlabel("X")
   plt.ylabel("Y")
   plt.title("Régression linéaire")
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

![Régression linéaire](../regression.png?width=40vw)
