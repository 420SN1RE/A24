+++
title = "Les opérateurs et les expressions booléennes"
weight = 41
+++

![Expressions booléennes](../exp_bool.jpeg?width=25vw)

### Les opérateurs de comparaison

Les **opérateurs de comparaison** permettent de comparer des valeurs et de déterminer si une condition est vraie ou fausse.

Soient `a = 10` et `b = 3`

|Opération (opérateur)   |Exemple|
|------------------------|-------|
|Égalité (`==`)            |`a == b` donne faux (`False`)|
|Inégalité (`!=`)          |`a != b` donne vrai (`True`)|
|Supérieur â (`>`)         |`a > b` donne vrai (`True`)|
|Inférieur à (`<`)         |`a < b` donne faux (`False`)|
|Supérieur ou égal â (`>=`)|`a >= b` donne vrai (`True`)|
|Inférieur ou égal à (`<=`)|`a <= b` donne faux (`False`)|

### Les opérateurs logiques

Les **opérateurs logiques** permettent de combiner des expressions booléennes.

Soient `x = True` et `y = False`

|Opération (opérateur)|Explication         |Exemple|
|---------------------|--------------------|------------
|Et (and)              |Renvoie `True` si les deux expressions sont vraies.|`a and b` donne `False`|
|Ou (or)               |Renvoie `True` si au moins l’une des expressions est vraie.|`a or b` donne True|
|Non (not)             |Inverse la valeur d’une expression (si c’était `True`, devient `False`, et vice versa).|`not a` donne False|

## Les priorités des opérateurs

La **priorité des opérateurs**, aussi appelée **précédence des opérateurs**, est la règle qui définit quel opérateur doit être évalué en premier dans une expression. 

Voici les niveaux de priorité en Python, du plus élevé au plus bas :
1. **Parenthèses (())** : Modifie la priorité normale des opérations.
2. **Exponentiation (\*\*)** : L’opérateur d’exponentiation a la plus haute priorité.
3. **Multiplication, Division, Division entière, Modulo (*, /, //, %)** : Ces opérateurs ont la même priorité entre eux.
4. **Addition et Soustraction (+, -)** : Ces opérateurs ont une priorité inférieure à celle des opérateurs de multiplication/division.
5. **Opérateurs de comparaison (==, !=, <, >, <=, >=)** : Évaluent l’égalité ou la relation entre deux valeurs.
6. **Opérateurs logiques (and, or, not)** : `not` a la priorité la plus élevée, suivi de `and`, puis `or`.

**NB:** En cas d'égalité de priorité, l'ordre se fera de gauche à droite.

## Les expressions booléennes

{{% notice style=info title=Définition %}}
Une expression booléenne est une formule mathématique qui évalue à vrai (`True`) ou faux (`False`).
Elles sont utilisées en programmation dans les **structures conditionnelles et répétitives**, pour prendre des décisions logiques. Autrement dit, elles servent à exécuter du code en fonction de certaines conditions.
{{% /notice %}} 

### Exemples d'application

#### Exemple #1

Soit l'expression: `(5 + 3) * 2**2/4`

L'ordre d'exécution sera:

|Ordre                   |Détail              |Nouvelle expression                                                                      |
|------------------------|--------------------|-----------------------------------------------------------------------------------------|
|1. Parenthèses          |On calcule l’expression entre parenthèses: `(5+3) = 8`                                  |`(8) * 2**2/4`       |
|2. Exponentiation       |On calcule l’élévation à la puissance : `2**2 = 4`                                      |`(8) * 4/4`          |
|3. Multiplication       |On multiplie le résultat des parenthèses par le résultat de l’exponentiation: `8*4 = 32`|`32/4`               |
|4. Addition             |N/A                                                                                     |Pas de changement    |
|5. Division             |On divise le résultat de la multiplication par 4|Le résultat final de l’expression `(5 + 3) * 2 ** 2 / 4` est `8`|

#### Exemple #2

Supposons que nous ayons deux variables `a` et `b`, avec `a = 10` et `b = 5`. 
Nous voulons vérifier si `a` est plus grand que `b` et si `b` multiplié par 2 est égal à `a`. 
L’expression serait : `(a > b) and (b * 2 == a)` ou si on remplace les valeurs de `a` et `b` l'expression devient:  `(10 > 5) and (5 * 2 == 10)`.

|Ordre                   |Expression calculée              |Résultat                     |
|------------------------|---------------------------------|-----------------------------|
|1. Parenthèses          |`(10 > 5)`et <br> `(5 * 2 == 10)`|`(True)` et <br> `(10 == 10)`|
|2. Opérations logiques  |`(True)` and `(True)`            |Les deux parties de l’expression sont vraies <br>L’expression complète est donc évaluée à `True`.|
 
**Exemple avec l'instruction conditionnelle IF**:

```python
temperature = 25

# La condition/test: Est-ce que la température est plus grande que 20?
if temperature > 20:	 
    print("Il fait chaud")
else:
    print("Il fait froid")
```

Voyons maintenant que sont les structures conditionnelles.
