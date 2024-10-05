+++
title = 'Les listes de listes'
weight = 5
+++

![Listes de listes](listes-listes.jpeg?width=25vw)

## Les listes dans les listes

Une liste peut comporter tout type d'élément. Nous pouvons donc mettre des listes dans des listes. Nous parlons alors de listes (ou tableaux) à 2 dimensions.

```python
# Liste contenant 3 éléments
# Chaque élément est une liste contenant 2 nombres
matrice = [[1, 2], [3, 4], [5, 6]]
```

Pour parcourir toutes les listes, il suffit de mettre une boucle dans une boucle :

```python
# On parcourt chaque éléments de la liste principale
for sous_liste in matrice:
    # et ensuite chaque élément de la "sous-liste"
    for element in sous_liste:
        print(element)
```

Les opérations vues sur les listes en 1 dimension fonctionnent aussi pour les listes en 2D:

```python
print(matrice[0]) # affiche la première liste de la matrice
print(matrice[0][1]) # affiche le 2e élément de la première liste de la matrice

matrice.append([7, 8]) # ajoute une nouvelle liste à la matrice
```

Comme nous l'avons vu plus haut, la fonction `range()` peut aussi être utilisé pour parcourir les listes à 2 dimensions :

```python
# On ajoute 1 à chaque élément de la matrice
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        matrice[i][j] += 1
```