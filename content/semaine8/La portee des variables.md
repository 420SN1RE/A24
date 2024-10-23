+++
title =  "La portée des variables"
weight = 83
+++


![La portée des variables](../portees.jpg?width=25vw).


## La portée des variables

La portée d'une variable fait référence à l'endroit où une variable est accessible dans le code. En Python, les variables déclarées à l'intérieur d'une fonction sont `locales` à cette fonction, tandis que les variables déclarées en dehors de toute fonction sont `globales`.

- Une **variable locale** pourra être utilisée **SEULEMENT** à l'intérieur de la fonction dans laquelle elle a été déclarée.
- Une **variable globale** pourra être utilisée dans tout le programme.

Exemple : On crée utilise une variable globale à l'intérieur de la fonction, **sans la redéfinir**.

```python
c = 1 # variable globale 

def addition():
    # incrémente c de 2
    c = c + 2  # Ici c n'est pas accessible
    print(c)

print(c)  # Ici c vaut 1
addition()   # Affiche UnboundLocalError: local variable 'c' referenced before assignment
```

**Explication**: On peut accéder à la variable globale `c`, qu'à l'extérieur de la fonction, mais non ne peut pas la modifier à l'intérieur de la fonction.

## Rendre globale, une variable locale

Il est possible de modifier une variable locale en une variable globale à l'intérieur d'une fonction en utilisant le mot-clé `global`.

```python
c = 1 # variable globale 

def addition():
    global c    # Ici c est le même  et vaut 1
    # incrémente c de 2
    c = c + 2  
    print(c)  Ici c = 1 + 2

print(c)  # Ici c vaut toujour 1
addition() # Affiche 3
```

```plaintext
1
3
````

