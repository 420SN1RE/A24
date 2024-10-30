+++
title = "Les variables, interaction et types de données"
weight = 1
+++

## Les variables

En Python, une variable est un conteneur qui permet de stocker des données. Pour créer une variable, il suffit de lui attribuer une valeur en utilisant le signe `=`. Par exemple :

```python
nom = "Aline"
age = 30
```

Dans cet exemple, `nom` est une variable qui contient la chaîne de caractères `"Alice"`, et `age` est une variable qui contient le nombre entier `30`.

## Interaction avec l'utilisateur

### Affichage

La fonction `print()` est utilisée pour afficher des informations à l'écran. Elle est essentielle pour le débogage et l'interaction avec l'utilisateur. 

### La syntaxe de la fonction print()

La syntaxe de base de `print()` est la suivante :

```python
print(valeur1, valeur2, valeur3,...)
```

- `valeur1, valeur2, ...` : Les valeurs à afficher.
- `end` : Ce qui est ajouté à la fin (par défaut, un saut de ligne).


### Les f-strings

Les `f-strings` (formatted string literals) sont une manière concise et lisible de formater des chaînes de caractères. Une f-string est définie en plaçant un `f` avant les guillemets et en utilisant des accolades `{}` pour inclure des expressions Python à évaluer. Voici un exemple :

```python
nom = "Alice"
age = 30
print(f"Bonjour, {nom}. Vous avez {age} ans.")
```

Dans cet exemple, les variables `nom` et `age` sont insérées directement dans la chaîne de caractères.

Les f-strings permettent également d'inclure des expressions plus complexes :

```python
largeur = 5
hauteur = 10
print(f"La surface du rectangle est {largeur * hauteur}.")
```

### L'attribut `end`

Par défaut, `print()` ajoute un saut de ligne (`\n`) à la fin de chaque appel. Vous pouvez modifier ce comportement en utilisant l'attribut `end`. Voici un exemple :

```python
for i in range(5):
    print(i, end=" ")
```

Dans cet exemple, les nombres de 0 à 4 sont imprimés sur la même ligne, séparés par un espace.

Vous pouvez également utiliser d'autres caractères ou chaînes pour `end` :

```python
print("Bonjour", end=", ")
print("monde!")
```

Dans cet exemple, la sortie sera `Bonjour, monde!`.

### Combinaison de f-strings et `end`

Vous pouvez combiner les f-strings et l'attribut `end` pour un formatage encore plus flexible :

```python
for i in range(1, 6):
    print(f"Nombre {i}", end="; ")
```

Dans cet exemple, chaque nombre est imprimé avec un point-virgule à la fin.

### Saisie au clavier

Python permet d'interagir facilement avec l'utilisateur via la fonction `input()`. Cette fonction affiche un message à l'écran et attend que l'utilisateur saisisse une valeur. Par exemple :

```python
nom = input("Quel est votre nom ? ")
print("Bonjour, " + nom + "!")
```

Ici, `input()` demande à l'utilisateur de saisir son nom, puis `print()` affiche un message de bienvenue.


## Types de données

Python prend en charge plusieurs types de données, dont les plus courants sont :

- **Les chaînes de caractères (str)** : Utilisées pour représenter du texte. Elles sont entourées de guillemets simples ou doubles.
```python
texte = "Bonjour, monde!"
```

- **Les nombres entiers (int)** : Utilisés pour représenter des nombres entiers.
```python
nombre = 42
```

- **Les nombres à virgule flottante (float)** : Utilisés pour représenter des nombres décimaux.
```python
pi = 3.14
```

- **Les booléens (bool)** : Utilisés pour représenter des valeurs de vérité, soit `True` soit `False`.
```python
est_vrai = True
```

- **Les listes (list)** : Utilisées pour stocker des collections ordonnées de valeurs.
```python
fruits = ["pomme", "banane", "cerise"]
```

## Transtypage ou conversion de type

La conversion de type consiste à modifier le type d'une donnée à un autre type. La conversion se fait en utilisant des fonctions de conversion.

- `int()`: Convertit une valeur en entier.
```python
nombre = int("42")  # nombre sera 42
```

- `float()`: Convertit une valeur en flottant.
```python
nombre = float("3.14")  # nombre sera 3.14
```

- `str()`: Convertit une valeur en chaîne de caractères.
```python
texte = str(42)  # texte sera "42"
```

- `list()`: Convertit une valeur en liste.
```python
liste = list("abc")  # liste sera ['a', 'b', 'c']
```

### Conversion de la sortie de input()

La fonction `input()` est utilisée pour obtenir des données de l'utilisateur. Cependant, il est important de noter que `input()` **retourne toujours une chaîne de caractères (str)**, quel que soit le type de données saisi par l'utilisateur. Par conséquent, il est souvent nécessaire de convertir cette chaîne en un autre type de données pour pouvoir l'utiliser correctement dans votre programme.

Supposons que vous demandiez à l'utilisateur de saisir un nombre. Pour pouvoir **effectuer des opérations arithmétiques avec ce nombre**, vous devez convertir la chaîne de caractères retournée par `input()` en un entier ou un flottant :

```python
age_str = input("Quel est votre âge ? ")
age = int(age_str)  # Conversion de la chaîne en entier
print("Vous aurez " + str(age + 1) + " ans l'année prochaine.")
```

Dans cet exemple, `age_str` est une chaîne de caractères. La fonction `int()` est utilisée pour convertir cette chaîne en un entier, ce qui permet ensuite d'effectuer une addition.

### Pourquoi la conversion est nécessaire

1. **Opérations arithmétiques** : Pour effectuer des calculs, les données doivent être dans un format numérique (int ou float).
```python
nombre_str = input("Entrez un nombre : ")
nombre = float(nombre_str)
print("Le double de votre nombre est " + str(nombre * 2))
```

2. **Comparaisons** : Pour comparer des valeurs numériques, il est nécessaire de convertir les chaînes en nombres.
```python
age_str = input("Quel est votre âge ? ")
age = int(age_str)
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```