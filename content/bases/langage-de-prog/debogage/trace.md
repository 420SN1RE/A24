+++
title = "La trace d'exécution"
weight = 2
+++

![Trace d'exécution](../trace.webp?width=20vw)

## Qu'est-ce que la trace d'exécution ?

La trace d’exécution est un outil, sous forme d'un tableau, qui permet de vérifier le bon fonctionnement d'un algorithme. Elle montre l'évolution des valeurs de chacune des variables tout au long du déroulement de l’algorithme (exécution pas-à-pas).

## Construction du tableau de la trace

- Les colonnes du tableau correspondent aux variables déclarées dans l'algorithme. Le titre des colonnes est le nom des variables.
- Le titre des lignes est le numéro des lignes de l'algorithme.
- Dans une cellule, on inscrira la valeur de la variable correspondante seulement si elle a changé après l’exécution de l'instruction.
- On peut ajouter une colonne «Console» pour simuler l'affichage à la console.
- Vidéo explicative: [Vidéo explicative sur la trace d'exécution](https://www.youtube.com/watch?v=ZLNhqxUlM68)

## Exemple

Prenons l'exemple de cet algorithme simple en supposant que l'utilisateur saisira 5 et 10:

```python {linenos=true}
# Exemple d'un programme simple qui effectue la somme de 2 nombres
# Données en entrée
print("Veuillez saisir deux nombres pour en faire la somme : ")
nombre1 = int(input("Nombre 1 : "))
nombre2 = int(input("Nombre 2 : "))

# Traitement
somme = nombre1 + nombre2

# Affichage
print("La somme des deux nombres saisis est égale à : ", somme)
```

| # | nombre1 | nombre2 | somme | Console |
| :-: | :-: | :-: | :-: | ---- |
| 1 |   |   |    | Saisir deux nombres pour en faire la somme |
| 2 |   |   |    | Nombre 1 : |
| 3 | 5 |   |    |  | 
| 4 |   |   |    | Nombre 2 : |
| 5 |   | 10 |   |  |
| 6 |   |   | 15 |  |
| 7 |   |   |    | La somme des deux nombres saisis est égale à : 15 |
