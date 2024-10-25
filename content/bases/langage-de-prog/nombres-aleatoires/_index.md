+++
title = "Les nombres aléatoires"
weight = 7
+++

![Aleatoire](./nb_aleatoire.jpeg?width=18vw)


La génération de nombres aléatoires est une tâche courante en programmation, utilisée dans des domaines variés comme les jeux, les simulations, et les tests. Python offre plusieurs façons de générer des nombres aléatoires, principalement via le module `random`.

## Introduction au module `random`

Le module `random` de Python fournit des fonctions pour générer des nombres pseudo-aléatoires. Pour l'utiliser, vous devez d'abord l'importer :

```python
import random
```

## Générer des nombres aléatoires

### Nombres aléatoires entiers

Pour générer un nombre entier aléatoire entre deux bornes inclusives, utilisez la fonction `randint` :

```python
import random

# Génère un nombre entier aléatoire entre 1 et 10
nombre_aleatoire = random.randint(1, 10)
print(nombre_aleatoire)
```

### Nombres aléatoires à virgule flottante

Pour générer un nombre à virgule flottante entre 0 et 1, utilisez la fonction `random` :

```python
import random

# Génère un nombre flottant aléatoire entre 0 et 1
nombre_flottant = random.random()
print(nombre_flottant)
```

Pour générer un nombre flottant dans une plage spécifique, utilisez `uniform` :

```python
import random

# Génère un nombre flottant aléatoire entre 1.5 et 5.5
nombre_flottant = random.uniform(1.5, 5.5)
print(nombre_flottant)
```

## Choisir des éléments aléatoires

### Choisir un élément aléatoire dans une liste

La fonction `choice` permet de sélectionner un élément aléatoire dans une séquence (comme une liste) :

```python
import random

# Liste d'exemple
liste = ['pomme', 'banane', 'cerise', 'datte']

# Choisit un élément aléatoire dans la liste
fruit_aleatoire = random.choice(liste)
print(fruit_aleatoire)
```

### Mélanger une liste

Pour mélanger les éléments d'une liste de manière aléatoire, utilisez `shuffle` :

```python
import random

# Liste d'exemple
liste = [1, 2, 3, 4, 5]

# Mélange la liste
random.shuffle(liste)
print(liste)
```

## Générer des échantillons aléatoires

Pour sélectionner plusieurs éléments aléatoires sans répétition, utilisez `sample` :

```python
import random

# Liste d'exemple
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sélectionne 3 éléments aléatoires de la liste
echantillon = random.sample(liste, 3)
print(echantillon)
```
