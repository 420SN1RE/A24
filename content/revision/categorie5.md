+++
title = "Les listes"
weight = 5
+++

Les listes sont l'un des types de données les plus utilisés en Python. Elles permettent de stocker des collections ordonnées d'éléments, qui peuvent être de n'importe quel type. Les listes sont mutables, ce qui signifie que leurs éléments peuvent être modifiés après leur création.

## Création de listes

Vous pouvez créer une liste en plaçant une série d'éléments entre crochets `[]`, séparés par des virgules. 

```python
# Liste de nombres
nombres = [1, 2, 3, 4, 5]

# Liste de chaînes de caractères
fruits = ["pomme", "banane", "cerise"]

# Liste mixte
mixte = [1, "pomme", 3.14, True]
```

## Accès aux éléments

Les éléments d'une liste peuvent être accédés en utilisant des indices, qui commencent à 0. Voici comment accéder aux éléments d'une liste :

```python
fruits = ["pomme", "banane", "cerise"]
print(fruits[0])  # Affiche "pomme"
print(fruits[1])  # Affiche "banane"
print(fruits[2])  # Affiche "cerise"
```

Vous pouvez également utiliser des indices négatifs pour accéder aux éléments à partir de la fin de la liste :

```python
print(fruits[-1])  # Affiche "cerise"
print(fruits[-2])  # Affiche "banane"
print(fruits[-3])  # Affiche "pomme"
```

## Modification des éléments

Les listes étant mutables, vous pouvez modifier leurs éléments en utilisant des indices :

```python
fruits = ["pomme", "banane", "cerise"]
fruits[1] = "orange"
print(fruits)  # Affiche ["pomme", "orange", "cerise"]
```

## Ajout et suppression d'éléments

Python offre plusieurs méthodes pour ajouter et supprimer des éléments dans une liste :

- `append()`: Ajoute un élément à la fin de la liste.
```python
fruits.append("mangue")
print(fruits)  # Affiche ["pomme", "orange", "cerise", "mangue"]
```

- `insert()`: Insère un élément à une position spécifique.
```python
fruits.insert(1, "banane")
print(fruits)  # Affiche ["pomme", "banane", "orange", "cerise", "mangue"]
```

- `remove()`: Supprime la première occurrence d'un élément.
```python
fruits.remove("orange")
print(fruits)  # Affiche ["pomme", "banane", "cerise", "mangue"]
  ```

- `pop()`: Supprime et retourne l'élément à une position spécifique (par défaut, le dernier élément).
```python
dernier_fruit = fruits.pop()
print(dernier_fruit)  # Affiche "mangue"
print(fruits)  # Affiche ["pomme", "banane", "cerise"]
```

## Parcourir une liste

Vous pouvez parcourir les éléments d'une liste en utilisant une boucle `for` :

```python
for fruit in fruits:
    print(fruit)
```

## Fonctions utiles

Python fournit plusieurs fonctions intégrées pour travailler avec les listes :

- `len()`: Retourne la longueur de la liste.
```python
print(len(fruits))  # Affiche 3
```

- `sorted()`: Retourne une nouvelle liste triée.
```python
fruits_triees = sorted(fruits)
print(fruits_triees)  # Affiche ["banane", "cerise", "pomme"]
```

- `sum()`: Retourne la somme des éléments d'une liste de nombres.
```python
nombres = [1, 2, 3, 4, 5]
print(sum(nombres))  # Affiche 15
```

- `index(x)`: Retourne l'indice de la première occurrence de l'élément `x`.
```python
fruits = ["pomme", "banane", "cerise"]
index = fruits.index("banane")
print(index)  # Affiche 1
```

- `sort()`: Trie la liste en place. 
```python
fruits = ["cerise", "pomme", "banane"]
fruits.sort()
print(fruits)  # Affiche ["banane", "cerise", "pomme"]`
```

- `reverse()`: Inverse l'ordre des éléments de la liste.
```python
fruits = ["pomme", "banane", "cerise"]
fruits.reverse()
print(fruits)  # Affiche ["cerise", "banane", "pomme"]
```

- `min()`: retourne l'élément avec la valeur minimale d'une liste.
```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5]
valeur_minimale = min(nombres)
print(valeur_minimale)  # Affiche 1
```

- `max()`: retourne l'élément avec la valeur maximale d'une liste.
```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5]
valeur_maximale = max(nombres)
print(valeur_maximale)  # Affiche 9
```

- `set()`: convertit une liste en un ensemble, supprimant ainsi les doublons et ne conservant que les éléments uniques.
```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5]
ensemble_unique = set(nombres)
print(ensemble_unique)  # Affiche {1, 2, 3, 4, 5, 6, 9}
```

## Slicing (découpage) des listes 

Le slicing (ou découpage) permet d'extraire une partie d'une liste (ou d'autres séquences comme les chaînes de caractères). Le slicing utilise la syntaxe des indices pour spécifier les éléments à inclure dans la nouvelle sous-liste.

La syntaxe de base pour le découpage est la suivante :

```python
liste[debut:fin:saut]
```

- `debut` : L'indice de début (inclusif). Si omis, le découpage commence au début de la liste.
- `fin` : L'indice de fin (exclusif). Si omis, le découpage s'arrête à la fin de la liste.
- `saut` : L'incrément entre chaque élément. Si omis, la valeur par défaut est 1.

### Découpage de base

Voici quelques exemples de découpage de base :

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraire les éléments de l'indice 2 à l'indice 5 (exclusif)
sous_liste = nombres[2:5]
print(sous_liste)  # [2, 3, 4]

# Extraire les éléments du début jusqu'à l'indice 4 (exclusif)
sous_liste = nombres[:4]
print(sous_liste)  # [0, 1, 2, 3]

# Extraire les éléments de l'indice 5 jusqu'à la fin
sous_liste = nombres[5:]
print(sous_liste)  # [5, 6, 7, 8, 9]

# Extraire tous les éléments
sous_liste = nombres[:]
print(sous_liste)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Découpage avec un saut

Vous pouvez également spécifier un saut pour le découpage :

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraire tous les éléments avec un saut de 2
sous_liste = nombres[::2]
print(sous_liste)  # [0, 2, 4, 6, 8]

# Extraire les éléments de l'indice 1 à l'indice 7 avec un saut de 2
sous_liste = nombres[1:8:2]
print(sous_liste)  # [1, 3, 5, 7]
```

### Découpage avec des indices négatifs

Les indices négatifs peuvent être utilisés pour compter à partir de la fin de la liste :

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraire les trois derniers éléments
sous_liste = nombres[-3:]
print(sous_liste)  # [7, 8, 9]

# Extraire les éléments de l'indice -7 à l'indice -2
sous_liste = nombres[-7:-2]
print(sous_liste)  # [3, 4, 5, 6, 7]
```

### Découpage inversé

Vous pouvez inverser une liste en utilisant un pas négatif :

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inverser la liste
sous_liste = nombres[::-1]
print(sous_liste)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
