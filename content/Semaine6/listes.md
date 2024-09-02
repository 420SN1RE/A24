+++
title =  "Les Listes"
weight = 61
+++

![Les listes](../listes.png?width=25vw)

## Pourquoi utiliser des listes ?

### Mise en situation

Vous devez gérer les données des planètes des différents systèmes solaires.
Chaque planète a un nom et une distance par rapport à notre soleil.
Vous ne savez pas combien de planètes sont exactement présentes dans ces systèmes solaires.
Vous devez afficher le nom de toutes les planètes et leur distance par rapport à notre soleil.

#### Solution sans liste

```python
# Saisie de chaque variable
planete_01_nom = "Mercure"
planete_01_distance = 58
planete_02_nom = "Vénus"
# ....
planete_08_distance = 2871


# Affichage des noms et des distances un par un
print(planete_01_nom, planete_01_distance)
# ....
print(planete_08_nom, planete_08_distance)
```

#### Solution avec une liste

L'utilisation des listes permettra d'exécuter cette tâche beaucoup plus facilement.
Vous pourrez ajouter/modifier/enlever des planètes.
Et vous pourrez ajouter plusieurs informations pour chaque planète.  

```python
# Remplissage de la liste
planetes = []
planetes.append(["Mercure", 58])
planetes.append(["Vénus", 108.2])
....
planetes.append(["Uranus", 2871])

# Affichage des noms et des distances dans une boucle
for planete in planetes:
    print(planete[0], planete[1])
```

![Exemple](../exempleListe_01_2.jpg)


## Qu'est-ce qu'une liste ?

En Python, une liste est une collection ordonnée et modifiable d'éléments. Les listes sont utilisées pour stocker plusieurs éléments dans une seule variable et peuvent contenir des éléments de différents types, y compris des nombres, des chaînes de caractères, d'autres listes, etc. Les listes en Python sont définies en utilisant des crochets `[ ]`.

### Caractéristiques d'une liste

- **Ordonnée** : Les éléments de la liste conservent un ordre défini, ce qui signifie que l'ordre dans lequel vous ajoutez les éléments est préservé.
- **Modifiable** : Une liste peut être modifiée après sa création, ce qui signifie que vous pouvez ajouter, supprimer ou changer des éléments.
- **Taille Dynamique** : Une liste en Python peut changer de taille dynamiquement. Vous pouvez ajouter ou supprimer des éléments sans avoir à spécifier la taille initiale de la liste.
- **Hétérogène** : En *Python*, une liste peut contenir des éléments de différents types (entiers, chaînes de caractères, listes, etc.).
    - Bien qu'il est possible de le faire, il faut rester prudent lorsqu'on utilise des listes hétérogènes. Elles pourraient entraîner des erreurs, notamment dans les boucles.


## Comment utiliser une liste ?

### Fonctions et méthodes

| Fonctions |  |
| ---- | ----|
| len() | Retourne la longueur de la liste |
| max() | Retourne la valeur maximum de la liste |
| min() | Retourne la valeur minimum de la liste |


| Méthodes |  |
| ---- | ----|
| append() | Ajoute un élément à la fin de la liste |
| insert() | Ajoute un élément à un endroit spécifique dans la liste |
| remove() | Supprime un élément de la valeur spécifiée |
| pop() | Supprime un élément selon sa position et retourne la valeur |
| del() | Supprime un élément selon sa position |
| [] | Permet d'accéder à un élément de la liste selon sa position |
| extend() | Ajoute tous les éléments d'une liste dans une autre liste |
| clear() | Efface tous les éléments d'une liste |
| index() | Retourne l'indice du premier élément dont la valeur est égale à celle spécifiée |
| sort() | Trie les éléments de la liste |
| reverse() | Inverse l'ordre des éléments de la liste |
| copy() | Retourne une copie superficielle de la liste |


### Opérations simples

#### Création d'une liste

```python
# Création d'une liste vide
ma_liste = []
# ou
ma_liste = list()

# Liste avec des éléments
ma_liste = [6, 3, 8, 9, 7, 3, 1, 2]
```

![Trace 1](../trace_01.png)

![Trace 4](../trace_04.png)


#### Accès aux éléments d'une liste

Les crochets `[]` sont utilisés pour accéder directement à l'élément correspondant.  

```python
# Accès au premier élément
print(ma_liste[0])  # Affiche 6

# Accès au dernier élément
print(ma_liste[-1])  # Affiche 2

# Opérations sur les éléments de la liste
x = ma_liste[1] + ma_liste[3]  # est l'équivalent de 3 + 9, soit les éléments qui se trouve aux indices 1 et 3
print(x)    # Affiche 12
```

Notez que les indices commencent à zéro.

#### Ajout d'éléments

```python
# Liste vide
ma_liste = []
```

![Trace 1](/Semaine6/trace_01.png)


```python
# Ajoute la valeur 6 à la fin de la liste
ma_liste.append(6)
```

![Trace 2](../trace_02.png)

```python
# Ajoute la valeur 3 à la fin de la liste
ma_liste.append(3)
```

![Trace 3](../trace_03.png)

```python
ma_liste.append(8)
ma_liste.append(9)
ma_liste.append(7)
ma_liste.append(3)
ma_liste.append(1)
ma_liste.append(2)
```

![Trace 4](../trace_04.png)

{{%notice style="note" title="Notez"%}}
Chaque nouveau nombre est ajouté dans l'ordre. La liste restera ordonnée dans le reste du code.
{{% /notice%}}


#### Modification des éléments


```python
# La valeur de la case à l'indice 2 est maintenant 0
ma_liste[2] = 0

# La valeur de la case à l'indice 4 est maintenant la même que celle de la case à l'indice 7
ma_liste[4] = ma_liste[7]
```

![Trace 5](../trace_05.png)


```python
# isch...
ma_liste[0] = ma_liste[ma_liste[7]]

# Décomposition du problème
indice = ma_liste[7]   # indice vaut 2
nouvelle_valeur = ma_liste[indice]   # nouvelle_valeur vaut ma_liste[2], soit 0
ma_liste[0] = nouvelle_valeur    # La case à l'indice 0 vaut maintenant 0
```

![Trace 6](../trace_06.png)


```python
# Même logique...
ma_liste[4] = ma_liste[ma_liste[7] + ma_liste[6]]

# Décomposition du problème
indice = ma_liste[7] + ma_liste[6]   # indice vaut 3
nouvelle_valeur = ma_liste[indice]   # nouvelle_valeur vaut ma_liste[3], soit 9
ma_liste[4] = nouvelle_valeur    # La case à l'indice 4 vaut maintenant 9
```

![Trace 7](../trace_07.png)


#### Suppression d'éléments


```python
# Supprime le dernier élément de la liste
ma_liste.pop()
```

![Trace 8](../trace_08.png)


```python
# Supprime l'élément à l'indice 2
ma_liste.pop(2)
```

![Trace 9](../trace_09.png)


```python
# Supprime la première occurrence de la valeur 3
ma_liste.remove(3)
```

![Trace 11](../trace_11.png)

{{%notice style="note" title="Notez"%}}
Lors de la suppression, les valeurs **après** sont décalées.
{{% /notice%}}


#### Insertion

```python
# Insert la valeur 7 à la case 3
ma_liste.insert(3, 7)
```

![Trace 10](../trace_10.png)


#### Triage

```python
# La liste est triée en ordre croissant
ma_liste.sort()
```

![Trace 12](../trace_12.png)

```python
# La liste est triée en ordre décroissant
ma_liste.sort(reverse=True)
```

![Trace 13](../trace_13.png)


### Dans une boucle

Un premier exemple serait de parcourir chacun des éléments de la liste avec une boucle `for`:

```python
# Affichage de chacun des éléments de la liste
for element in ma_liste:
    print(element)
```

Il est aussi possible d'utiliser la fonction `range()` afin de parcourir la liste à l'aide des indices:

```python
# On additionne 1 à chaque élément de la liste
for i in range(len(ma_liste)):
    ma_liste[i] = ma_liste[i] + 1
```

Enfin, la boucle `while` peut aussi être utile:

```python
# On affiche les premiers éléments de la liste.
# On arrête dès que le total atteint au moins 10
ma_liste = [1, 2, 3, 4, 5, 6, 7]
total = 0
i = 0
while total < 10:
    print(ma_liste[i])
    i += 1
```

### Les listes dans les listes

Une liste peut comporter tout type d'élément.\
Nous pouvons donc mettre des listes dans des listes.
Nous parlons alors de listes (ou tableaux) à 2 dimensions.

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

## Ateliers

1. [Prise en main des listes](../atelier_listes_prise_en_main.ipynb)

1. [Les listes](../atelier_listes.ipynb)
