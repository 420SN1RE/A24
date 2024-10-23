+++
title = "Les sous-programmes"
weight = 81
+++

![fonctions](../fonctions.jpg?width=25vw).


## Déclaration des sous-programmes

En programmation, un **sous-programme** est généralement appelé une **fonction**. Une fonction est déclarée avec le mot-clé `def` suivi du nom de la fonction et des parenthèses `()`. Les instructions à exécuter sont ensuite écrites sous cette déclaration, **indentées d'une tabulation**.

```python
# Déclaration d'une fonction nommée ma_fonction
def ma_fonction():
    print("Bonjour le monde!")
```

## Appel des sous-programmes

Lorsqu'on veut utiliser une fonction, on dit qu'on **appelle** la fonction. Pour appeler une fonction, il suffit d'écrire son nom suivi de parenthèses `()`.

```python
# Appel (utilisation) de la fontion ma_fonction
ma_fonction()  # Affiche "Bonjour le monde!"
```

## Passage de paramètres

Les fonctions peuvent prendre des **paramètres**, qui sont des valeurs passées à la fonction lors de son appel. Les paramètres sont précisés **entre les parenthèses** d'une fonction, **lors de la déclaration de la fonction**.

```python
# Déclaration de la fonction saluer
def saluer(nom):
    print(f"Bonjour {nom}!")

# Utilisation de la fonction saluer avec comme paramètre Nathalie
saluer("Nathalie")  # Affiche "Bonjour Nathalie!"
```
## Les paramètres par défaut

Les paramètres par défaut dans les fonctions en Python permettent de donner une valeur par défaut à un ou plusieurs paramètres. Cela signifie que si un argument n'est pas fourni lors de l'appel de la fonction, le paramètre prendra la valeur par défaut spécifiée.
Les paramètres par défaut sont très utiles pour rendre les fonctions plus flexibles et faciles à utiliser, car ils permettent de ne pas spécifier certains arguments si les valeurs par défaut conviennent.

Voici un exemple simple pour illustrer cela :

```python
def salutation(nom, message="Bonjour"):
    print(f"{message}, {nom}!")

# Appel de la fonction avec les deux arguments
salutation("Nathalie", "Salut")

# Appel de la fonction avec seulement le premier argument
salutation("Nathalie")
```
**Explication**

- Dans cet exemple, la fonction `salutation` prend deux paramètres : `nom` et `message`. 
- Le paramètre `message` a une valeur par défaut de `"Bonjour"`. 
- Lorsque la fonction est appelée avec les deux arguments, elle affiche "Salut, Nathalie!". 
- Lorsque la fonction est appelée avec seulement le premier argument, elle utilise la valeur par défaut pour `message` et affiche "Bonjour, Nathalie!".

## Retour des sous-programmes

Une fonction peut **renvoyer une valeur** pour que cette valeur soit **utilisée dans le reste du programme. Pour faire en sorte qu'une fonction renvoie une valeur, on utilise le mot clé `return`. L'instruction avec le mot clé `return` **DOIT** être la dernière de la fonction. En d'autres mots, il ne peut pas avoir d'autres lignes de code dans une fonction, **APRÈS** l'instruction `return`

```python
# Déclaration de la fonction carre
def carre(nombre):
    return nombre ** 2

# Utilisation de la fonction pour calculer le carré de 5 et stocker le résultat dans la variable x
x = carre(5)  # x vaut maintenant 25
```

## Atelier

[Les fonctions](../atelier-Fonctions.ipynb) 