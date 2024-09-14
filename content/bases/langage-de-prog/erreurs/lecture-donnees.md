+++
title = "Erreurs lors de la lecture de données au clavier"
weight = 3
+++


![Erreurs lecture données](../erreur-input.jpeg?width=20vw)

## Les erreurs communes lors de la lecture de données au clavier 

La lecture de données au clavier en Python peut être source d'erreurs, mais en suivant les bonnes pratiques et en utilisant les astuces mentionnées, vous pouvez éviter ces erreurs et rendre votre code plus robuste. 

La lecture de données au clavier est une tâche courante en Python, souvent réalisée avec la fonction `input()`. Cependant, des erreurs peuvent survenir, surtout pour les débutants. Explorons les erreurs courantes et voyons comment les éviter et les détecter facilement.

### 1. Erreurs de type

**Erreurs courantes :**

- **Conversion de type** : La fonction `input()` retourne toujours une chaîne de caractères. Oublier de convertir cette chaîne en un autre type peut causer des erreurs.
  ```python
  age = input("Entrez votre âge : ")
  print(age + 5)  # TypeError: can only concatenate str (not "int") to str
  ```

**Astuces pour les éviter :**

- **Conversion explicite** : Convertir la chaîne de caractères en l'autre type nécessaire.
  ```python
  age = int(input("Entrez votre âge : "))
  print(age + 5)
  ```
- **Utilisation de `try` et `except`** : Gérer les exceptions pour éviter les plantages du programme.
  ```python
  try:
      age = int(input("Entrez votre âge : "))
      print(age + 5)
  except ValueError:
      print("Veuillez entrer un nombre valide.")
  ```

### 2. Entrées inattendues

**Erreurs courantes :**
- **Entrées vides** : L'utilisateur peut appuyer sur Entrée sans rien saisir, ce qui peut causer des erreurs si le programme attend une entrée spécifique.
  ```python
  name = input("Entrez votre nom : ")
  if name == "":
      print("Erreur : le nom ne peut pas être vide.")
  ```

**Astuces pour les éviter :**

- **Validation des entrées** : Vérifier que l'entrée n'est pas vide et correspond aux attentes.
  ```python
  name = input("Entrez votre nom : ")
  while not name.strip():
      print("Erreur : le nom ne peut pas être vide.")
      name = input("Entrez votre nom : ")
  ```

### 3. Gestion des espaces et des caractères spéciaux

**Erreurs courantes :**

- **Espaces non désirés** : Les espaces en début ou fin de chaîne peuvent causer des problèmes lors de la comparaison ou du traitement des données.
  ```python
  password = input("Entrez votre mot de passe : ")
  if password == "secret ":
      print("Accès refusé.")
  ```

**Astuces pour les éviter :**

- **Utilisation de `strip()`** : Supprimer les espaces en début et fin de chaîne.
  ```python
  password = input("Entrez votre mot de passe : ").strip()
  if password == "secret":
      print("Accès accordé.")
  ```

### 4. Lecture de plusieurs valeurs

**Erreurs courantes :**

- **Séparation incorrecte des valeurs** : Lire plusieurs valeurs séparées par des espaces ou des virgules peut causer des erreurs si la séparation n'est pas gérée correctement.
  ```python
  data = input("Entrez deux nombres séparés par une virgule : ")
  num1, num2 = data.split(",")
  print(int(num1) + int(num2))
  ```

**Astuces pour les éviter :**

- **Validation et gestion des exceptions** : Vérifier que les valeurs sont correctement séparées et gérer les exceptions.
  ```python
  data = input("Entrez deux nombres séparés par une virgule : ")
  try:
      num1, num2 = data.split(",")
      print(int(num1) + int(num2))
  except ValueError:
      print("Erreur : veuillez entrer deux nombres séparés par une virgule.")
  ```
