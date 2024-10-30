+++
title = "Les fonctions"
weight = 7
+++

Les fonctions sont des blocs de code réutilisables qui effectuent une tâche spécifique. Elles permettent de structurer le code de manière modulaire, facilitant ainsi la lecture, la maintenance et la réutilisation.

## Définition d'une fonction

En Python, une fonction est définie à l'aide du mot-clé `def`, suivi du nom de la fonction, de parenthèses et d'un deux-points. Le corps de la fonction est indenté.

```python
def saluer():
    print("Bonjour, monde!")
```

Dans cet exemple, `saluer` est une fonction qui affiche "Bonjour, monde!" lorsqu'elle est appelée.

## Appel d'une fonction

Pour appeler une fonction, il suffit d'utiliser son nom suivi de parenthèses :

```python
saluer()  # Affiche "Bonjour, monde!"
```

## Paramètres et arguments

Les fonctions peuvent accepter des **paramètres**, qui sont des variables locales à la fonction. Les **arguments** sont les valeurs passées à ces paramètres lors de l'appel de la fonction. 

```python
def saluer_personne(nom):
    print(f"Bonjour, {nom}!")

saluer_personne("Aline")  # Affiche "Bonjour, Alice!"
```

Dans cet exemple, `nom` est un paramètre, et "Aline" est un argument passé à la fonction `saluer_personne`.

## Valeurs de retour

Les fonctions peuvent retourner des valeurs à l'aide du mot-clé `return`. 

```python
def additionner(a, b):
    return a + b

resultat = additionner(3, 5)
print(resultat)  # Affiche 8
```

Dans cet exemple, la fonction `additionner` retourne la somme de `a` et `b`.

## Paramètres par défaut

Les fonctions peuvent avoir des paramètres par défaut, qui sont utilisés si aucun argument n'est fourni pour ces paramètres :

```python
def saluer_personne(nom="monde"):
    print(f"Bonjour, {nom}!")

saluer_personne()  # Affiche "Bonjour, monde!"
saluer_personne("Alice")  # Affiche "Bonjour, Alice!"
```

### Arguments nommés

Les arguments peuvent être passés par nom, ce qui permet de les fournir dans un ordre différent :

```python
def afficher_info(nom, age):
    print(f"Nom : {nom}, Âge : {age}")

afficher_info(age=30, nom="Alice")  # Affiche "Nom : Alice, Âge : 30"
```

## Portée des variables

### Variables locales

Les variables définies à l'intérieur d'une fonction sont locales à cette fonction et ne sont pas accessibles en dehors.

```python
def ma_fonction():
    variable_locale = "Je suis locale"
    print(variable_locale)

ma_fonction()  # Affiche "Je suis locale"
# print(variable_locale)  # Provoque une erreur car variable_locale n'est pas définie en dehors de la fonction
```

### Variables globales

Les variables globales sont définies en dehors de toutes les fonctions et sont accessibles depuis n’importe quelle fonction du programme. 
Pour **modifier une variable globale à l’intérieur d’une fonction**, vous devez utiliser le mot-clé `global`.

```python
compteur = 0	# variable globale

def incrementer_compteur():
    global compteur  # Indique que nous voulons utiliser/modifier la variable globale
    compteur += 1
    print(f"Compteur à l'intérieur de la fonction : {compteur}")

# Appel de la fonction
incrementer_compteur()  # Affiche "Compteur à l'intérieur de la fonction : 1"

# Affichage de la variable globale
print(f"Compteur à l'extérieur de la fonction : {compteur}")  # Affiche "Compteur à l'extérieur de la fonction : 1"
```
