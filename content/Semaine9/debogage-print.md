+++
title = "Savoir déboguer un programme"
weight = 91
+++


![debogage avec print](../debogage-print.jpeg?width=25vw)

## Comment trouver où sont les erreurs dans notre code ?

### Étape 1: Lire et comprendre les erreurs

- Lorsque vous exécutez une cellule et qu'une erreur se produit, un message d'erreur s'affiche. Lisez attentivement ce message pour comprendre ce qui ne va pas. Les messages d'erreur fournissent souvent des informations précieuses sur la nature de l'erreur et l'endroit où elle s'est produite dans le code.

### Étape 2: Identifier le type d'erreur

- Les erreurs Python courantes incluent les erreurs de syntaxe, les erreurs de type, et les erreurs d'attribut. Par exemple:
   - **SyntaxError**: Il y a une faute de syntaxe dans votre code.
   - **TypeError**: Vous essayez d'utiliser une opération sur un type de données incorrect.
   - **AttributeError**: Vous essayez d'accéder à un attribut qui n'existe pas pour un objet donné.

### Étape 3: Utiliser la fonction `print()` pour déboguer 

- La fonction `print()` est un outil simple mais puissant pour comprendre ce qui se passe dans votre code. Voici comment l'utiliser:
   - **Imprimer des variables**: Ajoutez des instructions `print()` pour afficher les valeurs des variables à différents points de votre code. Cela vous permet de vérifier si les variables contiennent les valeurs attendues.
   - **Tracer l'exécution du code**: Utilisez `print()` pour afficher des messages à différents endroits de votre code afin de suivre l'exécution du programme. Par exemple, vous pouvez imprimer un message au début et à la fin d'une boucle pour voir combien de fois elle s'exécute.
   - **Vérifier les conditions**: Utilisez `print()` pour afficher les résultats des conditions `if` et `else` afin de vérifier si les branches de votre code s'exécutent comme prévu.

## Exemple de débogage avec `print()`

Supposons que vous avez le code suivant qui ne fonctionne pas comme prévu:

```python
def addition(a, b):
    result = a + b
    return result

x = 5
y = "10"
print(addition(x, y))
```

Ce code produira une `TypeError` car vous essayez d'ajouter un entier (`int`) et une chaîne de caractères (`str`). Pour déboguer ce code, vous pouvez ajouter des instructions `print()`:

```python
def addition(a, b):
    print(f"a: {a}, b: {b}")  # Imprimer les valeurs des paramètres
    result = a + b
    print(f"result: {result}")  # Imprimer le résultat avant de le retourner
    return result

x = 5
y = "10"
print(f"x: {x}, y: {y}")  # Imprimer les valeurs avant l'appel de la fonction
print(addition(x, y))
```

En exécutant ce code, vous verrez les valeurs des variables et comprendrez pourquoi l'erreur se produit. Vous pouvez ensuite corriger l'erreur en convertissant `y` en entier:

```python
def addition(a, b):
    print(f"a: {a}, b: {b}")
    result = a + b
    print(f"result: {result}")
    return result

x = 5
y = int("10")  # Convertir y en entier
print(f"x: {x}, y: {y}")
print(addition(x, y))
```