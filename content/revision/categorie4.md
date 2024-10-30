+++
title = "La boucle for"
weight = 4
+++


La boucle `for` permet de parcourir une séquence (comme une liste, une chaîne de caractères, ou une plage de nombres) et d'exécuter un bloc de code pour chaque élément de cette séquence. 

### Syntaxe de la boucle for

La syntaxe de base de la boucle `for` est la suivante :

```python
for element in sequence:
    # bloc de code à exécuter pour chaque élément
```

Voici un exemple simple qui parcourt une liste de nombres et imprime chaque nombre :

```python
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    print(nombre)
```

Dans cet exemple, la boucle `for` parcourt chaque élément de la liste `nombres` et l'imprime.

## Utilisation de range()

La fonction `range()` est souvent utilisée avec la boucle `for` pour **générer une séquence de nombres entiers**. La syntaxe de `range()` peut varier, mais voici les formes les plus courantes :

- `range(n)`: Génère une séquence de 0 à `n - 1`.
  ```python
  for i in range(5):
      print(i)  # Imprime les nombres de 0 à 4
  ```

- `range(debut, n)`: Génère une séquence de `debut` à `n - 1`.
  ```python
  for i in range(2, 6):
      print(i)  # Imprime les nombres de 2 à 5
  ```

- `range(debut, n, saut)`: Génère une séquence de `debut` à `n - 1`, en incrémentant de `saut`.
  ```python
  for i in range(1, 10, 2):
      print(i)  # Imprime les nombres 1, 3, 5, 7, 9
  ```

## L'instruction break

L'instruction `break` permet de sortir immédiatement de la boucle, même si tous les éléments de la séquence n'ont pas été parcourus. 

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Dans cet exemple, la boucle s'arrête lorsque `i` vaut 5, grâce à l'instruction `break`.

### L'instruction continue

L'instruction `continue` permet de passer immédiatement à l'itération suivante de la boucle, en sautant le reste du code à l'intérieur de la boucle pour l'itération en cours.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

Dans cet exemple, seuls les nombres impairs sont imprimés, car l'instruction `continue` fait passer immédiatement à l'itération suivante lorsque `i` est pair.

## Boucles imbriquées

Il est possible d'imbriquer des boucles `for` pour effectuer un certain nombre de fois des instructions répétées :

Exemple se trouvant dans l'examen formatif:
```python
x = 0
for i in range(4):
    for j in range(4):
        x = x + j
print()
```