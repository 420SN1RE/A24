+++
title = "Structures conditionnelles imbriquées"
weight = 188
+++

## Les structures conditionnelles imbriquées

Les tests peuvent être imbriquées, c'est-à-dire qu'on peut mettre un `IF` dans une autre.

```python
score = 75
if score > 50:
    if score > 70:
        print("Bien joué !")
    else:
        print("Pas mal, mais peut mieux faire.")
else:
    print("Il faut travailler davantage.")
```

Dans ce cas, comme `score` est 75, le programme affichera "Bien joué !".

**Explication**:

1. **Définition de la variable** : `score` est défini avec une valeur de 75.
2. **Première condition** : Si `score` est supérieur à 50, le programme vérifie une deuxième condition.
3. **Deuxième condition** : Si `score` est supérieur à 70, le programme affiche "Bien joué !".
4. **Sinon** : Si `score` est supérieur à 50 mais pas supérieur à 70, le programme affiche "Pas mal, mais peut mieux faire."
5. **Sinon** : Si `score` n'est pas supérieur à 50, le programme affiche "Il faut travailler davantage."
