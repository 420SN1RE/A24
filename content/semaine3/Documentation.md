+++
title =  "Documentation du code"
weight =  32
+++

![Documentation](../documentation.jpg?width=25vw).

## Pourquoi documenter le code ?

La documentation du code est essentielle pour rendre votre code compréhensible et maintenable par d'autres développeurs, ainsi que par vous-même à l'avenir. 

Il existe différentes raisons de vouloir documenter le code: 
- Pour expliquer une instruction (commentaire)
- Pour décrire un module ou sous-programme (docstring)
- Pour incorporer du texte avec du code (programme lettré)

{{% notice info %}}
Pour l'instant, on se contentera de documenter le code à l'aide de commentaires. Plus tard dans la session, on utilisera des `docstrings` et la programmation lettrée.
{{% /notice %}}

## Les commentaires

Les commentaires sont des notes que vous ajoutez directement dans le code pour expliquer ce que fait une section spécifique. Python ignore les commentaires, c’est-à-dire qu’il ne les exécute pas.

- Les commentaires commencent par le symbole `#` (dièse).
- Les commentaires sont utilisés pour :

	1. Expliquer le code
	1. Rendre le code plus lisible
	1. Empêcher l’exécution lors de tests du code

**Exemple en Python :**

```python
# Cette fonction calcule la somme de deux nombres
def addition(a, b):
    return a + b
```

## Atelier

[Lecture et affichage de données](../atelier-input_print.ipynb)

## Pause : 5 minutes

![Pause](../pause.jpg?width=25vw)
