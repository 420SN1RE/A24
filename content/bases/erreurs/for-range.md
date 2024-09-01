+++
title = "Erreurs avec la boucle for et la fonction range"
weight = 6
+++


![Erreurs avec for et range](../erreur-for-range.jpeg?width=20vw)

## Les erreurs communes avec la boucle `for` et la fonction `range()`

La boucle `for` et la fonction `range()` sont des outils puissants en Python pour itérer sur des séquences. Cependant, des erreurs peuvent survenir, surtout pour les débutants. Explorons les erreurs courantes et des astuces pour les éviter et les détecter facilement.

### 1. Erreurs de syntaxe avec `range()`

**Erreurs courantes :**

- **Oublier les parenthèses** : La fonction `range()` nécessite des parenthèses pour fonctionner correctement.
  ```python
  for i in range 10:  # SyntaxError
      print(i)
  ```

**Astuces pour les éviter :**

- **Relecture du code** : Toujours vérifier que `range()` est utilisé avec des parenthèses.
  ```python
  for i in range(10):
      print(i)
  ```

### 2. Mauvaise utilisation des arguments de `range()`

**Erreurs courantes :**

- **Arguments incorrects** : Utiliser des arguments incorrects ou dans le mauvais ordre peut causer des erreurs.
  ```python
  for i in range(10, 1):  # Ne produit aucune itération
      print(i)
  ```

**Astuces pour les éviter :**

- **Compréhension des arguments** : `range(start, stop, step)` où `start` est inclusif, `stop` est exclusif, et `step` est l'incrément.
  ```python
  for i in range(1, 10, 2):
      print(i)  # Affiche 1, 3, 5, 7, 9
  ```

### 3. Boucles infinies avec `range()`

**Erreurs courantes :**

- **Incrément incorrect** : Utiliser un incrément incorrect peut causer des boucles infinies ou des itérations inattendues.
  ```python
  for i in range(10, 0, -1):
      print(i)  # Affiche 10, 9, 8, ..., 1
  ```

**Astuces pour les éviter :**

- **Vérification des arguments** : S'assurer que l'incrément est cohérent avec les valeurs de début et de fin.
  ```python
  for i in range(10, 0, -1):
      print(i)  # Affiche 10, 9, 8, ..., 1
  ```

### 4. Modification de la séquence pendant l'itération

**Erreurs courantes :**

- **Modification de la liste** : Modifier une liste pendant son itération peut causer des comportements inattendus.
  ```python
  numbers = [1, 2, 3, 4, 5]
  for num in numbers:
      if num % 2 == 0:
          numbers.remove(num)
  print(numbers)  # Résultat inattendu
  ```

**Astuces pour les éviter :**

- **Itération sur une copie** : Itérer sur une copie de la liste pour éviter les modifications pendant l'itération.
  ```python
  numbers = [1, 2, 3, 4, 5]
  for num in numbers[:]:
      if num % 2 == 0:
          numbers.remove(num)
  print(numbers)  # Affiche [1, 3, 5]
  ```

### 5. Utilisation incorrecte de `enumerate()`

**Erreurs courantes :**

- **Mauvaise gestion des indices** : Utiliser `enumerate()` sans comprendre son fonctionnement peut causer des erreurs.
  ```python
  fruits = ["pomme", "banane", "cerise"]
  for fruit in enumerate(fruits):
      print(fruit)  # Affiche (0, 'pomme'), (1, 'banane'), (2, 'cerise')
  ```

**Astuces pour les éviter :**

- **Déballage des tuples** : Utiliser le déballage des tuples pour accéder aux indices et aux valeurs.
  ```python
  fruits = ["pomme", "banane", "cerise"]
  for index, fruit in enumerate(fruits):
      print(index, fruit)  # Affiche 0 pomme, 1 banane, 2 cerise
  ```