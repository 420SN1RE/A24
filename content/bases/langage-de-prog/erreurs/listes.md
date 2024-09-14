+++
title = "Erreurs avec les listes"
weight = 7
+++


![Erreurs avec les listes](../erreur-listes.jpeg?width=20vw)

## Les erreurs communes avec les listes

Les listes sont l'une des structures de données les plus utilisées en Python. Cependant, leur utilisation peut parfois mener à des erreurs courantes. Voici un aperçu de ces erreurs et des astuces pour les éviter ou les détecter facilement.

### 1. **IndexError : Liste hors limites**

**Erreur :**

```python
my_list = [1, 2, 3]
print(my_list[3])  # IndexError: list index out of range
```
**Astuce :** Toujours vérifier la longueur de la liste avant d'accéder à un index.

```python
if index < len(my_list):
    print(my_list[index])
else:
    print("Index hors limites")
```

### 2. **TypeError : Mélange de types**

**Erreur :**

```python
my_list = [1, 'two', 3]
total = sum(my_list)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
**Astuce :** Utiliser des listes homogènes ou convertir les types avant les opérations.

```python
my_list = [1, 2, 3]
total = sum(my_list)  # Correct
```

### 3. **Modification de la liste pendant l'itération**

**Erreur :**

```python
my_list = [1, 2, 3, 4]
for item in my_list:
    if item % 2 == 0:
        my_list.remove(item)  # Cela peut causer des éléments manquants
```
**Astuce :** Itérer sur une copie de la liste ou utiliser une compréhension de liste.

```python
# Itérer sur une copie
for item in my_list[:]:
    if item % 2 == 0:
        my_list.remove(item)

# Utiliser une compréhension de liste
my_list = [item for item in my_list if item % 2 != 0]
```

### 4. **Utilisation incorrecte de `append` et `extend`**

**Erreur :**

```python
my_list = [1, 2, 3]
my_list.append([4, 5])  # Résultat : [1, 2, 3, [4, 5]]
```
**Astuce :** Utiliser `extend` pour ajouter plusieurs éléments.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])  # Résultat : [1, 2, 3, 4, 5]
```

### 5. **Confusion entre `copy` et `deepcopy`**

**Erreur :**

```python
import copy
my_list = [[1, 2], [3, 4]]
new_list = copy.copy(my_list)
new_list[0][0] = 9  # Modifie aussi my_list
```
**Astuce :** Utiliser `deepcopy` pour copier des listes imbriquées.

```python
new_list = copy.deepcopy(my_list)
new_list[0][0] = 9  # Ne modifie pas my_list
```