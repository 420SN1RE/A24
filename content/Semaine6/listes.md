+++
title =  "Les Listes"
weight = 61
+++

![Les listes](../listes.png?width=25vw)

## L'importance des listes

Les listes sont l’une des structures de données les plus utilisées en Python. Elles permettent de **stocker plusieurs éléments de différents types dans une seule variable**, ce qui les rend très pratiques pour gérer des collections de données.

{{% notice style=info title=Définition %}}
Une liste est une collection **ordonnée** et **modifiable** d’éléments. Chaque élément de la liste a une position définie, appelée **index**, qui **commence à 0 pour le premier élément**.
{{% /notice %}}

Les listes sont particulièrement utiles pour :

- **Gérer des collections de données** : Par exemple, une liste de noms, de numéros, ou d'éléments complexes (objets).
- **Effectuer des opérations à répétition** : Parcourir les éléments d’une liste pour les traiter.
- **Modifier des données** : Ajouter, supprimer ou modifier des éléments de la liste.

## Pourquoi utiliser des listes ?

### Mise en situation

Vous devez gérer les données des planètes des différents systèmes solaires.
Chaque planète a un **nom** et une **distance** par rapport à notre soleil.
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

Les listes en Python sont définies en utilisant des crochets `[ ]`.

### Caractéristiques d'une liste

- **Ordonnée** : Les éléments de la liste conservent un ordre défini, ce qui signifie que l'ordre dans lequel vous ajoutez les éléments est préservé.
- **Modifiable** : Une liste peut être modifiée après sa création, ce qui signifie que vous pouvez ajouter, supprimer ou changer des éléments.
- **Taille Dynamique** : Une liste en Python peut changer de taille dynamiquement. Vous pouvez ajouter ou supprimer des éléments sans avoir à spécifier la taille initiale de la liste.
- **Hétérogène** : En *Python*, une liste peut contenir des éléments de différents types (entiers, chaînes de caractères, listes, etc.).
    - Bien qu'il est possible de le faire, il faut rester prudent lorsqu'on utilise des listes hétérogènes. Elles pourraient entraîner des erreurs, notamment dans les boucles.

## Création d'une liste

Pour créer une liste en Python, on utilise des crochets [] :

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

## Accès aux éléments d'une liste

Les crochets `[]` sont aussi utilisés pour accéder directement à l'élément correspondant.

{{% notice note %}}
**Rappel** : Les indices commencent à zéro.
{{% /notice %}}


```python
# Accès au premier élément
print(ma_liste[0])  # Affiche 6

# Accès au dernier élément
print(ma_liste[-1])  # Affiche 2

# Opérations sur les éléments de la liste
x = ma_liste[1] + ma_liste[3]  # est l'équivalent de 3 + 9, soit les éléments qui se trouve aux indices 1 et 3
print(x)    # Affiche 12
```

## Modification des éléments d'une liste

Les listes sont modifiables, ce qui signifie que l’on peut changer la valeur des éléments :

```python
# La valeur de la case à l'indice 2 est maintenant 0
ma_liste[2] = 0

# La valeur de la case à l'indice 4 est maintenant la même que celle de la case à l'indice 7
ma_liste[4] = ma_liste[7]
```

![Trace 5](../trace_05.png)


## Ajout et suppression d’éléments d'une liste

On peut ajouter des éléments à une liste avec `append()` ou `insert()`, et les supprimer avec `remove()` ou `pop()`.

### Ajout d'éléments

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

{{%notice style="note" %}}
Chaque nouveau nombre est ajouté dans l'ordre. La liste conservera cet ordre, s'il n'est pas volontairement modifié dans le code.
{{% /notice%}}

### Insertion d'éléments

```python
ma_liste = [0, 9, 9, 3, 1]
# Insert la valeur 7 à la case 3
ma_liste.insert(3, 7)
```

![Trace 10](../trace_10.png)


### Suppression d'éléments

{{%notice style="warning" title=Attention %}}
Lors de la suppression, les valeurs **après** sont décalées.
{{% /notice%}}

```python
ma_liste = [0, 3, 0, 9, 9, 3, 1, 2]
# Supprime le dernier élément de la liste
ma_liste.pop()
```

![Trace 8](../trace_08.png)


```python
ma_liste = [0, 3, 0, 9, 9, 3, 1]
# Supprime l'élément à l'indice 2
ma_liste.pop(2)
```

![Trace 9](../trace_09.png)


```python
ma_liste = [0, 3, 9, 9, 3, 1]
# Supprime la première occurrence de la valeur 3
ma_liste.remove(3)
```

![Trace 11](../trace_11.png)


## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)

## Parcourir les éléments d'une liste (à l'aide d'une **boucle**)

Un premier exemple serait de parcourir chacun des éléments de la liste avec une boucle `for`:

```python
ma_liste = [1, 2, 3, 4, 5, 6, 7]

# Affichage de chacun des éléments de la liste
for element in ma_liste:
    print(element, end=",")	# Affiche  1, 2, 3, 4, 5, 6, 7
```

Il est aussi possible d'utiliser la fonction `range()` afin de parcourir la liste à l'aide des indices:

```python
ma_liste = [1, 2, 3, 4, 5, 6, 7]

# On additionne 1 à chaque élément de la liste
for i in range(len(ma_liste)):
    ma_liste[i] = ma_liste[i] + 1	
    
print(ma_liste, end=" ")	# Affiche 2 3 4 5 6 7 8
```

Enfin, la boucle `while` peut aussi être utile:

```python
# On affiche les premiers éléments de la liste.
# On arrête dès que le total des nombres lus dépasse 10

ma_liste = [1, 2, 3, 4, 5, 6, 7]

total = 0
i = 0
while total < 10:
    print(ma_liste[i], end=".")
    total += ma_liste[i]
    i += 1
``` 

Affiche:

```python
1.2.3.4.
```

## Autres manipulations courantes sur les listes

### Faire la somme de tous les éléments d'une liste.

Avec `sum(ma_liste)` on obtient la somme des éléments numériques d'une liste. Par exemple:

```python
notes = [15, 18, 12, 20, 17]
somme = sum(notes)
print("La somme des notes est: ", somme)
```
Cela affiche:
```python
La somme des notes est:  82
```

### Obtenir le nombre d'éléments d'une liste (sa taille ou longueur).

La méthode `len(ma_liste)` donne le nombre d'éléments de la liste. Par exemple:

```python
notes = [15, 18, 12, 20, 17]
nb_notes = len(notes)
print("La liste contient", nb_notes, "notes")
```

Résultat :
```python
La liste contient 5 notes
```

### Trier les éléments d'une liste.

La méthode `ma_list.sort()` en Python est utilisée pour trier les éléments d'une liste. Exemples: 

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


{{% notice style=warning title=Attention %}}
Lorsqu'il s'agit de chaînes de caractères (`str`) avec un mélange de majuscules et de minuscules, le tri se fait par défaut en premier sur les **majuscules** et après sur les **minuscules**. Ce comportement vient de leur position dans la [table ASCII](https://www.purebasic.com/french/documentation/reference/ascii.html). 
{{% /notice %}}

Par exemple:

La liste **`['Banane', 'ananas', 'Cerise']`** sera triée en **`['Banane', 'Cerise', 'ananas']`**.
 
Pour effectuer un tri sans tenir compte de la casse, vous pouvez utiliser le paramètre `key` avec la fonction `str.lower`, comme ceci : 
`ma_list.sort(key=str.lower)`. Cela convertira temporairement chaque élément en minuscules pour le tri, tout en conservant la casse originale dans la liste triée.

Exemple :
 
```python
ma_liste = ['Banane', 'ananas', 'Cerise']

ma_liste.sort(key = str.lower)
print(ma_liste)	# Affiche ['ananas', 'Banane', 'Cerise']
```

### Trouver les éléments uniques d'une liste.

Dans ce cas, on utilise `list()` et `set()`, comme dans cet exemple:

```python
ma_liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

uniques = list(set(ma_liste))
print(uniques)  # Affiche [1, 2, 3, 4, 5]
```

### Filtrer les nombres pairs d'une liste.

{{% notice info %}}
L'opérateur modulo (`%`) est utilisé ici pour vérifier si un nombre est divisible par 2 sans reste, ce qui signifie qu'il est pair.
{{% /notice %}}

Pour extraire les nombres pairs d'une liste, en utilisant l'opérateur modulo (`%`), vous pouvez utiliser une compréhension de liste comme suit :

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pairs = [nombre for nombre in nombres if nombre % 2 == 0]
print(pairs)  # Affiche [2, 4, 6, 8, 10]
```

Explication: 

- La ligne de code **`pairs = [nombre for nombre in nombres if nombre % 2 == 0]`** utilise une compréhension de liste pour créer une nouvelle liste contenant uniquement les nombres pairs de la liste `nombres`. 
- **`nombre for nombre in nombres`** : Cette partie de la compréhension de liste itère sur chaque élément de la liste `nombres`.
- **`if nombre % 2 == 0`** : Cette condition utilise l'opérateur modulo (`%`) pour vérifier si le nombre est divisible par 2 sans reste. Si c'est le cas, le nombre est pair et il est ajouté à la nouvelle liste `pairs`.


## D'autres fonctions ou méthodes de listes


| Fonction ou méthode | Description |
| ---- | ----|
| max() | Retourne la valeur maximum de la liste |
| min() | Retourne la valeur minimum de la liste |
| del() | Supprime un élément selon sa position |
| extend() | Ajoute tous les éléments d'une liste dans une autre liste |
| clear() | Efface tous les éléments d'une liste |
| index() | Retourne l'indice du premier élément dont la valeur est égale à celle spécifiée |
| reverse() | Inverse l'ordre des éléments de la liste |
| copy() | Retourne une copie superficielle de la liste |

## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)

===

### Les listes dans les listes ???

Une liste peut comporter tout type d'élément.  
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