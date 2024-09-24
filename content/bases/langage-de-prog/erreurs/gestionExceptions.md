+++
title = "Gestion des exceptions"
weight = 99
+++

## La gestion des exceptions

Python permet de gérer les exceptions à l'aide des blocs `try-except`. Cela permet d'attraper les erreurs et de les traiter de manière appropriée sans interrompre l'exécution du programme.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro")
```

Il est également possible de gérer plusieurs types d'exceptions dans un même bloc `try-except`.

```python
try:
    ma_liste = [1, 2, 3]
    print(ma_liste[5])
except IndexError:
    print("Erreur : index de liste incorrect")
except ZeroDivisionError:
    print("Erreur : division par zéro")
```
