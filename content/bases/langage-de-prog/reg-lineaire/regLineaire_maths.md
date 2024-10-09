+++
title = "La régression linéaire (mathématiquement)"
weight = 10
draft = true
+++

Le calcul d'une droite de régression linéaire consiste à trouver la meilleure droite qui passe à travers un ensemble de points de données. Cette droite est souvent exprimée par l'équation `(y = ax + b)`, où `a` est la pente et `b` est l'ordonnée à l'origine. Voici comment on peut calculer ces coefficients de manière mathématique.

### Étapes du calcul

1. **Définir les données** :
   Supposons que nous avons un ensemble de `n` points de données `((x_i, y_i))` pour `(i = 1, 2, ..., n)`.

2. **Formules pour les coefficients** :
   Les coefficients `a` (pente) et `b` (ordonnée à l'origine) sont calculés à l'aide des formules suivantes :
   ```math
   - Pente : `$$[ a = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2} ]$$`
   - Ordonnée à l’origine : `$$[ b = \frac{(\sum y) - a(\sum x)}{n} ]$$`
   ```
Ces formules permettent de calculer les coefficients `a` et `b` de la droite de régression linéaire, où :

`(n)` est le nombre de points de données.  
$(\sum xy)$ est la somme des produits des paires de valeurs `(x)` et `(y)`.  
$(\sum x)$ est la somme des valeurs `x`.  
$(\sum y)$ est la somme des valeurs `y`.  
$(\sum x^2)$ est la somme des carrés des valeurs `x`.

### Dérivation des formules

1. **Minimisation de l'erreur quadratique** :
   La droite de régression linéaire est celle qui minimise la somme des carrés des erreurs (différences entre les valeurs observées et les valeurs prédites). Cette somme des carrés des erreurs est donnée par :
   $$ S = \sum_{i=1}^{n} (y_i - (ax_i + b))^2 $$

2. **Calcul des dérivées partielles** :
   Pour minimiser `S`, nous prenons les dérivées partielles de `S` par rapport à `a` et `b`

   - **Dérivée partielle par rapport à `a`** :
     $$ \frac{\partial S}{\partial a} = -2 \sum_{i=1}^{n} x_i (y_i - ax_i - b) = 0 $$

   - **Dérivée partielle par rapport à `b`** :
     $$ \frac{\partial S}{\partial b} = -2 \sum_{i=1}^{n} (y_i - ax_i - b) = 0 $$

3. **Résolution des équations** :
   En résolvant ces équations simultanément, nous obtenons les formules pour `a` et `b`.

   - **Pour `a`** :
     $$ a = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2} $$

   - **Pour `b`** :
     $$ b = \frac{(\sum y) - a(\sum x)}{n} $$

### Exemple numérique

Supposons que nous avons les points de données suivants :

| x | y  |
|---|----|
| 1 | 2  |
| 2 | 3  |
| 3 | 5  |
| 4 | 7  |
| 5 | 11 |

Calculons les sommes nécessaires :

$\
\sum x = 1 + 2 + 3 + 4 + 5 = 15
\$

$
\sum y = 2 + 3 + 5 + 7 + 11 = 28
\$

$\
\sum xy = 1 \cdot 2 + 2 \cdot 3 + 3 \cdot 5 + 4 \cdot 7 + 5 \cdot 11 = 97
\$

$\
\sum x^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
\$

$\
n = 5
\$

Calculons `a` et `b` :  

$\
a = \frac{5 \cdot 97 - 15 \cdot 28}{5 \cdot 55 - 15^2} = \frac{485 - 420}{275 - 225} = \frac{65}{50} = 1.3
\$

$\
b = \frac{28 - 1.3 \cdot 15}{5} = \frac{28 - 19.5}{5} = \frac{8.5}{5} = 1.7
\$


Ainsi, l'équation de la droite de régression est :
$\ y = 1.3x + 1.7 \$

Cette droite représente la meilleure approximation linéaire des points de données donnés.