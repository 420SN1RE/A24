+++
title = "Erreurs avec if elif et else"
weight = 4
+++


![Erreurs avec if-elif-else](../erreur-if.jpeg?width=20vw)

## Les erreurs communes avec les structures `if`, `elif` et `else`

Les structures conditionnelles `if`, `elif` et `else` sont fondamentales en programmation pour contrôler le flux d'exécution du programme. Cependant, des erreurs peuvent survenir, surtout pour les débutants. Voici les erreurs courantes et des astuces pour les éviter et les détecter facilement.

### 1. Erreurs de syntaxe

**Erreurs courantes :**

- **Oublier les deux-points (`:`)** : Chaque condition `if`, `elif` et `else` doit se terminer par un deux-points.
  ```python
  if condition
      # Code
  ```

**Astuces pour les éviter :**

- **Relecture du code** : Toujours vérifier que chaque condition se termine par un deux-points.
- **Utilisation de l'IDE** : Utiliser un environnement de développement intégré (IDE) qui souligne les erreurs syntaxiques.

### 2. Indentation incorrecte

**Erreurs courantes :**

- **Mauvaise indentation** : Python utilise l'indentation pour définir les blocs de code. Une mauvaise indentation peut causer des erreurs `IndentationError`.
  ```python
  if condition:
  print("Condition vraie")  # IndentationError
  ```

**Astuces pour les éviter :**

- **Utilisation cohérente des espaces ou des tabulations** : Choisir entre espaces et tabulations et s'y tenir tout au long du code.
- **Configuration de l'éditeur** : Configurer l'éditeur de texte pour afficher les caractères d'espacement et utiliser l'indentation automatique.

### 3. Conditions mal formulées

**Erreurs courantes :**

- **Utilisation incorrecte des opérateurs de comparaison** : Confondre `=` et `==` ou utiliser des opérateurs incorrects.
  ```python
  if a = 5:  # SyntaxError
      # Code
  ```

**Astuces pour les éviter :**

- **Relecture du code** : Vérifier que les opérateurs de comparaison sont utilisés correctement.
- **Tests unitaires** : Écrire des tests pour vérifier que les conditions fonctionnent comme prévu.

### 4. Oublier les cas `elif` et `else`

**Erreurs courantes :**

- **Oublier de couvrir tous les cas possibles** : Ne pas inclure de conditions `elif` ou `else` peut entraîner des comportements inattendus.
  ```python
  if a > 0:
      print("Positif")
  elif a < 0:
      print("Négatif")
  # Que se passe-t-il si a == 0 ?
  ```

**Astuces pour les éviter :**

- **Utilisation de `else`** : Toujours inclure une clause `else` pour couvrir les cas non spécifiés.
  ```python
  if a > 0:
      print("Positif")
  elif a < 0:
      print("Négatif")
  else:
      print("Zéro")
  ```

### 5. Conditions redondantes ou contradictoires

**Erreurs courantes :**

- **Conditions redondantes** : Vérifier la même condition plusieurs fois ou inclure des conditions qui se contredisent.
  ```python
  if a > 0:
      print("Positif")
  elif a > 0:
      print("Toujours positif")  # Condition redondante
  ```

**Astuces pour les éviter :**

- **Simplification des conditions** : Réduire les conditions redondantes et s'assurer qu'elles sont mutuellement exclusives.
  ```python
  if a > 0:
      print("Positif")
  elif a < 0:
      print("Négatif")
  else:
      print("Zéro")
  ```