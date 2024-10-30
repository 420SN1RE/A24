+++
title = "if elif et else (expressions booléennes et structures conditionnelles)"
weight = 2
+++


## Expressions booléennes

Les expressions booléennes sont souvent utilisées dans les structures conditionnelles pour contrôler le flux d'exécution du programme. En comprenant comment utiliser les opérateurs de comparaison et logiques, vous pouvez écrire des conditions complexes et contrôler le comportement de vos programmes de manière efficace.:

Les expressions booléennes sont des **expressions qui valent à `True` ou `False`**. Elles sont essentielles pour les structures conditionnelles et les boucles. 

## Opérateurs de comparaison

Les opérateurs de comparaison sont utilisés pour comparer des valeurs et renvoient un résultat booléen (`True` ou `False`).

- `==` : Égal à
```python
5 == 5  # True
5 == 3  # False
```

- `!=` : Différent de
```python
5 != 3  # True
5 != 5  # False
```

- `>` : Supérieur à
```python
5 > 3  # True
3 > 5  # False
```

- `<` : Inférieur à
```python
3 < 5  # True
5 < 3  # False
```

- `>=` : Supérieur ou égal à
```python
5 >= 5  # True
5 >= 3  # True
```

- `<=` : Inférieur ou égal à
```python
3 <= 5  # True
5 <= 5  # True
```

## Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs expressions booléennes. 

- `and` : Renvoie `True` si les deux expressions sont vraies
```python
(5 > 3) and (3 < 5)  # True
(5 > 3) and (3 > 5)  # False
```

- `or` : Renvoie `True` si au moins une des expressions est vraie
```python
(5 > 3) or (3 > 5)  # True
(5 < 3) or (3 > 5)  # False
```

- `not` : Inverse la valeur de l'expression
```python
not (5 > 3)  # False
not (3 > 5)  # True
```

## Structures conditionnelles

Les structures conditionnelles permettent à un programme de prendre des décisions en fonction de certaines conditions. Les mots-clés `if`, `elif` et `else` sont utilisés pour créer ces structures conditionnelles.

### La structure `if`

La structure `if` permet d'exécuter un bloc de code **uniquement si une condition donnée est vraie**. 
```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
```

Dans cet exemple, le message "Vous êtes majeur." sera affiché uniquement si la variable `age` est supérieure ou égale à 18.

### La structure `elif`

Le mot-clé `elif`, contraction de "else if", **permet de vérifier plusieurs conditions de manière séquentielle**. Si la première condition `if` est fausse, Python vérifie la condition `elif`.

```python
note = 75

if note >= 90:
    print("Excellent")
elif note >= 75:
    print("Très bien")
elif note >= 60:
    print("Bien")
else:
    print("Peut mieux faire")
```

Dans cet exemple, si la note est supérieure ou égale à 90, le message "Excellent" sera affiché. Si la note est inférieure à 90 mais supérieure ou égale à 75, le message "Très bien" sera affiché, et ainsi de suite.

### La structure `else`

Le mot-clé `else` permet de définir un bloc de code qui sera exécuté **si toutes les conditions précédentes sont fausses**. 

```python
temperature = 15

if temperature > 30:
    print("Il fait très chaud")
elif temperature > 20:
    print("Il fait chaud")
else:
    print("Il fait frais")
```

Dans cet exemple, si la température est supérieure à 30, le message "Il fait très chaud" sera affiché. Si la température est supérieure à 20 mais inférieure ou égale à 30, le message "Il fait chaud" sera affiché. Si aucune de ces conditions n'est remplie, le message "Il fait frais" sera affiché.

## Combinaison de conditions

Il est possible de combiner plusieurs conditions en utilisant les opérateurs logiques `and`, `or` et `not`. 

```python
age = 20
citoyen = True

if age >= 18 and citoyen:
    print("Vous pouvez voter.")
else:
    print("Vous ne pouvez pas voter.")
```

Dans cet exemple, le message "Vous pouvez voter." sera affiché uniquement si l'âge est supérieur ou égal à 18 et si la personne est citoyenne.

