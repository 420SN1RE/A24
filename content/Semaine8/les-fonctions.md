+++
title = "Les fonctions"
weight = 81
+++

![fonctions](../fonction.jpeg?width=25vw)

Les sous-programmes, aussi appelés `fonctions`, sont des blocs de **code réutilisables** qui permettent de structurer et d'organiser un programme. Ils facilitent la maintenance et la lisibilité du code. 

Vous en connaissez déjà quelques-unes:
- print()
- int(), float(), str(), bool()
- input()
- range()

## Déclaration des fonctions

En Python, une fonction est déclarée avec le mot-clé `def` suivi du nom de la fonction et des parenthèses `()`. Les instructions à exécuter sont ensuite écrites sous cette déclaration, indentées d'une tabulation.

```python
def ma_fonction():
    # Bloc de code de la fonction
```

{{% notice style=note title=Noe %}}
Notez le `:` après les parenthèses et l'**indentation** du bloc de code.
{{% /notice %}}

## Utilisation des fonctions (l'appel d'une fonction)

Pour utiliser une fonction, il faut `l'appeler`. Pour ce faire, il suffit d'écrire son nom suivi de parenthèses `()`.

```python
def ma_fonction():
    print("Bonjour tout le monde!")

ma_fonction()  # Affiche "Bonjour tout le monde!"
```

## Passage de paramètres

Les fonctions peuvent prendre des paramètres, qui sont des valeurs passées à la fonction lors de son appel. Les paramètres sont déclarés entre les parenthèses lors de la déclaration de la fonction.

```python
def saluer(nom):
    print(f"Bonjour {nom}!")

saluer("Nathalie")  # Affiche "Bonjour Nathalie!"
```

### Paramètres par défaut

Il est possible de définir des valeurs par défaut pour les paramètres. Si un argument n'est pas fourni lors de l'appel de la fonction, la valeur par défaut sera utilisée.

```python
def saluer(nom="tout le monde"):
    print(f"Bonjour {nom}!")

saluer()  # Affiche "Bonjour tout le monde!"
saluer("Albert")  # Affiche "Bonjour Albert!"
```

### Paramètres nommés

Les paramètres peuvent être passés par nom, ce qui permet de les fournir dans un ordre différent de celui de la déclaration.

```python
def saluer(nom, message):
    print(f"{message}, {nom}!")

saluer(message="Salut", nom="Aline")  # Affiche "Salut, Aline!"
```

### Paramètres variables

Python permet de passer un nombre variable d'arguments à une fonction en utilisant `*args` pour les arguments positionnels et `**kwargs` pour les arguments nommés.

```python
def afficher_noms(*noms):
    for nom in noms:
        print(nom)

afficher_noms("Alice", "Bob", "Charlie")  # Affiche chaque nom sur une nouvelle ligne

def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=30, ville="Paris")  # Affiche chaque information sur une nouvelle ligne
```

## Retour de valeurs

Une fonction peut renvoyer une valeur à l'aide de l'instruction `return`. Cette valeur peut ensuite être utilisée dans le reste du programme.

![retour de valeur](../fonctions.jpg?width=25vw).

```python
def carre(nombre):
    return nombre ** 2

x = carre(5)  # x vaut maintenant 25
```

## La documentation des fonctions (_Docstrings_)

Les docstrings sont des chaînes de caractères utilisées pour documenter les fonctions. Elles sont placées juste après la définition de la fonction.

**Exemple en Python :**

```python
def addition(a, b):
    """
    Calcule la somme de deux nombres.

    Paramètres:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Retourne:
    int, float: La somme des deux nombres.
    """
    return a + b
```

## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)