+++
title = "Les fonctions"
weight = 81
draft = true
+++

![fonctions](../fonction.jpeg?width=25vw)

Les sous-programmes, aussi appelés `fonctions`, sont des blocs de **code réutilisables** qui permettent de structurer et d'organiser un programme. Ils facilitent la maintenance et la lisibilité du code. 

## Déclaration des fonctions

En Python, une fonction est déclarée avec le mot-clé `def` suivi du nom de la fonction et des parenthèses `()`. Les instructions à exécuter sont ensuite écrites sous cette déclaration, indentées d'une tabulation.

```python
def ma_fonction():
    print("Bonjour tout le monde!")
```

## Utilisation des fonctions (l'appel)

Pour utiliser une fonction, il faut `l'appeler`. Pour ce faire, il suffit d'écrire son nom suivi de parenthèses `()`.

```python
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

```python
def carre(nombre):
    return nombre ** 2

x = carre(5)  # x vaut maintenant 25
```

Il est également possible de retourner plusieurs valeurs en utilisant des tuples.

```python
def operations(a, b):
    somme = a + b
    produit = a * b
    return somme, produit

s, p = operations(3, 4)  # s vaut 7 et p vaut 12
```

## Portée des variables

La portée d'une variable fait référence à l'endroit où une variable est accessible dans le code. En Python, les variables déclarées à l'intérieur d'une fonction sont `locales` à cette fonction, tandis que les variables déclarées en dehors de toute fonction sont `globales`.

```python
x = 10  # Variable globale

def ma_fonction():
    y = 5  # Variable locale
    print(y)  # Affiche 5

ma_fonction()
print(x)  # Affiche 10
print(y)  # Erreur! y n'est pas défini à ce niveau
```

### Variables globales et locales

Il est possible de modifier une variable globale à l'intérieur d'une fonction en utilisant le mot-clé `global`.

```python
x = 10

def modifier_global():
    global x
    x = 20

modifier_global()
print(x)  # Affiche 20
```

### Variables enfermées (Bases de connaissances)

Les variables enfermées sont des variables définies dans une fonction englobante et accessibles dans une fonction imbriquée.

```python
def exterieur():
    x = 10

    def interieur():
        print(x)  # Accède à la variable x de la fonction englobante

    interieur()

exterieur()  # Affiche 10
```

## Fonctions Lambda (Bases de connaissances)

Les fonctions lambda sont des fonctions anonymes définies à l'aide du mot-clé `lambda`. Elles sont souvent utilisées pour des opérations simples et rapides.

```python
carre = lambda x: x ** 2
print(carre(5))  # Affiche 25
```

## Fonctions de première classe (Bases de connaissances)

En Python, les fonctions sont des objets de première classe, ce qui signifie qu'elles peuvent être passées en argument à d'autres fonctions, retournées par d'autres fonctions, et assignées à des variables.

```python
def appliquer_fonction(f, valeur):
    return f(valeur)

def carre(x):
    return x ** 2

resultat = appliquer_fonction(carre, 5)  # resultat vaut 25
```

## Fermetures (Bases de connaissances)

Une fermeture est une fonction qui capture les variables de son environnement englobant. Cela permet de créer des fonctions avec un état interne.

```python
def creer_incrementateur(n):
    def incrementer(x):
        return x + n
    return incrementer

incrementer_de_5 = creer_incrementateur(5)
print(incrementer_de_5(10))  # Affiche 15
```

## Décorateurs (Bases de connaissances)

Les décorateurs sont des fonctions qui modifient le comportement d'autres fonctions. Ils sont souvent utilisés pour ajouter des fonctionnalités à des fonctions existantes.

```python
def decorateur(fonction):
    def nouvelle_fonction(*args, **kwargs):
        print("Avant l'appel de la fonction")
        resultat = fonction(*args, **kwargs)
        print("Après l'appel de la fonction")
        return resultat
    return nouvelle_fonction

@decorateur
def dire_bonjour():
    print("Bonjour!")

dire_bonjour()
```