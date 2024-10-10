+++
title = "Les fonctions prédéfinies"
weight = 81
+++

![Fonctions prédéfinies](../fn-predefinies.jpeg?width=25vw)

Les sous-programmes, aussi appelés `fonctions`, sont des blocs de **code réutilisables** qui permettent de structurer et d'organiser un programme. Ils facilitent la maintenance et la lisibilité du code. 

Python fourni des fonctions prédéfinies, qui permettent de réaliser des tâches courantes sans avoir à écrire beaucoup de code. Vous en connaissez déjà quelques-unes.

## Quelques fonctions de base

- `print()`
- `len()`
- `int()`, `float()`, `str()`, `bool()`
- `round()`
- etc.

Voyons d'autres fonctions prédéfinies utiles.

## Les fonctions mathématiques

Pour utiliser ces fonctions, vous devez d'abord importer le module math dans votre code.

```python
import math
```

### La fonction `abs()`

La fonction `abs()` retourne la valeur absolue d'un nombre.

```python
print(abs(-5))  # Affiche 5
```

### La fonction `sqrt()`

La fonction `math.sqrt(x)` retourne la racine carrée de `x`.

```python
import math

# Calcul de la racine carrée de 16
resultat = math.sqrt(16)
print(resultat)  # Affiche 4.0

# Calcul de la racine carrée de 2
resultat = math.sqrt(2)
print(resultat)  # Affiche environ 1.4142135623730951
```

### La fonction `log()`

La fonction `math.log(x, base)` retourne le logarithme de `x` dans la base spécifiée. Si la base n'est pas spécifiée, elle utilise la base naturelle `e`.

```python
import math

# Logarithme naturel de 10
resultat = math.log(10)
print(resultat)  # Affiche environ 2.302585092994046

# Logarithme de 8 en base 2
resultat = math.log(8, 2)
print(resultat)  # Affiche 3.0

# Logarithme de 100 en base 10
resultat = math.log(100, 10)
print(resultat)  # Affiche 2.0
```

### La fonction `exp()`

La fonction `math.exp(x)` retourne `e` (la base des logarithmes naturels) élevé à la puissance `x`.


```python
import math

# Calcul de e^1
resultat = math.exp(1)
print(resultat)  # Affiche environ 2.718281828459045

# Calcul de e^2
resultat = math.exp(2)
print(resultat)  # Affiche environ 7.3890560989306495

# Calcul de e^0
resultat = math.exp(0)
print(resultat)  # Affiche 1.0
```

Voici un tableau récapitulatif de quelques fonctions mathématiques prédéfinies en Python :

| **Fonction** | **Description** | **Exemple** |
|--------------|-----------------|-------------|
| `abs(x)`     | Retourne la valeur absolue de `x`. | `abs(-7) -> 7` |
| `round(x, n)`| Arrondit `x` à `n` décimales. | `round(3.14159, 2) -> 3.14` |
| `max(iterable)` | Retourne le plus grand élément d'un itérable. | `max([1, 2, 3]) -> 3` |
| `min(iterable)` | Retourne le plus petit élément d'un itérable. | `min([1, 2, 3]) -> 1` |
| `sum(iterable)` | Retourne la somme des éléments d'un itérable. | `sum([1, 2, 3]) -> 6` |
| `pow(x, y)`  | Retourne `x` élevé à la puissance `y`. | `pow(2, 3) -> 8` |
| `divmod(x, y)` | Retourne le quotient et le reste de la division de `x` par `y`. | `divmod(9, 4) -> (2, 1)` |
| `math.sqrt(x)` | Retourne la racine carrée de `x`. | `math.sqrt(16) -> 4.0` |
| `math.exp(x)`  | Retourne `e` élevé à la puissance `x`. | `math.exp(2) -> 7.3890560989306495` |
| `math.log(x, base)` | Retourne le logarithme de `x` dans la base spécifiée. | `math.log(8, 2) -> 3.0` |
| `math.sin(x)` | Retourne le sinus de `x` (en radians). | `math.sin(math.pi/2) -> 1.0` |
| `math.cos(x)` | Retourne le cosinus de `x` (en radians). | `math.cos(0) -> 1.0` |
| `math.tan(x)` | Retourne la tangente de `x` (en radians). | `math.tan(math.pi/4) -> 1.0` |



