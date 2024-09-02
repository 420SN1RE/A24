+++
title =  "La portée des variables"
weight = 82
+++

![La portée des variables](../portees.jpg?width=25vw).

## Portée des variables

La **portée d'une variable** fait référence à **l'endroit où une variable est accessible/utilisable** dans le code. 
En Python, les variables déclarées à l'intérieur d'une fonction sont **locales** à cette fonction, tandis que les variables déclarées en dehors de toute fonction sont **globales**.
- Une **variable locale** pourra être utilisée **SEULEMENT** à l'intérieur de la fonction dans laquelle elle a été déclarée.
- Une **variable globale** pourra être utilisée dans tout le programme.

```python
x = 10  # Variable globale

def ma_fonction():
    y = 5  # Variable locale
    print(y)  # Affiche 5

ma_fonction()
print(x)  # Affiche 10
print(y)  # Erreur! y n'est pas défini à ce niveau
```

Dans cet exemple, **`y` est une variable locale à `ma_fonction`**, donc elle n'est pas accessible en dehors de cette fonction. 
À l'inverse, **`x` est une variable globale**, donc elle est accessible partout dans le code. 

## Atelier

[La portée des variables](../atelier-PorteeVariables.ipynb)