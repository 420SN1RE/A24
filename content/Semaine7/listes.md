+++
title = "Les listes"
weight = 73
+++


## Comment créer une liste

```python
ma_liste_vide = []
ma_liste = [1, 2, 3, 4, 5]
```

## Comment accéder aux éléments d'une liste

```python
premier_element = ma_liste[0]  # Accède au premier élément
dernier_element = ma_liste[-1]  # Accède au dernier élément
```

## Comment ajouter ou supprimer des éléments

```python
ma_liste.append(6)  # Ajoute 6 à la fin de la liste
ma_liste.remove(3)  # Supprime la première occurrence de 3
```

## Comment modifier un élément d'une liste

```python
ma_liste[1] = 10  # Change le deuxième élément en 10
```

## Comment lire les éléments d'une liste un à un (boucle)

```python
for element in ma_liste:
    print(element)
```

## Comment extraire une sous-liste d'une liste

```python
sous_liste = ma_liste[1:3]  # Prend les éléments de l'indice 1 à 2
```

## Comment obtenir l'indice (position) d'un élément dans une liste

```python
ma_liste.index(element, debut, fin)
```


